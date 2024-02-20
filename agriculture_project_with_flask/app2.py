from flask import Flask, request, url_for, redirect, render_template
import pickle as p
import numpy as np
import requests
app=Flask(__name__)
model=p.load(open("model.pkl","rb"))
# def prediction(input_data):
#     url = "https://pcmk4tdl8k.execute-api.ap-south-1.amazonaws.com/agristage/agiapi"


#     # payload = "215.82,24.9,35.0,7.7,278.7,30.5,357.0,1.43,15.33,1.63,19.33,29.09,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0"
#     my_string = ','.join(map(str, input_data[0]))
#     print(my_string)
#     headers = {
#     'Content-Type': 'text/csv'
#     }

#     response = requests.request("POST", url, headers=headers, data=my_string)

#     # print(response.text)
#     res=response.json()
#     return res["Prediction"]
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/yield")
def Yield():
    return render_template("yield.html")
@app.route("/data")
def data():
    return render_template("data.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
    d=request.form
    districts=['District_Adilabad', 'District_Bhadradri Kothagudem', 'District_Jagtial', 'District_Jangoan',
                 'District_Jayashankar Bhoopalpally', 'District_Jogulamba Gadwal', 'District_Kamareddy',
                 'District_Karimnagar', 'District_Khammam', 'District_Komaram bheem asifabad', 'District_Mahabubabad',
                 'District_Mahabubnagar', 'District_Mancherial', 'District_Medak', 'District_Medchal-Malkajgiri',
                 'District_Mulug', 'District_Nagarkurnool', 'District_Nalgonda', 'District_Narayanpet',
                 'District_Nirmal', 'District_Nizamabad', 'District_Peddapalli', 'District_Rajanna Sircilla',
                 'District_Rangareddy', 'District_Sangareddy', 'District_Siddipet', 'District_Suryapet',
                 'District_Vikarabad', 'District_Wanaparthy', 'District_Warangal', 'District_Hanumakonda',
                 'District_Yadadri Bhuvanagiri']
    dis=[0]*32
    dis[districts.index(d["district"])]=1
    season=[0,0]
    if(d["season"]=="Season_Kharif"):
        season[0]=1
    else:
        season[1]=1
    crops=['Crop_Groundnut', 'Crop_Maize','Crop_Moong(Green Gram)', 'Crop_Rice', 'Crop_cotton(lint)']
    crop=[0]*5
    #crop[crops.index(d['crop'])]=1
    for i in range(len(crops)):
        if crops[i]==d["crop"]:
            crop[i]=1
    l=list(d.values())
    r=l[3:]
    l1=r+dis+season+crop
    a=np.array([l1])
    a = np.array(a, dtype=float)
    print(a)
    output=model.predict(a)[0]
    print(output)
    out=round(output,2)
    print(out)
    if d['crop']=='Crop_cotton(lint)':
        return render_template("yield.html",out=f"Predicted Yield of {d['crop'][5:]} is  {out}  bales/hectare")
    else:
        return render_template("yield.html",out=f"Predicted Yield of {d['crop'][5:]} is  {out}  tones/hectare")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)