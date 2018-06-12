/**
 * This is the logic for dynamically displaying the login.html page
 */

$(function() {
    $('#loginbtn').click(function() {
        let pword = $('#password').val();
        let user = $('#username').val();

        $.post({
            url: '/api/login',
            data: JSON.stringify({
                username: user,
                password: pword
            }),
            contentType: 'application/json'
        }).then(function(response) {
            console.log(response)
            if(response.valid) {
                window.location.href = "/challenge.html";
            }else {
                alert("Invalid Username and Password");
            }
        });
    });
});
