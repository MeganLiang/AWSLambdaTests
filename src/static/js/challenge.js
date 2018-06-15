
$(function() {
    var url2 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB";
    var url1 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/Eratosthenes";
    var url3 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes512MB";
    var url4 = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes1024MB";
    var headers = {
        'content-type': "application/json"
    }
    var params={
        "max": 1000000,
        "loops": 2
    }
    $('#128btn').click(function() {
        var start = new Date().getTime();
        $.get( url1, params, function( data ) {
            var time = (new Date().getTime() - start)/1000;
            console.log(time)
            $(".results128").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + time);
            console.log(data.durationSeconds)
        });
    });
    $('#256btn').click(function() {
        var start = new Date().getTime();
        $.get( url2, params, function( data ) {
            var time = (new Date().getTime() - start)/1000;
            console.log(time)
            $(".results256").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + time);
            console.log(data.durationSeconds)
        });
    });
    $('#512btn').click(function() {
        var start = new Date().getTime();
        $.get( url3, params, function( data ) {
            var time = (new Date().getTime() - start)/1000;
            console.log(time)
            $(".results512").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + time);
            console.log(data.durationSeconds)
        });
    });
    $('#1024btn').click(function() {
        var start = new Date().getTime();
        $.get( url4, params, function( data ) {

            var time = (new Date().getTime() - start)/1000;
            console.log(time)
            $(".results1024").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + time);
            console.log(data.durationSeconds)
        });
    });
    //-----------------------------------------

    $('#128btn30').click(function() {
        let x = []
        let start = window.performance.now();
        x.push(start)
        for (var i = 0; i< 30; i++) {
            $.get( url1, params, function( data ) {
                let end = window.performance.now();
                x.push(end)
                let time = (x.slice(-1)[0]) - (x.slice(-2)[0])
                $(".results12830").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + (time/1000));
                console.log(data.durationSeconds);
                console.log(time/1000)
            });
        }

    });
    $('#256btn30').click(function() {
        let x = []
        let start = window.performance.now();
        x.push(start)
        for (var i = 0; i< 30; i++) {
            $.get( url2, params, function( data ) {
                let end = window.performance.now();
                x.push(end)
                let time = (x.slice(-1)[0]) - (x.slice(-2)[0])
                $(".results25630").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + (time/1000));
                console.log(data.durationSeconds);
                console.log(time/1000)
            });
        }

    });
    $('#512btn30').click(function() {
        let x = []
        let start = window.performance.now();
        x.push(start)
        for (var i = 0; i< 30; i++) {
            $.get( url3, params, function( data ) {
                let end = window.performance.now();
                x.push(end)
                let time = (x.slice(-1)[0]) - (x.slice(-2)[0])
                $(".results51230").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + (time/1000));
                console.log(data.durationSeconds);
                console.log(time/1000)
            });
        }

    });


    $('#1024btn30').click(function() {
        let x = []
        let start = window.performance.now();
        x.push(start)
        for (var i = 0; i< 30; i++) {
            $.get( url4, params, function( data ) {
                let end = window.performance.now();
                x.push(end)
                let time = (x.slice(-1)[0]) - (x.slice(-2)[0])
                $(".results102430").html('Duration seconds: ' + data.durationSeconds + ' max:' + data.max + ' loops:' + data.loops + ' client response time seconds: ' + (time/1000));
                console.log(data.durationSeconds);
                console.log(time/1000)
            });
        }

    });

});
