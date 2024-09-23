// server js 

const express = require('express');
const cors = require('cors');
const port = 8000;

const app = express();
app.use(cors());

app.post('/update',  (req, res)=> {
    res.json({msg: 'Hello World'})
})
app.listen(port, () => {
    console.log(`Server is running on port ${port}`)
})


