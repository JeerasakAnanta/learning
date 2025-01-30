// โค้ดสำหรับเชื่อมต่อฐานข้อมูล MySQL ด้วย Node.js  
x =  require('dotenv').config(); 
const mysql = require('mysql');

const db = mysql.createConnection({
    host: 'db', 
    user: process.env.MYSQL_USERNAME, 
    password: process.env.MYSQL_USERNAME, 
    database: process.env.MYSQL_DATABASE
});

db.connect(err => {
    if (err) throw err;
    console.log('MySQL connected...');
});

module.exports = db;