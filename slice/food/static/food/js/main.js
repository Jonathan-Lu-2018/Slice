var hours = 24;
var now = new Date().getTime();
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

var orders = JSON.parse(localStorage.getItem('orders'));
var total = localStorage.getItem('total');

// Checks to see if the user selects an item
if(orders === null || orders === undefined ){
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

// Checks the total cost
if(total === null || total === undefined ){
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total');
}

var cart = document.querySelector("#cart");
cart.innerHTML = orders.length;