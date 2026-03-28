'use client';

import { useState } from 'react';

export default function CounterPage() {
    const [count, setCount] = useState(0);

    return (
        <div className="flex min-h-screen flex-col items-center justify-center gap-4">
            <h1 className="text-4xl font-bold">ตัวนับ: {count}</h1>
            <button
                onClick={() => setCount(count + 1)}
                className="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
            >
                กดเพิ่มเลข +
            </button>
        </div>
    );
}