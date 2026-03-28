const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');

// รับคำขอที่หน้าเข้าสู่ระบบ
router.get('/login', (req, res) => {
    res.sendFile(__dirname + '/../views/login.html');
});

// จัดการการเข้าสู่ระบบ
router.post('/login', authController.login);

// จัดการการออกจากระบบ
router.get('/logout', authController.logout);

module.exports = router;
