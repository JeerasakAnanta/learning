const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const authRoutes = require('./routes/auth');

// db
const db = require('./configs/db');


// config() จะอ่านไฟล์ .env และเก็บค่าไว้ใน process.env
require('dotenv').config(); 


const app = express();
const PORT = 3030;

// Middleware setup
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: process.env.SECRET_KEY,
    resave: false,
    saveUninitialized: true
}));

// ใช้งาน Routing
app.use('/', authRoutes);

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});