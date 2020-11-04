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

    removeButton = '<button class="del" onclick="removeTacoBell(' + cartSize + ')">X</button';
    tacoBellTotal.innerHTML = 'Total: $' + total;
    tacoBellCart.innerHTML += '<li>' + name + ': $' + price + removeButton + '</li>';
}

// Stores tacoBell items in shopping cart
function tacoBellShoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;
    tacoBellCart.innerHTML = '';
    for(let i=0; i<cartSize; i++){
        removeButton = '<button class="del" onclick="removeTacoBell(' + i + ')">X</button>';
        tacoBellCart.innerHTML += '<li>'+ orders[i][0] + ': $' + orders[i][1] + removeButton +'</li>';
    }
    tacoBellTotal.innerHTML = 'Total: $' + total;
}

tacoBellShoppingCart();

function removeTacoBell(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');

    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);

    // Updates the number of items in cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    tacoBellShoppingCart();
}
 