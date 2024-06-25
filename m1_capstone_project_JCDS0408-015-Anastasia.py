# Data Pasien merupakan dictionary dalam list. Karena sebagai list dapat disimpan bersana key dan values, 
# serta list dapat diubah/mutable
dataPasien = [
    {'Nomor Rekam Medis' : 'A122', 'Nama Lengkap' : 'Bang Chan', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 1, 'Bulan' : 1, 'Tahun' : 1997}, 'Asuransi' : 'Swasta', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Rekam Medis' : 'A223', 'Nama Lengkap' : 'Ningning Sasya', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 2, 'Bulan' : 3, 'Tahun' : 2000}, 'Asuransi' : 'BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Rekam Medis' : 'A334', 'Nama Lengkap' : 'Karina Sumina', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 12, 'Bulan' : 12, 'Tahun' : 2012}, 'Asuransi' : 'BPJS', 'Perawatan' : 'Rawat Jalan', 'Proses' : 'Selesai' },
    {'Nomor Rekam Medis' : 'A445', 'Nama Lengkap' : 'Justine Biner', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 30, 'Bulan' : 10, 'Tahun' : 1990}, 'Asuransi' : 'Swasta', 'Perawatan' : 'Rawat Jalan', 'Proses' : 'Selesai' }
]

# Penyusunan tabel dataPasien
# 1. Mengubah format tanggal lahir menjadi dd-mm-yyyy
def penulisanTanggalLahir(tanggalLahir):
    return f"{tanggalLahir['Tanggal']:02d}-{tanggalLahir['Bulan']:02d}-{tanggalLahir['Tahun']:04d}"
#2. Membuat tabelPasien
def tabelPasien(q):
    judulTabel = ['Nomor Rekam Medis', 'Nama Lengkap','Jenis Kelamin', 'Tanggal Lahir', 'Asuransi', 'Perawatan', 'Proses' ]
    print('{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|'.format(*judulTabel))
    print('-'*147)
    for pasien in q:
        baris = [
            pasien['Nomor Rekam Medis'],
            pasien['Nama Lengkap'],
            pasien['Jenis Kelamin'],
            str(penulisanTanggalLahir(pasien['Tanggal Lahir'])),
            pasien['Asuransi'],
            pasien['Perawatan'],
            pasien['Proses']
        ]
        print('{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|'.format(*baris))
#==================================================================================================================================
# Konfirmasi Periksa Perubahan
def simpanPerubahan():
    while True: 
        konfirmasi = input('Simpan perubahan? (Y/N): ')
        if konfirmasi.upper() == 'Y':
            return True
        elif konfirmasi.upper() == 'N':
            return False
        else:
            continue        
def diubah():
    while True: 
        konfirmasi = input('Lakukan perubahan? (Y/N): ')
        if konfirmasi.upper() == 'Y':
            return True
        elif konfirmasi.upper() == 'N':
            return False
        else:
            continue        

# Periksa duplikat unique key
def nrm(nomorRm):
    global dataPasien
    for pasien in dataPasien:
        if pasien['Nomor Rekam Medis'] == nomorRm.upper():
            return True
    else:
        return False
    
# Cari pasien berdasarkan nomor unik
def pasien(nomorRm):
    for pasien in dataPasien:
        if pasien['Nomor Rekam Medis'] == nomorRm.upper():
            return pasien
        
#==================================================================================================================================
# Menu Utama
def menuUtama():
    print(
        '''\n==================Database Pasien Rumah Sakit XYZ==================\n''')
    print('''
    1. Lihat Daftar Pasien
    2. Tambahkan Data Pasien Baru
    3. Ubah Informasi Pasien
    4. Hapus Data Pasien
    5. Keluar dari Program
    ''')
#==================================================================================================================================

# Menu 1
def menu1():
    print(
        ''' ==================Lihat Daftar Pasien==================''')
    print('''
    1. Tampilkan Seluruh Data
    2. Tampilkan Data Pasien Tertentu
    3. Tampilkan Data Pasien yang Dihapus
    4. Kembali ke Menu Utama
   ''')
