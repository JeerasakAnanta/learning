import Link from "next/link";

import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "My website",
  description: "Learning Next.js 13 with TypeScript",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <nav className="p-4 bg-gray-800 text-white mb-4 flex gap-4">
          <Link href="/" className="hover:text-blue-300">หน้าแรก</Link>
          <Link href="/about" className="hover:text-blue-300">เกี่ยวกับเรา</Link>
          <Link href="/product/1" className="hover:text-blue-300">สินค้าชิ้นที่ 1</Link>
        </nav>

        {children}

      </body>
    </html>
  );
}
