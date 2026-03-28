const db = require('../configs/db');

exports.login = (req, res) => {
    const { username, password } = req.body;
    const query = 'SELECT * FROM users WHERE username = ? AND password = ?';
    
    db.query(query, [username, password], (err, results) => {
        if (err) throw err;
        
        if (results.length > 0) {
            req.session.loggedin = true;
            req.session.username = username;
            res.redirect('/dashboard'); // เปลี่ยนเส้นทางเมื่อเข้าสู่ระบบสำเร็จ
        } else {
            res.send('Incorrect Username and/or Password!');
        }
    });
};

exports.logout = (req, res) => {
    req.session.loggedin = false;
    req.session.username = null;
    res.send('You have logged out.');
};