#==================================================================================================================================
# Menu 2
dataBaru = {}
def menu2():
    print('''\n==================Tambah Data Pasien Baru==================\n''')
    print('''\n1. Tambahkan Data Pasien Baru\n2. Kembali ke Menu Utama\n''')

# 2.1 Menu tambah pasien
def tambahPasien():
    global dataPasien
    global dataBaru 
    if inputNoBaru(dataBaru) == True:
        kelengkapanDataPasienBaru()
        if simpanPerubahan() == True:
            dataPasien.append(dataBaru)
            print('***Data Tersimpan***')   
    return dataBaru, dataPasien

# 2.2 Menu input data pasien baru
def kelengkapanDataPasienBaru():
    global dataPasien
    global dataBaru
    inputNama(dataBaru)
    inputJk(dataBaru)
    tglLahir()
    inputAsuransi(dataBaru)
    inputPerawatan(dataBaru)
    inputProses(dataBaru)
    tabelPasien([dataBaru])
    return dataBaru
#==================================================================================================================================
# Fungsi-fungsi untuk Input Data Pasien
def inputNoBaru(dataBaru):
    while True:
        nomorRm = input('Masukkan Nomor Rekam Medis Pasien: ')              #Input Nomor Rekam Medis
        if nrm(nomorRm) == True:                                            #periksa duplikat
            tabelPasien([pasien(nomorRm)])
            print('\n***Pasien sudah terdaftar***')
            return False
        if len(nomorRm) < 4 or not nomorRm.isalnum():                       # Periksa format unique key
            print('***** Nomor Rekam Medis Harus terdiri dari Huruf dan angka minimal 4 karakter *****')
            break
        else:
            dataBaru['Nomor Rekam Medis'] = nomorRm.upper() 
            return True

def inputNama(dataBaru):
    while True:
        namaLengkap = input('Masukkan Nama Lengkap Pasien: ')
        if namaLengkap.isalpha and len(namaLengkap) > 3:                    # Periksa penulisan nama
            dataBaru['Nama Lengkap'] = namaLengkap.title()
            break
        else:
            print('***Input Nama Lengkap dengan Benar!***')

def inputJk(dataBaru):
    while True:
        jenisKelamin = input('Masukkan Jenis Kelamin Pasien (P/L): ')
        if jenisKelamin.upper() == 'P' or jenisKelamin.upper() == 'L':      # Periksa input jenis kelamin
            dataBaru['Jenis Kelamin'] = jenisKelamin.upper()
            break
        else:
            print('''\n*****Masukkan jenis kelamin dengan benar!*****''')

def inputAsuransi(dataBaru):
    while True:
        asuransi = input(f'''{'-'*50}\nKode Shortcut\n1. Swasta\t 2. BPJS \t 3. Tidak Ada (-)\nMasukkan Jenis Asuransi Pasien [1-2]: ''')                   
        if asuransi == '1':
            asuransi = 'Swasta'
            break
        elif asuransi == '2':
            asuransi = 'BPJS'
            break
        elif asuransi == '3' or asuransi == '-':
            asuransi = '-'
            break
        else:
            print('*** Masukkan salah satu dari pilihan! ***')                  # Input harus sesuai opsi
    dataBaru['Asuransi'] = asuransi
    
def inputPerawatan(dataBaru):
    while True:
        perawatan = input(f'''{'-'*50}\nKode Shortcut\n1. Rawat Inap\t 2. Rawat Jalan\nMasukkan Jenis Perawatan Pasien [1-2]: ''')
        if perawatan == '1':
            perawatan = 'Rawat Inap'
            break
        elif perawatan == '2':
            perawatan = 'Rawat Jalan'
            break
        else:
            print('*** Masukkan salah satu dari pilihan! ***')                  # Input harus sesuai opsi
    dataBaru['Perawatan'] = perawatan
    
