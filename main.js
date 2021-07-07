//  Add email and password to an object when submitted

var objects = {};
var form = document.getElementById('form');
form.onsubmit = function(e){
    var item = document.getElementById('item').value, email =document.getElementById('email').value, password = document.getElementById('password').value;
    objects[item] = {'email':email, 'password':password}
    console.log(JSON.stringify(objects));
    e.preventDefault();
}