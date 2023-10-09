# Toko Gear Gaming dengan program operasi CRUD


import os
os.system('cls')

#Mengimpor/mengambil PrettyTable agar dapat digunakan
from prettytable import PrettyTable

#List dalam PrettyTable
daftarMerekMouse = PrettyTable()
daftarMerekMouse.field_names = ["Laci", "Merk Mouse", "Model Mouse", "Harga"]
daftarMerekMouse.add_row(["0", "Rexus", "Daxa Air 2", "200.000"])
daftarMerekMouse.add_row(["1", "Logitech", "G102", "150.000"])
daftarMerekMouse.add_row(["2", "VortexSeries", "GX107", "250.000"])
daftarMerekMouse.add_row(["3", "Razer", "Viper Mini", "900.000"])

def samaDengan():
    print("========================================================================")

def create():
    nomorTabel = len(daftarMerekMouse.rows)
    namaBarang = input("Masukkan merk mouse baru = ")
    modelMouse = input("Masukkan model mouse baru = ")
    jumlahHarga = input("Masukkan harga barang = ")
    daftarMerekMouse.add_row([nomorTabel, namaBarang, modelMouse, jumlahHarga])
    print("Data telah ditambahkan")
    menuAdmin()

def read():
    print(daftarMerekMouse)
    menuAdmin()

def update():
    print(daftarMerekMouse)
    kodeLama = input("Masukkan NO/Kode Mouse yang ingin diubah = ")
    if int(kodeLama) <= len(daftarMerekMouse.rows):
        daftarMerekMouse.del_row(int(kodeLama)) 
        nomorTabel = len(daftarMerekMouse.rows)
        kodeBaru = input("Masukkan merk mouse baru = ")
        modelMouse = input("Masukkan model mouse baru = ")
        jumlahHarga = input("Masukkan harga barang = ")
        daftarMerekMouse.add_row([nomorTabel, kodeBaru, modelMouse, jumlahHarga])
        print("Data telah ditambahkan")
        menuAdmin()

def delete():
    print(daftarMerekMouse)
    mouseHapus = input("Masukkan NO/Kode mouse yang ingin dihapus = ")
    if int(mouseHapus) <= len(daftarMerekMouse.rows):
        daftarMerekMouse.del_row(int(mouseHapus))
        print(f"Data {mouseHapus} telah dihapus")
        lanjut = input("Ingin melanjutkan? (y/n) = ")
        if lanjut=="y":
            delete()
        else:
            menuAdmin()
    else:
        print(f"Data tidak ditemukan")
        menuAdmin()

def menuAdmin():
    samaDengan()
    print("1. Tambahkan Data")
    print("2. Tampilkan Daftar Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")
    while True:
        pilihmenu = int(input("Masukkan Kode Angka Menu = "))
        if pilihmenu==1:
            create()
            break
        elif pilihmenu==2:
            read()
            break
        elif pilihmenu==3:
            update()
            break
        elif pilihmenu==4:
            delete()
            break
        elif pilihmenu==5:
            print("Program Berakhir")
            break
        else:
            print("Kode Angka tidak terdaftar, coba lagi")

def menuPembeli():
    while True:
        print("Mari dilihat-lihat dulu")
        print("1. Lihat Mouse")
        print("2. Beli Mouse")
        opsi = input("Pilih opsi = ")
        if opsi=="1" or opsi=="lihat mouse":
            print(daftarMerekMouse)
        elif opsi=="2" or opsi=="Beli mouse":
            print(daftarMerekMouse)
            pesanMouse = input("Masukkan Kode Angka Mouse = ") 
            if int(pesanMouse) <= len(daftarMerekMouse.rows):
                daftarMerekMouse.del_row(int(pesanMouse))
                lanjut = input("Mau Beli lagi? (y/n) ")
                if lanjut == "n" :
                    break #Perintah operasi pemrogaman berhenti

def login():
    print("Login Terlebih Dahulu")
    samaDengan()
    while True:
        username = ("Faisal")
        password1 = ("faisal12345")
        usn2 = ("fr")
        pw2 = ("fr")
        usernameid = str(input("Username = "))
        password = input("Password = ")
        if usernameid==username and password==password1:
            print("Login berhasil")
            menuAdmin()
            break
        elif usernameid==usn2 and password==pw2:
            print("Login berhasil")
            menuAdmin()
            break
        else:
            samaDengan()
            print("Data tidak terdaftar")

def role():
    loginKan = str(input("Masuk sebagai pembeli/admin = "))
    if loginKan=="pembeli":
        namaPembeli = input("Nama = ")
        print(f"Selamat datang {namaPembeli} di Gaming Gear Shop!")
        menuPembeli()
    elif loginKan=="admin":
        login()        

role()