def inputProses(dataBaru):
    while True:
        proses = input(f'''{'-'*50}\nKode Shortcut\n1. Sedang Berjalan\t 2. Selesai\nProses Pengobatan Pasien [1-2]: ''')
        if proses == '1':
            proses = 'Sedang Berjalan'
            break
        elif proses == '2':
            proses = 'Selesai'
            break
        else:
            print('*** Masukkan salah satu dari pilihan! ***')                  # Input harus sesuai opsi
    dataBaru['Proses'] = proses
    

#2.2.1 Khusus tanggal lahir
def tglLahir():
    print('\nMasukkan Tanggal, Bulan, dan Tahun Lahir Pasien')
    global dataBaru
    dataBaru['Tanggal Lahir']={'Tanggal':'','Bulan':'','Tahun':''}              # Input tanggal lahir 
    inputTglLahir(dataBaru)

def inputTglLahir(dataBaru):
    while True:
        try:
            tanggalLahir = int(input('1. Tanggal (maksimal 2 digit angka): '))
            if tanggalLahir <= 31 and tanggalLahir > 0:
                dataBaru['Tanggal Lahir']['Tanggal'] = tanggalLahir
                break
            else:
                print('''\n*****Masukkan tanggal dengan benar!*****\n''')

        except ValueError:                                                      # Input harus sesuai format yang ditentukan
            print('''\n*****Masukkan Maksimal 2 digit angka*****\n''')

    while True:   
        try:
            bulanLahir = int(input('2. Bulan (maksimal 2 digit angka): '))
            if bulanLahir <= 12 and bulanLahir > 0:
                dataBaru['Tanggal Lahir']['Bulan'] = bulanLahir
                break
            else:
                print(''''\n*****Masukkan bulan dengan benar!*****\n''')
        except ValueError:
            print('''\n*****Masukkan Maksimal 2 digit angka*****\n''')

    while True:           
        try:
            tahunLahir = int(input('3. Tahun (masukkan 4 digit angka): '))
            if tahunLahir <= 2024 and tahunLahir > 1900:
                dataBaru['Tanggal Lahir']['Tahun'] = tahunLahir
                break
            else:
                print('''\n*****Masukkan tahun dengan benar!*****\n''')
        except ValueError:
            print('''\n*****Masukkan Maksimal 4 digit angka!*****\n''')

    return dataBaru, tanggalLahir, bulanLahir, tanggalLahir
#==================================================================================================================================

# Menu 3
def menu3():
    print(
        '''\n==================Ubah Data Pasien==================\n''')
    print('''\n1. Ubah Data Pasien \n2. Kembali ke Menu Utama\n''')

# 3.1 Fungsi Ubah Data Pasien
dataUpdate={}
def ubahDataPasien(nomorRm):
    global dataPasien
    if nrm(nomorRm) == True:
        tabelPasien([pasien(nomorRm)])              # memunculkan tabel pasien sesuai input primary key
        if diubah() == True:
            kolomUpdate(pasien(nomorRm))
    else:
        print('*****Data Tidak Ada*****')
    return pasien
# 3.1.2 Pilih Kolom Update 
def kolomUpdate(pasien):
    kolom = (input(f'''{'-'*50}\nInput Kolom yang di-Update: ''')).title()
    keyDitemukan = False
    for key, values in pasien.items():
        if key == kolom:
            keyDitemukan = True
            if key == 'Nama Lengkap':
                namaUpdate(pasien)
            elif key == 'Nomor Rekam Medis':
                nrmUpdate(pasien)
            elif key == 'Jenis Kelamin':
                jkUpdate(pasien)
            elif key == 'Tanggal Lahir':
                tlUpdate(pasien)
            elif key == 'Asuransi':
                asuransiUpdate(pasien)
            elif key == 'Perawatan':
                perawatanUpdate(pasien)
            elif key == 'Proses':
                prosesUpdate(pasien)
    if not keyDitemukan:
        print('Kolom Tidak Ada')
    return dataPasien
