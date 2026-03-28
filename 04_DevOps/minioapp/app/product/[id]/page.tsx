"use client";

export default async function ProductDetail({ params }: { params: { id: string } }) {
    const { id } = await params;
    return (
        <div className="p-10">
            <h1 className="text-4xl font-bold mb-4">หน้ารายละเอียดสินค้า</h1>
            <p className="text-xl">
                คุณกำลังดูสินค้า รหัส: {id}
            </p>
        </div>
    );
}