var littleCaesarsCart = document.querySelector('#littleCaesarsCart');
var littleCaesarsTotal = document.querySelector('#littleCaesarsTotal');

// Adds littleCaesars Product
function addLittleCaesars(littleCaesarsId){
    // Gets the product name
    littleCaesars = '#little' + littleCaesarsId;
    var name = document.querySelector(littleCaesars).innerHTML;
   
    // Gets the product price
    var radio = 'littleCaesars' + littleCaesarsId;
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

    removeButton = '<button class="del" onclick="removeLittleCaesars(' + cartSize + ')">X</button>';
    littleCaesarsTotal.innerHTML = 'Total: $' + total;
    littleCaesarsCart.innerHTML += '<li>' + name + ': $' + price + removeButton + '</li>';
}

// Stores littleCaesars items in shopping cart
function littleCaesarsShoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;
    littleCaesarsCart.innerHTML = '';
    for(let i=0; i<cartSize; i++){
        removeButton = '<button class="del" onclick="removeLittleCaesars(' + i + ')">X</button>';
        littleCaesarsCart.innerHTML += '<li>'+ orders[i][0] + ': $' + orders[i][1] + removeButton + '</li>';
    }
    littleCaesarsTotal.innerHTML = 'Total: $' + total;
}

littleCaesarsShoppingCart();

function removeLittleCaesars(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');

    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);

    // Updates the number of items in cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    littleCaesarsShoppingCart();
}