# TASK-REPOSITORY
📘 Deskripsi Proyek (Panjang)
------------
Proyek ini merupakan implementasi Python sederhana namun fungsional yang bertujuan untuk menggabungkan dua konsep penting dalam perhitungan kalender: penentuan tahun kabisat dan penghitungan hari dalam seminggu dari suatu tanggal menggunakan Zeller’s Congruence. Program ini tidak hanya dirancang sebagai alat bantu perhitungan, tetapi juga sebagai sarana edukatif yang menjelaskan secara eksplisit logika yang digunakan dalam menentukan validitas tahun kabisat dan algoritma matematika kalender.

Fitur Utana
---------
- Membuktikan inputan tanggal, bulan dan tahun
- Melacak apakah tahun adalah tahun kabisat
- Mengonversikan tanggal ke hari (Senin-Minggu) menggunakan rumus klasik Zeller
- Validasi input dasar (dapat dikembangkan lebih lanjut)

Logika Program
-------------
1. **Fungsi is_kabisat (tahun)**
   Menunjukan apakah tahun tersebut adalah tahun kabisat:
   - Jika tahun yang habis dibagi 4,
   - jika habis dibagi 100 harus juga habis dibagi 400 -> Jadikan Kabisat
   Contoh:
      2024 -> Tahun Kabisat
      2011 -> Bukan tahun Kabisat
     
  ![image](https://github.com/user-attachments/assets/65c2bbb9-753a-49d2-bd01-9ad674fa7677)

2. **Fungsi numberof_day_in_month (bulan, tahun)**
   Mengembalikan jumlah hari dalam bulan tersebut:
   - Jika bulan adalah Februari (2), maka jumlah harinya adalah 29 atau 28
   - Sedangkan bulan April (4), Juni (6), September (9) dan November (11) jumlah harinya adalah 30
   - Selain yang diatas maka jumlah hari tersebut adalah 31
   
  ![image](https://github.com/user-attachments/assets/fdbde3ec-6770-4517-af4e-7d013a105e28)

3. **Fungsi enter_number**
   Meminta untuk memasukkan angka:
   - Harus berupa angka (int)
   - Harus berada dalam batas minimal dan maksimal
     
  ![image](https://github.com/user-attachments/assets/ef48e14c-8b9c-41e4-99c4-ebb6003c2da9)

4. **Fungsi validate_input()**
   Menerima input tanggal, bulan, dan tahun dari user:
   - Harus memastikan bahwa data yang di input, termasuk tanggal, bulan dan tahun adalah valid.
   - Jika tanggal tersebut melebihi dari jumlah hari pada bulan tertentu maka diminta dari awal sampai valid
     
   ![image](https://github.com/user-attachments/assets/988c3f9e-b993-44d1-8aba-86b19a518a05)

5. **Fungsi zeller_congruence(tanggal, bulan, tahun)**
   Menggunakan algoritma Zeller's Congruence untuk menentukan nama hari dari sebuah tanggal:
   - Algoritma yang mengubah tanggal menjadi indeks hari (0–6), lalu disusun ke nama hari seperti "Senin", "Selasa", dst.
   
