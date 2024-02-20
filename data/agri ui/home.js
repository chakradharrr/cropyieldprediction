window.onload = function() {
    var logo = document.querySelector('.logo');
  
    logo.addEventListener('animationend', function() {
      window.location.href = 'blog.html';
    });
  };
  