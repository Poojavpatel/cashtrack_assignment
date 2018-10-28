const express = require('express');
const router = express.Router();
var json2csv = require('json2csv');
 
router.get('/', async(req, res) => {
    var fields = ['name','info'];
    var csv = json2csv({ data: '', fields: fields });
    res.set("Content-Disposition", "attachment;filename=authors.csv");
    res.set("Content-Type", "application/octet-stream");
    res.send(csv);
});

module.exports = router;
