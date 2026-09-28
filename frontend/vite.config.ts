import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],

  server: {
    port: 5173,
  },

  preview: {
    host: '0.0.0.0',
    allowedHosts: ['chronoguard-2.onrender.com'],
  },
})
