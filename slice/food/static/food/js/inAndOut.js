var inAndOutCart = document.querySelector('#inAndOutCart');
var inAndOutTotal = document.querySelector('#inAndOutTotal');

// Adds InAndOut Product
function addInAndOut(inAndOutId){
    // Gets the product name
    inAndOut = '#in' + inAndOutId;
    var name = document.querySelector(inAndOut).innerHTML;
   
    // Gets the product price
    var radio = 'inAndOut' + inAndOutId;
    var pri = document.getElementsByName(radio);
    var price = pri[0].value;

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;
    // Saves item and item in localStorage
    orders[cartSize] = [name, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // Updates the number of items in cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    inAndOutTotal.innerHTML = 'Total: $' + total;
    inAndOutCart.innerHTML += '<li>' + name + ': $' + price + '</li>';
}

// Stores InAndOut items in shopping cart
function inAndOutShoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;
    inAndOutCart.innerHTML = '';
    for(let i=0; i<cartSize; i++){
        inAndOutCart.innerHTML += '<li>'+ orders[i][0] + ': $' + orders[i][1] + '</li>';
    }
    inAndOutTotal.innerHTML = 'Total: $' + total;
}

inAndOutShoppingCart();

 