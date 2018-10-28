const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const multer = require("multer");
const cloudinary = require("cloudinary");
const cloudinaryStorage = require("multer-storage-cloudinary");
const app = express();

app.use(express.json());
require('dotenv').config()

// Homepage route
app.get('/',(req,res) => {
    res.sendFile(path.join(__dirname+'/static/auth.html'));
});

port = process.env.PORT || 5000;
app.listen(port,() => console.log(`Server started at port ${port}`));