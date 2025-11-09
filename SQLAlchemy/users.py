from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped       # ใช้สำหรับบอก Type ของคอลัมน์
from sqlalchemy.orm import mapped_column  # ใช้สำหรับกำหนดรายละเอียดคอลัมน์
from sqlalchemy import String, Integer    # ใช้สำหรับกำหนดชนิดข้อมูล (เหมือน VARCHAR, INT)
from sqlalchemy import create_engine


# Load environment
from  config.setting import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# Database config postgres
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create engine for database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 2. สร้าง "กระดานหลัก" (Base)
class Base(DeclarativeBase):
    pass

# 3. สร้างโมเดล (แบบแปลน) สำหรับตาราง 'users'
class User(Base):
    # 👈 นี่คือชื่อตารางใน PostgreSQL
    __tablename__ = "users" 

    # --- กำหนดคอลัมน์ต่างๆ ---
    # สร้างคอลัมน์ id เป็น Primary Key
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # สร้างคอลัมน์ name เป็นตัวอักษร (VARCHAR 50)
    name: Mapped[str] = mapped_column(String(50))
    
    # สร้างคอลัมน์ email (VARCHAR 100) และห้ามซ้ำ (unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)

    # (อันนี้เป็นท่าเทคนิค) เพิ่ม method นี้เพื่อให้เวลา print object User จะได้อ่านง่ายๆ
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

print("สร้างโมเดล User (แบบแปลน) เรียบร้อยแล้ว!")

# --- 3. สั่งสร้างตาราง ---
print("กำลังส่งคำสั่ง CREATE TABLE ไปยัง PostgreSQL...")
Base.metadata.create_all(engine)

print("สร้างตาราง users เรียบร้อยแล้ว!")
