const express = require('express');

const app = express();

app.use(express.json());

// Homepage route
app.get('/',(req,res) => {
    res.send("welcome to homepage");
});

port = process.env.PORT || 5000;
app.listen(port,() => console.log(`Server started at port ${port}`));