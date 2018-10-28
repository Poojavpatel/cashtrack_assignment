const express = require('express');
// const fileUpload = require('express-fileupload');
const path = require('path');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());
// app.use(fileUpload());
require('dotenv').config()

// connecting to mongodb
const mongouri = process.env.mongoURI;
mongoose.connect(mongouri)
    .then( () => console.log('Connected to MongoDB'))
    .catch( err => console.log('Error while connecting to MongoDB', err));

// Homepage route
app.get('/',(req,res) => {
    res.sendFile(path.join(__dirname+'/static/auth.html'));
});
const diseases = require('./routes/diseases.js');
app.use('/a' , diseases);

port = process.env.PORT || 5000;
app.listen(port,() => console.log(`Server started at port ${port}`));