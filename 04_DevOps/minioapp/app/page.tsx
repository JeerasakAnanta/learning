import Link from "next/link";

// about  home page 
export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <h1 className="text-4xl font-bold text-black "> welcome </h1>
        <Link href="/about" className="mt-4 text-blue-600 hover:underline">
          ไปอ่านเกี่ยวกับเรา 👉
        </Link>
        <Link href="/counter" className="mt-4 text-blue-600 hover:underline">
          ไปที่หน้าเคาน์เตอร์ 👉
        </Link>

        <div>
          <button> click me </button>
        </div>
      </main >
    </div >
  );
}
