var express = require('express');
var bodyParser = require('body-parser');
var request = require("request")

var app = express();

app.use(express.static('static'));

app.use(bodyParser.json());

require("./server/routes/login")(app);
/*
app.get('/challenge.html', function(req, res){
    var url = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB?max=1000000&loops=1"

    request(url, function(error, response, body) {
        console.log(body);
        res.send(body);
    });

});
*/


var server = app.listen(3000, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("Example app listening at http://%s:%s", host, port)


});
