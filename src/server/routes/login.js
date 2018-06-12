module.exports = function (app) {

    /**
     * This function validates log in details
     */
    app.post('/api/login', function (req, res) {
        let username = req.body.username;
        let password = req.body.password;
        if(username == 'admin' && password == 'admin') {
            res.send({
                valid: true
            });
        } else {
            res.send({
                valid: false
            });
        }

    });

    /**
     * This excludes some pages (public pages for the participants) from having to login
     */
    app.use(function(req, res, next){
        var str = req.url;
        var patt = /challenge/g;
        console.log(str)
        console.log(patt.test(str))

        if(patt.test(str)){
            next();
            return;
        }
        res.status(401).send("Not logged in");

    });

};