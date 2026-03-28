from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# 1. (สมมติว่า) สร้าง Engine เชื่อมต่อกับฐานข้อมูล SQLite ในหน่วยความจำ
engine = create_engine("sqlite:///:memory:")

# 2. สร้าง Base Class
class Base(DeclarativeBase):
    pass

# 3. สร้าง Model (แมปกับตาราง 'users')
class User(Base):
    __tablename__ = "users" # ชื่อตาราง
    
    # กำหนดคอลัมน์
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str | None] # คอลัมน์ที่อาจเป็นค่าว่าง (None)

# 4. สร้างตารางทั้งหมดที่สืบทอดจาก Base
Base.metadata.create_all(engine)

# 5. ใช้ Session เพื่อเพิ่มและค้นหาข้อมูล
with Session(engine) as session:
    
    # เพิ่มข้อมูล (Create)
    user1 = User(username="gemini", email="gemini@example.com")
    session.add(user1)
    # ยืนยันการบันทึก
    session.commit() 

    # ค้นหาข้อมูล (Read)
    stmt = select(User).where(User.username == "gemini")
    found_user = session.scalars(stmt).first()
    
    if found_user:
        print(f"เจอผู้ใช้: {found_user.username} (Email: {found_user.email})")
        
        
