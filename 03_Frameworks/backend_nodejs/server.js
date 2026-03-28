require("dotenv").config();
const express = require("express");
const cors = require("cors");
const connectDB = require("./configs/db");

const app = express();
app.use(cors());
app.use(express.json());

// เชื่อมต่อ Database
connectDB();

// Routes
app.use("/api/users", require("./routes/userRoutes"));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
