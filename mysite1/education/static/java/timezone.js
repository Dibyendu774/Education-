var timer = setTimeout(register, 120000);


function register(){

if (! isRegistered){

alert('Register To Continue')

}

}

document.addEventListener('mousemove', function(){

clearTimeout(timer);

timer = setTimeout(register, 120000)

});