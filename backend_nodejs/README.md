/my-node-backend
│── /node_modules         # โฟลเดอร์เก็บ dependencies (อัตโนมัติ)
│── /config               # เก็บการตั้งค่าต่างๆ เช่น การเชื่อมต่อ Database
│    ├── db.js            # ตั้งค่าการเชื่อมต่อ MongoDB หรือ Database อื่นๆ
│── /controllers          # จัดการ logic ของ API
│    ├── userController.js
│── /models               # เก็บ Schema ของ Database
│    ├── userModel.js
│── /routes               # เก็บเส้นทาง API (Route)
│    ├── userRoutes.js
│── /middlewares          # เก็บ middleware เช่น auth, error handler
│    ├── authMiddleware.js
│── /utils                # เก็บฟังก์ชันที่ใช้ซ้ำ
│    ├── generateToken.js
│── /public               # เก็บไฟล์ static เช่น รูปภาพ
│── /uploads              # เก็บไฟล์ที่อัปโหลด (เช่น ภาพโปรไฟล์)
│── .env                  # เก็บตัวแปรแวดล้อม (Environment Variables)
│── .gitignore            # ไฟล์บอก Git ว่าห้าม push อะไร
│── package.json          # รายละเอียดของโปรเจ็กต์และ dependencies
│── server.js             # จุดเริ่มต้นของเซิร์ฟเวอร์

docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo
