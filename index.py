import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

while True:
    print("\n" + "="*45)
    print("SISTEM PENCATATAN NILAI MAHASISWA")
    print("="*45)
    print("1. Tampilkan Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih nomor menu: ")

    if pilihan == "1":
        print("\n========== DATA NILAI MAHASISWA ==========")
        for mahasiswa in data:
            print("Nama :", mahasiswa["nama"])
            print("NIM :", mahasiswa["nim"])
            print("Mata Kuliah :", mahasiswa["mata_kuliah"])
            print("Nilai :", mahasiswa["nilai"])
            print("-"*45)

    elif pilihan == "2":
        print("\n========== TAMBAH DATA NILAI ==========")
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM: ")
        mata_kuliah = input("Masukkan mata kuliah: ")
        nilai = int(input("Masukkan nilai: "))

        data_baru = {
            "nama": nama,
            "nim": nim,
            "mata_kuliah": mata_kuliah,
            "nilai": nilai
        }

        data.append(data_baru)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("\nDATA BERHASIL DITAMBAHKAN")

    elif pilihan == "3":
        print("\nSISTEM SELESAI. Terima Kasih")
        break

    else:
        print("\nMohon maaf. Pilihan tidak tersedia")