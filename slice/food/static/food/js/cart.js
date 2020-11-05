var foodName = document.querySelector("#name");
var price = document.querySelector("#price");
var bill = document.querySelector("#total");
var remove = document.querySelector("#rm");


function shoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =  orders.length;

    foodName.innerHTML = '<h3>Name</h3>';
    price.innerHTML = '<h3>Price</h3>';
    remove.innerHTML = '<h3><br></h3>';

    for(let i=0; i<cartSize; i++){
        remove.innerHTML += '<button class="btn-danger" onclick="removeItem(' + i + ')">X</button>';
        foodName.innerHTML += '<h4>' + orders[i][0] + '</h4>';
        price.innerHTML += '<h4> $' + orders[i][1] + '</h4>';
    }
    bill.innerHTML = 'Total: $' + total;
}

shoppingCart();

function removeItem(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');

    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);

    // Updates the number of items in cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
    
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    shoppingCart();
}

var note = document.querySelector('#message');

// Implementing Ajax
function order(){
    var msg = note.value;
    var orders = localStorage.getItem('orders');

    var ur = '/food/order';
    var orderData = {};
    orderData['orders'] = orders;
    orderData['note'] = msg;
    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        success: function(data){
            window.location.replace('success')
            localStorage.setItem('orders', JSON.stringify([]));
            localStorage.setItem('total', 0);
        }
    })
}