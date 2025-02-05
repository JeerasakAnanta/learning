const express = require("express");
const server = express();
const os = require("os");

count = 0;
server.get("/", (req, res) => {
  count++;
  res.send(`Hello World! response from ${os.hostname()}  =  ${count}\n`);
});

server.listen(3000, () => console.log("Server is running on port 3000"));
