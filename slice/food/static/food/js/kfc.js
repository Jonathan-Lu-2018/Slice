var kfcCart = document.querySelector('#kfcCart');
var kfcTotal = document.querySelector('#kfcTotal');

// Adds Kfc Product
function addKfc(kfcId){
    // Gets the product name
    kfc = '#k' + kfcId;
    var name = document.querySelector(kfc).innerHTML;
   
    // Gets the product price
    var radio = 'kfc' + kfcId;
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

    kfcTotal.innerHTML = 'Total: $' + total;
    kfcCart.innerHTML += '<li>' + name + ': $' + price + '</li>';
}

// Stores Kfc items in shopping cart
function kfcShoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;
    kfcCart.innerHTML = '';
    for(let i=0; i<cartSize; i++){
        kfcCart.innerHTML += '<li>'+ orders[i][0] + ': $' + orders[i][1] + '</li>';
    }
   kfcTotal.innerHTML = 'Total: $' + total;
}

kfcShoppingCart();

 