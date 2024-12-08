# Data Processing Application

Aplikasi ini dirancang untuk memproses data dari file teks input dan menghasilkan file Excel yang berisi informasi yang diambil dari URL tertentu. Setiap data yang diambil akan memiliki border di setiap sel, dan lebar kolom disesuaikan dengan panjang data.

## Fitur

- **Memproses Data dari File Teks**: Mengambil data dari file teks yang berisi daftar parameter, dan melakukan permintaan HTTP untuk mengambil tabel dari URL.
- **Penyimpanan Hasil**: Data yang diambil akan disimpan dalam file Excel yang diberi format dan border pada setiap sel.
- **Pengaturan Log**: Menyediakan log yang bisa dipantau di antarmuka aplikasi untuk membantu debugging dan memantau proses.
- **Indikator Progres**: Memiliki progress bar untuk menunjukkan status proses yang sedang berlangsung.
- **Tampilan Antarmuka Pengguna (UI)**: Menggunakan `tkinter` untuk membangun antarmuka pengguna yang intuitif dan mudah digunakan.

## Instalasi

### Prasyarat

1. **Python 3.x**: Pastikan Anda sudah menginstal Python versi 3.6 atau lebih tinggi.
2. **Paket yang Dibutuhkan**: Anda perlu menginstal beberapa dependensi untuk menjalankan aplikasi ini. Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal atau command prompt:

    ```bash
    pip install -r requirements.txt
    ```

   **requirements.txt**:


Proyek ini dibuat oleh [Nafis](https://github.com/NFS2245).
