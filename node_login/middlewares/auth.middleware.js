function authenticate(req, res, next) {
  // implement you rs authentication logic here
  if (!req.headers.authorization) {
    return res.status(401).json({ error: "Authorization header is required" });
  }

  next();
}

module.exports = {
  authenticate,
};
