var hours = 24;
var now = new Date.getTime();
var stepTime = localStorage.getItem('stepTime');

// Checks if the user has accessed the app within 24 hrs
if(stepTime == null){
    localStorage.setItem('stepTime', now);
}
else{
    if(now - stepTime > hours*60*60*1000){
        localStorage.clear();
        localStorage.setItem('stepTime', now);
    }
}
