# SK06_017_Jihanun-Syam-Nafiah

# Penjelasan Program
Program ini dibuat guna mencatat dan menampilkan data nilai mahasiswa. Data disimpan menggunakan file data.json, jadi data yang sudah ditambahkan dapat tersimpan dan digunakan kembali pada saat program dijalankan. Beberapa pilihan menu tersedia di dalam program ini sehingga Dosen bisa memilih menu yang sedang dia butuhkan, yaitu:
   1. Tampilkan data nilai mahasiswa
   2. Menambah data nilai mahasiswa

Dengan adanya program ini Dosen terbantu ketika ingin merekap nilai ujian mahasiswa. Selain itu, program ini dapat membaca riwayat nilai dari file data.json.

# Penjelasan Kode Program
   1. import json = digunakan untuk mengolah dan menyimpan data dalam format json
   2. open("data.json", "r") = untuk membuka file data.json dalam mode membaca
   3. json.load(f) = untuk memgambil dan membaca data dari file json
   4. while True = digunakan agar program terus berjalan dan menu daqpat ditampilkan kembali sampe pengguna memilih keluar.
   5. for mahasiswa in data = digunakan untuk mengambil dan menampilkan data mahasiswa satu per satu
   6. data_baru = {...} = digunakan untuk membuat dictionary yang berisi data mahasiswa baru.
   7. data.append = untuk menambahkan data mahasiswa baru ke dalam list data
   8. open("data.json", "w") = digunakan untuk membukaa file json dalam mode menulis agar data bisa diperbarui
   9. json.dump(data, f, indent=4) = digunakan untuk menyimpan data yang sudah diperbarui ke dalam file data.json


# Screenshot Output Program
<img width="257" height="77" alt="Screenshot 2026-10-07 220656" src="https://github.com/user-attachments/assets/6f39925d-94ec-4dd6-a800-b7481b47d6de" />

Ini merupakan output pertama dimana sistem menampilkan pilihan menuu utama program yang terdiri dari tiga pilihan, yaitu: 

       1. Tampilkan Data Nilai, 
       2. Tambah Data Nilai, dan 
       3. Keluar. 
dan disini sistem meminta Dosen untuk memasukkan pilihan menu nomor berapa yang akan Dosen pilih.


<img width="386" height="230" alt="Screenshot 2026-10-07 233502" src="https://github.com/user-attachments/assets/f6f44c18-4365-400c-9a50-9df3be3538c6" />

Ini output apabila Dosen memilih menu nomor 1 yaitu Tampilkan data nilai mahasiswa. Disini output menampilkan data nilai mahasiswa yang tersimpan di dalam file data.json. setelah itu sistem akan kembali ke menu dan menawarkan Dosen untuk memasukkkan pilihan lagi jika ada.



<img width="319" height="154" alt="Screenshot 2026-10-07 233647" src="https://github.com/user-attachments/assets/541785a1-cd78-4f48-9345-3d895f756cb1" />

Jika memilih menu nomor 2 yakni Tambah data nilai mahasiswa maka Dosen diminta untuk memasukkan Nama, NIM, Mata Kuliah, dan Nilai. Jika sesuai, sistem akan menampilkan DATA BERHASIL DITAMBAHKAN dan dengan begini data tersimpan di dalam file data.json. Sistem juga akan mengarahkan kembali ke menu untuk Dosen memasukkan pilihan menu jika masih ingin menggunakan.



<img width="320" height="100" alt="Screenshot 2026-10-07 233951" src="https://github.com/user-attachments/assets/35d46c2f-1aed-40e4-bfc8-9115687b9907" />

Ini output ketika Dosen telah selesai dan ingin keluar dari sistem Dosen bisa memasukkan pilihan nomor 3 yaitu Keluar. Dengan ini program selesai.



<img width="422" height="236" alt="Screenshot 2026-10-07 234304" src="https://github.com/user-attachments/assets/8281dc8b-ea82-48a6-b016-d4a82b4e1b04" />

Pada output ini menunjukan Dosen yang ingin mengecek sistem lagi apakah data nilai mahasiswa yang tadi Dosen input tersimpan atau tidak jadi Dosen memilih memasukkan menu pilihan 1 Yaitu Tampilkan data nilai mahasiswa. Nah karena tadi data baru telah disimpan di dalam file data.json maka ketika Dosen menutup program lalu ingin dijalankan kembali, data tersebut masih ada dan dapat ditampilkan. Di awal data nilai mahasiswa hanya 3 namun setelah tadi tambah data sekarang menjadi 4 data.
