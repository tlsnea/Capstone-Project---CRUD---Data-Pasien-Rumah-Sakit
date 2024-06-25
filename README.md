# Capstone-Project-
# __CRUD - Data Pasien Rumah Sakit__
##### Capstone Project Modul 1 Purwadhika Job Connector Data Science (JCDS-0408)
---
## __Context__
Projek ini merupakan implementasi `CRUD dalam Aplikasi Database Pasien Rumah Sakit di Python`. Program ini dapat membantu menampilkan data pasien, memasukkan data pasien baru, mengubah data pasien yang sudah ada, dan menghapus data pasien. Tujuan dari program ini adalah untuk membantu pekerja di bidang kesehatan, seperti staff di rumah sakit untuk dapat mengatur data pasien sesuai dengan ketentuan yang berlaku.

## __Business Task__
#### Key Features
- ___Read___: 
-- Menampilkan tabel data pasien secara keseluruhan.
-- Menampilkan data pasien tertentu dengan menginput `Nomor Rekam Medis` pasien sebagai _primary key_.
- ___Create___: 
-- Menambahkan data pasien baru ke dalam daftar yang sudah ada dengan masukkan detail data: Nomor Rekam Medis, Nama Lengkap, Tanggal Lahir, Jenis Kelamin, Asuransi, Jenis Perawatan, dan Proses.
-- Memeriksa  `Nomor Rekam Medis` yang diinput merupakan data unik atau bukan duplikat.
-- Menampilkan seluruh pasien yang sudah dihapus dari tabel data pasien.
- ___Update___: Mengubah informasi pasien dalam data pasien yang sudah ada di tabel pasien dengan menginput `Nomor Rekam Medis` pasien yang dipilih.
- ___Delete___:
-- Menghapus data pasien tertentu dengan menginput  `Nomor Rekam Medis` pasien yang ingin dihapus.
-- Menghapus seluruh data pasien yang dikategorikan "Selesai" atau sudah menyelesaikan pengobatan.

#### Objectives
- Menyediakan aplikasi yang memudahkan pengguna dalam proses ```manajemen data``` pasien.
- Mempermudah pengguna untuk melakukan _```tracking```_ terhadap proses pengobatan pasien.
- Membantu pengguna melengkapi maupun ```memperbaharui data``` pasien sesuai dengan ketentuan yang berlaku.

## __Stakeholders__
- __Tenaga Kesehatan__: Staff yang terlibat dalam proses pengobatan pasien dan bertanggung jawab dalam mencatat proses pengobatan pasien.
- __Pasien__: Individu yang datanya dicatat dan dikelola rumah sakit terkait.
- ___Developer___: Tim yang bertanggung jawab dalam mengembangkan, memelihara dan memperbaharui aplikasi seiring waktu.
- __Administrasi Rumah Sakit__: Pengawas berjalannya pencatatan serta proses pengobatan di rumah sakit.

## __Limitations__
Projek ini memiliki kekurangan sebagai berikut:
- Data tidak dapat diinput secara otomatis. Input data perlu dilakukan secara manual, satu per satu dengan mengikuti aturan yang sudah ditetapkan aplikasi.
- Kolom atau detail data yang ada merupakan informasi general. Oleh karena itu, kolom pada tabel dapat dikembangkan lagi sesuai dengan kebutuhan.
- Aplikasi ini dirancang untuk staff atau orang yang bertanggung jawab akan data pribadi pasien rumah sakit, sehingga hanya dapat diakses oleh pihak tertentu saja atau tidak terbuka untuk umum.

## Data Description
Berikut deskripsi data yang dapat diinput dalam program ini.
|No.| Detail Data | Jumlah Karakter |Jenis Data |
|----|----|----|----|
|1|Nomor Rekam Medis|  >3 karakter | String, alphanumerik
2|Nama Lengkap| >3 karakter | String, alpha
3|Tanggal Lahir| 2 digit angka (0<x<32) | Integer
||Bulan Lahir| 2 digit angka (0<x<13) | Integer
||Tahun Lahir| 4 digit angka| Integer
4| Jenis Kelamin| 1 karakter (P/L) | String
5| Asuransi| 1 karakter (input pilihan [1-2]) | String 
6|Jenis Perawatan|1 karakter (input pilihan [1-2]) | String 
7| Proses|1 karakter (input pilihan [1-2]) | String 

#### Note
Data yang digunakan dalam projek ini merupakan data fiktif.

## Contact
<jasa.anastasia@gmail.com>




