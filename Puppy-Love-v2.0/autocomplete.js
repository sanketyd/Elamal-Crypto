express=require('express');
app=express();
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('students.db');
var request=require('request');
var http = require('http').Server(app);
var io = require('socket.io')(http);
app.use(express.static(__dirname+'/templates'));
http.listen(8080);
io.on('connection',function(socket){
	socket.on('name',function(data){
		db.each("SELECT rowid AS id,name,imgsrc,roll_no FROM students",function(err,row){
			socket.emit('names',{name:row.name})
			if(row.name===data.name){socket.emit('pic',{pic:row.imgsrc})}
		});
	});
	socket.on('crushes',function(data){
		
	});
});
