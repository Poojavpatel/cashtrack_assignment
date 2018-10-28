const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const multer = require('multer');
const ejs = require('ejs');
const app = express();

app.use(express.json());
require('dotenv').config();
app.set('view engine','ejs');
app.use(express.static('./static'))

// connecting to mongodb
const mongouri = process.env.mongoURI;
mongoose.connect(mongouri)
    .then( () => console.log('Connected to MongoDB'))
    .catch( err => console.log('Error while connecting to MongoDB', err));

// set storage engine
const storage = multer.diskStorage({
     destination: './static/uploads/',
     filename: function(req, file, callback) {
         callback(null, file.fieldname + "_" + Date.now() + path.extname(file.originalname));
     }
});
const upload = multer({
    storage : storage
}).single('excelfile');

// Homepage route
app.get('/',(req,res) => {
    res.render('auth.ejs')
});
app.post('/upload',(req,res)=>{
    res.send("snt successfully");
})

port = process.env.PORT || 5000;
app.listen(port,() => console.log(`Server started at port ${port}`));