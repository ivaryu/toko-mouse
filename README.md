# Post-Test 2, CRUD
## Flowchart
![flowchrt](https://github.com/ivaryu/toko-mouse/assets/144821955/fae9ef4c-7c21-4843-bdc7-b0644e8bf2a4)

## Program
Dalam program ini, saya menggunakan function, while loop, percabangan if else elif, dan PrettyTable
### Utama
Bagian utama untuk mengkonfirmasi apakah pengguna masuk sebagai pembeli atau sebagai admin. Jika masuk sebagai pembeli, maka harus memasukkan nama pembeli. Menggunakan percabangan, dan pemanggilan fungsi
![Screenshot 2023-10-10 004948](https://github.com/ivaryu/toko-mouse/assets/144821955/808c6bf7-d67b-43b8-b94c-6ed0f7fdf2c5)

### List Produk
Saya menggunakan list dan PrettyTable (dan library prettytable yang lainnya) untuk membuat daftar produk
![list produk](https://github.com/ivaryu/toko-mouse/assets/144821955/c642fa16-1d5b-471d-b91e-412c09761281)


### Menu Pembeli + Transaksi
Jika berhasil masuk sebagai pembeli, maka akan ditampilkan menu khusus pembeli. Pengguna dapat mengakses menu "Lihat Mouse", "Beli Mouse", dan "Keluar". Program dapat dihentikan dengan mengakses opsi ke tiga atau saat melakukan pembelian, dan tidak ingin melanjutkan pembelian mouse. Menggunakan fungsi agar dapat memudahkan pemrogaman, dan menggunakan loop agar data yang diinput tidak valid, program tidak langsung berhenti.
![menu pembeli](https://github.com/ivaryu/toko-mouse/assets/144821955/5376a4b5-f302-43e1-9205-14cb8b8dd124)

### Menu Admin
Jika berhasil masuk sebagai admin, maka akan ditampilkan menu khusus admin. Admin memiliki wewenang untuk menambah, menampilkan, mengubah, dan menghapus produk/data yang ada. Karena menggunakan whileLoop, saya memberikan opsi keluar agar admin dapat keluar dari program. Di sini saya menggunakan pemanggilan function/fungsi untuk tiap-tiap opsi wewenang admin, kecuali opsi keluar program.
![menu admin](https://github.com/ivaryu/toko-mouse/assets/144821955/ce8fc319-b9e1-4873-a070-f5a01ef61d9c)

### Tambah Data (Create)
Jika memilih opsi 1. Admin dapat menambahkan merk mouse, model mouse, dan harga mouse yang akan ditambahkan di list produk.
![tambah(create)](https://github.com/ivaryu/toko-mouse/assets/144821955/ad15f139-c120-4feb-8f3b-1d07c6f6380f)

### Tampilkan Data (Read)
Jika memilih opsi 2. Admin bisa melihat langsung daftar produk yang ada. Jika daftar produk telah dirubah, admin juga dapat melihatnya di opsi 2 ini.
![tampilkan(read)](https://github.com/ivaryu/toko-mouse/assets/144821955/ed7fdc68-7094-4866-93a0-8d390c6e1252)

### Update Data (Ubah)
Jika memilih opsi 3. Admin dapat mengubah produk yang terdaftar dengan memasukkan kode angka (laci) pada daftar produk untuk mengidentifikasikan produk mana yang ingin dirubah, kemudian admin dapat memasukkan merk mouse, model mouse, dan harga mouse yang baru.
![ubah(update)](https://github.com/ivaryu/toko-mouse/assets/144821955/a7c89263-dc39-4d34-a48c-2e22a278c015)

### Hapus Data (Delete)
Jika Memilih opsi 4. Admin dapat menghapus produk yang terdaftar dengan memasukkan kode angka (laci) pada daftar produk untuk mengidentifikasi produk yang akan dihapus.
![hapus(delete)](https://github.com/ivaryu/toko-mouse/assets/144821955/beb54ce8-a352-458f-9725-8f90cdb4a2c9)

### Keluar (Opsi Tambahan)
Di menu admin. Jika Memilih opsi 5, maka admin akan langsung keluar dari program
![keluar program](https://github.com/ivaryu/toko-mouse/assets/144821955/7584f5d5-7412-4aab-819e-b6340e0901f8)
