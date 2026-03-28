import Link from "next/link";

export default function AboutPage() {
  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold">เกี่ยวกับเรา</h1>
      <Link href="/" className="mt-4 text-blue-600  hover:underline">
        กลับไปที่หน้าแรก 🏠
      </Link>

      <p className="mt-4">นี่คือหน้า About ที่สร้างขึ้นด้วย Next.js!</p>
    </div>
  );
}