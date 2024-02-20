var currentDate = new Date();
console.log(currentDate.getMonth());

async function run(){
    var elements=document.getElementsByClassName("input1");
    var arr=[];
    for(let i of elements)
    {
        arr.push(i.value);
    }
    const districts=['District_Adilabad', 'District_Bhadradri','District_Jagitial', 'District_Jangoan', 'District_Jayashankar','District_Jogulamba', 'District_Kamareddy', 'District_Karimnagar','District_Khammam', 'District_Komaram bheem asifabad','District_Mahabubabad', 'District_Mahbubnagar', 'District_Mancherial','District_Medak', 'District_Medchal', 'District_Mulugu','District_Nagarkurnool', 'District_Nalgonda', 'District_Narayanapet','District_Nirmal', 'District_Nizamabad', 'District_Peddapalli','District_Rajanna', 'District_Rangareddy', 'District_Sangareddy','District_Siddipet', 'District_Suryapet', 'District_Vikarabad','District_Wanaparthy', 'District_Warangal', 'District_Warangal urban','District_Yadadri'];
    var district=[];
    for(let i=0;i<districts.length;i++)
    {
        if(arr[0]==districts[i])
        {
            district[i]=1;
        }
        else
        {
            district[i]=0;
        }
    }
    var season=[];
    if(arr[1]=="Season_Kharif")
    {
        season[0]=1;
        season[1]=0;
    }
    else
    {
        season[0]=0;
        season[1]=1;
    }
    const crops=['Crop_Groundnut','Crop_Maize', 'Crop_Moong(Green Gram)', 'Crop_Rice','Crop_cotton(lint)'];
    var crop=[];
    for(let i=0;i<crops.length;i++)
    {
        if(arr[2]==crops[i])
        {
            crop[i]=1;
        }
        else
        {
            crop[i]=0;
        }
    }
    console.log(arr);
    console.log(arrf);
    var arrf=arr.slice(3,15).concat(district,season,crop);
    arrf=arrf.map(parseFloat);
    const MODEL_URL = 'http://localhost:3000/model.json';
    const model = await tf.loadLayersModel(MODEL_URL);
    //console.log(model.summary());
    const input = tf.tensor3d(arrf, [1,1,51]);
    const result = await model.predict(input);
    var num=parseFloat(result.toString().slice(14,23))*68.79655917165852;
    document.getElementById("output").innerHTML="Yield of "+arr[2].slice(5)+" is : "+Math.round((num + Number.EPSILON) * 100) / 100+" (Kg/Acre)";
    console.log(Math.round((num + Number.EPSILON) * 100) / 100);
}