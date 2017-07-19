var http = require('http');
var server = http.createServer().listen(4000);
var io = require('socket.io').listen(server);
var cookie_reader = require('cookie');
var querystring = require('querystring');

var redis = require('redis');
var sub = redis.createClient();

//Subscribe to the Redis chat channel
sub.subscribe('chat');


io.sockets.on('connection', function (socket) {

    //Grab message from Redis and send to client
    sub.on('message', function(channel, message){
      console.log(message)
        socket.send(message);
    });

    //Client is sending message through socket.io
    socket.on('send_message', function (message) {
      console.log(message)
        values = querystring.stringify({
            comment: message.msg,
            csrfmiddlewaretoken: message.csrf,
            session: message.session_id,
        });
        console.log(values)
        var options = {
            host: 'localhost',
            port: 8000,
            path: '/node_api/',
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'csrftoken=' + message.csrf,
                'Content-Length': values.length
            }
        };

        //Send message to Django server
        var req = http.request(options, function(res){
            res.setEncoding('utf8');

            //Print out error message
            res.on('data', function(message){
                if(message != 'Everything worked :)'){
                    console.log('Message: ' + message.msg);
                }
            });
        });

        req.write(values);
        req.end();
    });
});
