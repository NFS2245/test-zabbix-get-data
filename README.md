# Proyek Pengolahan Data Excel dengan Tkinter

Proyek ini adalah aplikasi berbasis Python yang digunakan untuk memproses data dari file teks dan menghasilkan file Excel dengan menambahkan border pada setiap sel serta menyesuaikan ukuran kolom sesuai dengan panjang data. Aplikasi ini dilengkapi dengan antarmuka pengguna menggunakan `Tkinter`.

## Fitur Utama

- Memproses data dari file teks (`.txt`).
- Mengambil data dari URL dan menyimpan hasilnya ke dalam file Excel.
- Menambahkan border di setiap sel Excel.
- Menyesuaikan lebar kolom di Excel sesuai dengan panjang data.
- Antarmuka pengguna berbasis `Tkinter` untuk memilih file input dan folder output.
- Menyediakan log output di antarmuka pengguna.

## Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda telah menginstal semua dependensi berikut:

- Python 3.x
- Internet connection untuk mengakses URL data.

## Instalasi

1. **Clone repositori ini:**

    ```bash
    git clone https://github.com/username/proyek-pengolahan-data.git
    ```

2. **Masuk ke direktori proyek:**

    ```bash
    cd proyek-pengolahan-data
    ```

3. **Buat dan aktifkan virtual environment (opsional):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/macOS
    venv\Scripts\activate  # Untuk Windows
    ```

4. **Instal dependensi:**

    Pastikan Anda memiliki file `requirements.txt` yang berisi daftar paket yang diperlukan. Instal semua dependensi dengan menjalankan:

    ```bash
    pip install -r requirements.txt
    ```

    **requirements.txt** yang digunakan dalam proyek ini meliputi:

    ```
    pandas
    requests
    openpyxl
    ttkbootstrap
    ```

## Penggunaan

1. **Jalankan aplikasi:**

    Untuk menjalankan aplikasi, cukup jalankan script utama (`main.py`) setelah semua dependensi terinstal:

    ```bash
    python main.py
    ```

2. **Pilih file input:**

    Klik tombol **Browse** di antarmuka pengguna untuk memilih file teks yang berisi data yang akan diproses.

3. **Pilih folder output:**

    Pilih folder tempat file Excel output akan disimpan.

4. **Klik **Run** untuk memulai proses:**

    Setelah memilih file input dan folder output, klik tombol **Run** untuk memulai pemrosesan data.

5. **Cek log output dan hasil:**

    Log output akan ditampilkan di antarmuka pengguna, dan setelah proses selesai, file Excel yang dihasilkan akan disimpan di folder yang dipilih.

## Penanganan Kesalahan

- Jika koneksi internet tidak tersedia, aplikasi akan menampilkan pesan kesalahan.
- Jika file input atau folder output tidak dipilih, aplikasi akan memberi tahu pengguna untuk melengkapinya.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka isu jika ada bug atau saran perbaikan.


Proyek ini dibuat oleh [Nafis](https://github.com/NFS2245).
