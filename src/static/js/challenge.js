
$(function() {
    var url = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB"
    var headers = {
        'content-type': "application/json"
    }
    var params={
        "max": 1000000,
        "loops": 1
    }
    $('#loginbtn').click(function() {
        $.get( url, params, function( data ) {
            $(".results").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops);
            console.log(data)
        });
    });


});
