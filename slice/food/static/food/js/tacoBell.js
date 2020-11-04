var tacoBellCart = document.querySelector('#tacoBellCart');
var tacoBellTotal = document.querySelector('#tacoBellTotal');

// Adds tacoBell Product
function addTacoBell(tacoBellId){
    // Gets the product name
    tacoBell = '#taco' + tacoBellId;
    var name = document.querySelector(tacoBell).innerHTML;
   
    // Gets the product price
    var radio = 'tacoBell' + tacoBellId;
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

    tacoBellTotal.innerHTML = 'Total: $' + total;
    tacoBellCart.innerHTML += '<li>' + name + ': $' + price + '</li>';
}

// Stores tacoBell items in shopping cart
function tacoBellShoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;
    tacoBellCart.innerHTML = '';
    for(let i=0; i<cartSize; i++){
        tacoBellCart.innerHTML += '<li>'+ orders[i][0] + ': $' + orders[i][1] + '</li>';
    }
    tacoBellTotal.innerHTML = 'Total: $' + total;
}

tacoBellShoppingCart();

 