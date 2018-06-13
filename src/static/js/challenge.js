
$(function() {
    var url1 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB"
    var url2 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/Eratosthenes"
    var url3 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes512MB"
    var url4 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes1024MB"
    var headers = {
        'content-type': "application/json"
    }
    var params={
        "max": 1000000,
        "loops": 1
    }
    $('#128btn').click(function() {
        $.get( url1, params, function( data ) {
            $(".results128").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops);
            console.log(data)
        });
    });
    $('#256btn').click(function() {
        $.get( url2, params, function( data ) {
            $(".results256").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops);
            console.log(data)
        });
    });
    $('#512btn').click(function() {
        $.get( url3, params, function( data ) {
            $(".results512").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops);
            console.log(data)
        });
    });
    $('#1024btn').click(function() {
        $.get( url4, params, function( data ) {
            $(".results1024").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops);
            console.log(data)
        });
    });

});
