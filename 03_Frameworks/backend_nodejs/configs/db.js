const mogoose = require("mongoose");

/**
 * Connect to MongoDB database
 *
 * @async
 * @function connectDB
 *
 * @returns {Promise<void>} - Resolves when the connection is established
 */
const connectDB = async () => {
  try {
    const conn = await mogoose.connect(process.env.MONGO_URI);
    console.log(`MongoDB connected: ${conn.connection.host}`);
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
};

module.exports = connectDB;
