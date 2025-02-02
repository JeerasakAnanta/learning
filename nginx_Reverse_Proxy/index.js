const express = require("express");
const app = express();
const port = 3000;
const os = require("os");

app.get("/", (req, res) => {
  res.json({ message: "response from host: " + os.hostname() });
});

app.listen(port, () => {
  console.log(`Sample API listening at http://localhost:${port}`);
});