#  Fungsi-fungsi untuk update data pasien sesuai kolom terpilih    
def nrmUpdate(pasien):
    print('\n----- Update Nomor Rekam Medis Pasien -----\n')
    while inputNoBaru(dataUpdate) != True:                                  # Menambahkan fungsi dari menu 2 (input)
        continue
    if simpanPerubahan() == True:
        pasien['Nomor Rekam Medis'] = dataUpdate['Nomor Rekam Medis']
        print('\nData Telah Di-Update\n')
    return dataPasien

def namaUpdate(pasien):
    print('\n----- Update Nama Pasien -----\n')
    inputNama(dataUpdate)
    if simpanPerubahan() == True:
        pasien['Nama Lengkap'] = dataUpdate['Nama Lengkap']
        print('\nData Telah Di-Update\n')      
    return dataPasien

def jkUpdate(pasien):
    print('\n----- Update Jenis Kelamin Pasien -----\n')
    inputJk(dataUpdate)
    if simpanPerubahan() == True:
        pasien['Jenis Kelamin'] = dataUpdate['Jenis Kelamin']
        print('\nData Telah Di-Update\n')     
    return dataPasien

def tlUpdate(pasien):
    print('\n----- Update Tanggal Lahir Pasien -----\n')
    dataUpdate['Tanggal Lahir']={'Tanggal':'','Bulan':'','Tahun':''}
    inputTglLahir(dataUpdate)
    if simpanPerubahan() == True:
        pasien['Tanggal Lahir']['Tanggal'] = dataUpdate['Tanggal Lahir']['Tanggal']
        pasien['Tanggal Lahir']['Bulan'] =  dataUpdate['Tanggal Lahir']['Bulan']
        pasien['Tanggal Lahir']['Tahun'] =  dataUpdate['Tanggal Lahir']['Tahun']
        print('Data Telah Di-Update')      
    return dataPasien

def asuransiUpdate(pasien):
    print('\n----- Update Asuransi Pasien -----\n')
    inputAsuransi(dataUpdate)
    if simpanPerubahan() == True:
        pasien['Asuransi'] = dataUpdate['Asuransi']
        print('\nData Telah Di-Update\n')      
    return dataPasien

def perawatanUpdate(pasien):
    print('\n----- Update Jenis Perawatan Pasien -----\n')
    inputPerawatan(dataUpdate)
    if simpanPerubahan() == True:
        pasien['Perawatan'] = dataUpdate['Perawatan']
        print('\nData Telah Di-Update\n')      
    return dataPasien

def prosesUpdate(pasien):
    print('\n----- Update Proses Pengobatan Pasien -----\n')
    inputProses(dataUpdate)
    if simpanPerubahan() == True:
        pasien['Proses'] = dataUpdate['Proses']
        print('Data Telah Di-Update')  
    return dataPasien
    
#==================================================================================================================================
# Menu 4
dataPasienDihapus = []
pasienSelesai = []
def menu4():
    print(
        ''' ==================Hapus Data Pasien==================\n''')
    print('''
    1. Hapus Data Pasien Tertentu
    2. Hapus Pasien yang Selesai Berobat
    3. Kembali ke Menu Utama
    ''')

# 4.1 Fungsi Hapus Pasien Tertentu
dataPasienDihapus = []
def hapusPasien(nomorRm):
    global dataPasienDihapus
    global dataPasien
    if nrm(nomorRm) == True:
        tabelPasien([pasien(nomorRm)])
        if simpanPerubahan() == True:
            dataPasienDihapus.append(pasien(nomorRm))
            dataPasien.remove(pasien(nomorRm))
            print('Data Telah Dihapus')    
    else:
        print('Pasien Tidak Terdaftar')
    return dataPasienDihapus, dataPasien

