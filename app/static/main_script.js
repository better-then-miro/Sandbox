var namespace = '/main';
console.log(location.protocol + '//' + document.domain + ':' + location.port + namespace)
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

socket.on('confirmer', function (msg){
    console.log("data was received")
});

socket.on('kek', function (msg){
    alert(msg.data)
});

function send_message() {
    var msg = document.getElementById("MessageBox").value;
    socket.emit("getMessage", {message:msg});
};