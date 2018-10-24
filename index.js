const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const passport = require('passport');
const app = express();

app.use(express.json());

// Homepage route
app.get('/',(req,res) => {
    res.sendFile(path.join(__dirname+'/static/auth.html'));
});

//  Passport setup
app.use(passport.initialize());
app.use(passport.session());
app.get('/success', (req, res) => res.send("Welcome "+req.query.username+"!!"));
app.get('/error', (req, res) => res.send("error logging in"));

passport.serializeUser(function(user, cb) {
    cb(null, user.id);
});
  
passport.deserializeUser(function(id, cb) {
    User.findById(id, function(err, user) {
      cb(err, user);
    });
});

port = process.env.PORT || 5000;
app.listen(port,() => console.log(`Server started at port ${port}`));