# 4.3 Hapus berdasarkan kategori
def hapusPasienKategori():
    global dataPasienDihapus
    global pasienSelesai
    global dataPasien
    dataDitemukan = False
    for pasien in dataPasien:
        if pasien['Proses'] == 'Selesai':
            pasienSelesai.append(pasien)
            dataDitemukan = True
    if dataDitemukan == True:
        tabelPasien(pasienSelesai)
        if simpanPerubahan() == True:
            for pasien in pasienSelesai:
                dataPasienDihapus.append(pasien)
                dataPasien.remove(pasien)
            print('Data Telah Dihapus')
        pasienSelesai.clear()
    if not dataDitemukan:
        print('Tidak Ada Pasien Selesai')     

#==================================================================================================================================
# Konsep besar
while True:
    menuUtama()
    pilihanMenu = input('Silahkan Pilih Menu [1-5]: ')

# MENU 1: MENAMPILKAN DATA (READ)
    if pilihanMenu == '1':
        while True:                  
            menu1()
            pilihamMenu1 = input('Silahkan Pilih Menu [1-4]: ') 
            if pilihamMenu1 == '1':
                if len(dataPasien) > 0: 
                    tabelPasien(dataPasien)               
                else:
                    print('*** Data Tidak Ada ***')
            elif pilihamMenu1 == '2':                               
                nomorRm = (input('Masukkan Nomor Rekam Medis: ')).capitalize()
                if nrm(nomorRm) == True:
                    tabelPasien([pasien(nomorRm)])
                elif nrm(nomorRm) == False:
                    print('*** Data Tidak Ada ***')
            elif pilihamMenu1 =='3':
                if len(dataPasienDihapus) > 0:
                    tabelPasien(dataPasienDihapus)
                else:
                    print('*** Data Tidak Ada ***')
            elif pilihamMenu1 == '4':
                break
            else:
                print('*****Inputan salah. Masukkan sesuai opsi!*****\n')
        
# MENU 2: MENAMBAHKAN DATA (CREATE)
    elif pilihanMenu == '2':
        while True:
            menu2()
            pilihanMenu2 = input('Silakan Pilih Menu [1-2]: ')
            if pilihanMenu2 == '1':
                dataBaru ={}
                tambahPasien()
            elif pilihanMenu2 == '2':
                break          
            else:
                print('*****Inputan salah. Masukkan sesuai opsi!*****\n')

# MENU 3: UPDATE DATA (UPDATE)
    elif pilihanMenu == '3':
        while True:
            menu3()
            pilihanMenu3 = input('Silakan Pilih Menu [1-2]: ')
            if pilihanMenu3 == '1':
                nomorRm = (input('Masukkan Nomor Rekam Medis: ')).capitalize()
                ubahDataPasien(nomorRm)
            elif pilihanMenu3 =='2':
                break
            else:
                print('*****Inputan salah. Masukkan sesuai opsi!*****\n')
            
# MENU 4: HAPUS DATA (DELETE)
    elif pilihanMenu == '4':
        while True:
            menu4()
            pilihanMenu4 = input('Silakan Pilih Menu [1-3]: ')
            if pilihanMenu4 == '1':
                nomorRm = (input('Masukkan Nomor Rekam Medis: ')).capitalize()
                hapusPasien(nomorRm) 
            elif pilihanMenu4 == '2':
                print('Hapus Pasien Selesai Pengobatan')
                hapusPasienKategori()        
            elif pilihanMenu4 == '3':
                break
            else:
                print('*****Inputan salah. Masukkan inputan yang benar!*****\n')
            
# MENU 5: KELUAR PROGRAM
    elif pilihanMenu == '5':
        keluarProgram = input('Apakah Anda yakin ingin keluar dari program? (Y/N): ')       # Konfirmasi exit program
        if keluarProgram.upper() == 'N':
            continue                                            # Lanjut ke menuUtama
        elif keluarProgram.upper() == 'Y':
            print('\n***** Terima kasih! *****')
            break                                               # Keluar dari program
    else:
        print('***** Pilihan tidak tersedia *****')
        
