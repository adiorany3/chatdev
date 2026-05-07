# Chat Sederhana

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)](https://streamlit.io/)

Aplikasi chat sederhana berbasis Python dan Streamlit. Proyek ini menampilkan riwayat pesan, timestamp real-time, efek typing, dan respons bot acak untuk simulasi interaksi chat.

## ✨ Fitur

- 💾 **Riwayat Chat Tersimpan**: Pesan disimpan di `st.session_state` selama sesi aktif
- ⏱️ **Timestamp Real-time**: Setiap pesan memiliki waktu pengiriman
- ✨ **Efek Typing**: Animasi typing saat bot membalas
- 🎲 **Respons Bot Acak**: Bot memberikan respons acak untuk simulasi interaktif
- 📱 **UI Sederhana**: Antarmuka yang mudah digunakan dengan Streamlit

## 📋 Prerequisites

- Python 3.9 atau lebih baru
- `pip` (biasanya sudah terinstall dengan Python)

## 🚀 Instalasi

1. **Clone atau download** repositori ini ke lokal Anda.

2. **Buat virtual environment** (opsional tapi direkomendasikan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Pada Windows: venv\Scripts\activate
   ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Menjalankan Aplikasi

Dari folder proyek, jalankan perintah berikut:

```bash
streamlit run chat.py
```

Aplikasi akan terbuka di browser default Anda pada `http://localhost:8501`.

## 📁 Struktur Proyek

```
chat/
├── chat.py              # File utama aplikasi Streamlit
├── requirements.txt     # Daftar dependensi Python
└── README.md           # Dokumentasi proyek (file ini)
```

## 🔧 Penggunaan

1. Buka aplikasi di browser.
2. Ketik pesan di kolom input chat.
3. Tekan Enter untuk mengirim pesan.
4. Bot akan memberikan respons dengan efek typing.
5. Riwayat chat akan tersimpan selama sesi aktif.

## 🤝 Contributing

Kontribusi sangat diterima! Silakan:

1. Fork repositori ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.

## ⚠️ Catatan

- Aplikasi ini masih bersifat simulasi dan belum terhubung ke backend AI atau database eksternal.
- Riwayat chat hilang saat aplikasi di-restart.
- Untuk penggunaan produksi, pertimbangkan integrasi dengan database atau API eksternal.

## 📞 Dukungan

Jika Anda memiliki pertanyaan atau masalah, silakan buat issue di repositori ini.