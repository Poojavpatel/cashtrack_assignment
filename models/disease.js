var mongoose = require('mongoose');
const diseaseSchema = mongoose.Schema({
    name:{type:String},
    info:{type:String}
});
const Disease = mongoose.model( 'Disease' , diseaseSchema);
module.exports = Disease;