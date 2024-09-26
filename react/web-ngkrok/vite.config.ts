import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://0.0.0.0:5500/config/
export default defineConfig({
  server: {
    port: 5500,
  },
  plugins: [react()],
})

