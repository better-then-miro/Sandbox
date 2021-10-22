var namespace = '/main';
console.log(location.protocol + '//' + document.domain + ':' + location.port + namespace)
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

socket.on('confirmer', function (msg){
    console.log(msg)
});

function send_message() {
    var msg = document.getElementById("MessageBox").value;
    socket.emit("getMessage", {message:msg});
};