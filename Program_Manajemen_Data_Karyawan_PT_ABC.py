#=============================================== CAPSTONE PROJECT ===============================================#
#============================================= Sistem Data Karyawan =============================================#

from tabulate import tabulate

#========================================== DATA SET ============================================================
# Dataset Karyawan menggunakan dictionary di dalam list. 
# *NIK = Nomor Induk Karyawan. Bukan NIK KTP
daftar_karyawan = [ 
    {"NIK": 1001, "Nama": "Erik Thohir", "Jenis Kelamin": "Laki-Laki", "Usia": 54, "Jabatan": "Direktur", "Divisi": "Utama", "Status Karyawan": "Tetap", "Gaji": 10000},
    {"NIK": 2001, "Nama": "Patrick Kluivert", "Jenis Kelamin": "Laki-Laki", "Usia": 48, "Jabatan": "Manager", "Divisi": "Pemasaran", "Status Karyawan": "Tetap", "Gaji": 8000},
    {"NIK": 2002, "Nama": "Shin Tae Yong", "Jenis Kelamin": "Laki-Laki", "Usia": 54, "Jabatan": "Manager", "Divisi": "Keuangan", "Status Karyawan": "Tetap", "Gaji": 7000},
    {"NIK": 2003, "Nama": "Melody Nurramdhani Laksani", "Jenis Kelamin": "Perempuan", "Usia": 33, "Jabatan": "Manager", "Divisi": "SDM", "Status Karyawan": "Tetap", "Gaji": 6000},
    {"NIK": 3001, "Nama": "Jay Noah Idzes", "Jenis Kelamin": "Laki-Laki", "Usia": 24, "Jabatan": "Staff", "Divisi": "Keuangan", "Status Karyawan": "Kontrak", "Gaji": 3000},
    {"NIK": 3002, "Nama": "Ayana Shahab", "Jenis Kelamin": "Perempuan", "Usia": 27, "Jabatan": "Staff", "Divisi": "Keuangan", "Status Karyawan": "Magang", "Gaji": 2000},
    {"NIK": 3003, "Nama": "Rizky Ridho Ramadhani ", "Jenis Kelamin": "Laki-Laki", "Usia": 23, "Jabatan": "Staff", "Divisi": "Pemasaran", "Status Karyawan": "Kontrak", "Gaji": 3000},
    {"NIK": 3004, "Nama": "Cindy Christina Gulla", "Jenis Kelamin": "Perempuan", "Usia": 27, "Jabatan": "Staff", "Divisi": "Pemasaran", "Status Karyawan": "Magang", "Gaji": 2000},
    {"NIK": 3005, "Nama": "Ragnar Oratmangoen", "Jenis Kelamin": "Laki-Laki", "Usia": 27, "Jabatan": "Staff", "Divisi": "SDM", "Status Karyawan": "Kontrak", "Gaji": 3000},
    {"NIK": 3006, "Nama": "Shani Indira Natio", "Jenis Kelamin": "Perempuan", "Usia": 26, "Jabatan": "Staff", "Divisi": "SDM", "Status Karyawan": "Magang", "Gaji": 2000}
    ]

#========================================== MAIN MENU ============================================================
def menu_utama():
    print(f"{20*"="} Sistem Data Karyawan {20*"="} \n")
    print(f"{20*"-"} PT Anak Bangsa Ceria {20*"-"}") 
    print('''
Selamat Datang di Sistem Data Karyawan
PT Anak Bangsa Ceria
          
Menu:
    1. Menampilkan Daftar Karyawan
    2. Menambah Data Karyawan
    3. Update Data Karyawan
    4. Menghapus Data Karyawan
    0. Keluar Program
''')

# table_input= []
# table_sementara=[]
# daftar_karyawan["NIK"][0] == '3'
# table_input["NIK"] = table_sementara[-1]["NIK"]+1

#========================================== FUNCTION'S ============================================================

# Function untuk validasi input yang berupa angka
def valInput_angka (perintah, pesan_error = "⚠ Input tidak valid! Input harus berupa angka!"):
    while True:
        try:
            return int(input(perintah))
        except:
            print(pesan_error)

# Function untuk validasi input yang berupa huruf
def valInput_huruf (perintah, pesan_error = "⚠ Input tidak valid! Input harus berupa angka!"):
    while True:
        input_huruf = input(perintah)
        if input_huruf.replace(' ', '').isalpha():
            return input_huruf
        else:
            print(pesan_error)

# Function untuk mengakses menu program dengan input nomor 
def input_menu():
    global inputMenu
    while True:
        try:
            inputMenu = int(input("Masukkan nomor menu yang ingin Anda jalankan: "))
            return inputMenu
        except:
            print("⚠ Input tidak valid! Input harus berupa angka!")

# Function untuk konfirmasi lanjut ke code berikutnya atau tidak
def val_Konfirmasi (perintah, pesan_error = "Input Tidak Valid. Input harus Yes / No"):
    while True:
        input_yes_no = valInput_huruf(perintah)
        if input_yes_no.lower() == "yes":
            return True
        elif input_yes_no.lower() == "no":
            return False
        else:
            print(pesan_error)

# Function val_NIK berfungsi untuk mengecek apakah data NIK sudah terdaftar atau belum di dataset daftar_karyawan
# Function ini akan digunakan di dalam function lain untuk membuat data NIK karyawan baru 
def val_NIK (perintah, pesan_error = "⚠ NIK sudah terdaftar. Silahkan masukkan NIK lain"):
    while True:
        input_NIK = valInput_angka(perintah)
        if len(str(input_NIK)) != 4: #---> hasil input di-casting menjadi string untuk mengecek jumlah karakternya, jika tidak sama dengan 4 maka akan menampilkan pesan error
            print("⚠ NIK tidak valid! NIK harus terdiri dari 4 angka!")
            continue #---> Jika input belum sesuai, continue akan mengembalikan lagi ke looping awal dan meminta input ulang sebelum menjalankan code berikutnya
    
        NIK_terdaftar = [data ["NIK"] for data in daftar_karyawan]
        if input_NIK in NIK_terdaftar: #--> "in" berarti jika NIK yang diinput ada di  daftar_karyawan maka akan menampilkan pesan error
                print(pesan_error) 
        else:
            return int(input_NIK)

# Function val_NIK_2 berfungsi untuk mengecek apakah data NIK ada di dalam daftar karyawan
# Function ini akan digunakan dalam function lain untuk menampilkan dan mengupdate data karyawan berdasarkan NIK yang telah terdaftar di dataset daftar_karyawan 
def val_NIK_2 (perintah, pesan_error = "⚠ NIK tidak terdaftar. Silahkan masukkan NIK lain"):
    while True:
        input_NIK = valInput_angka(perintah)
        if len(str(input_NIK)) != 4: 
            print("⚠ NIK tidak valid! NIK harus terdiri dari 4 angka!")
            continue 
    
        NIK_terdaftar = [data ["NIK"] for data in daftar_karyawan]
        if input_NIK not in NIK_terdaftar:  #--> "not in" berarti jika NIK yang diinput tidak ada di daftar_karyawan maka akan menampilkan pesan error
                print(pesan_error) 
        else:
            return int(input_NIK)

# Function untuk validasi data Gender/Jenis Kelamin 
dict_gender = {"L" : "Laki-Laki", "P": "Perempuan"}

def val_Gender (perintah, pesan_error = "⚠ Input tidak valid! Input harus L / P!"):
    while True:
        inputGender = input(perintah)
        if inputGender.upper() in dict_gender: #Mengubah inputGender menjadi huruf besar dan memeriksa apakah input yang dimasukkan sesuai dengan dict_gender 
            return dict_gender[inputGender.upper()] # Mengubah input menjadi huruf besar (L/P) agar dapat dikembalikan menjadi value dari dict_gender
        else:
            print(pesan_error)

# Function untuk validasi data Usia 
def val_Usia (perintah, pesan_error = "⚠ Input tidak valid! Usia min 18 dan max 60"):
    while True:
        inputUsia = valInput_angka(perintah)
        if inputUsia >=18 and inputUsia <=60:
            return inputUsia
        else:
            print(pesan_error)

# Function untuk validasi data Jabatan
def val_Jabatan (perintah, pesan_error = "⚠ Input Jabatan tidak valid! Jabatan yang tersedia hanya Direktur, Manager, dan Staff"):
    while True:
        inputJabatan = valInput_huruf(perintah)
        for data in daftar_karyawan:
            if inputJabatan.capitalize() == "Direktur" or inputJabatan.capitalize() == "Manager" or inputJabatan.capitalize() == "Staff":
                return inputJabatan.capitalize()
        else:
            print(pesan_error)

# Function untuk validasi Data Divisi
def val_Divisi (perintah, pesan_error = "⚠ Input Divisi tidak valid! Divisi yang tersedia hanya Utama, Keuangan, Pemasaran dan SDM"):
    while True:
        inputDivisi = valInput_huruf(perintah)
        if inputDivisi.capitalize() == "Utama" or inputDivisi.capitalize() == "Keuangan" or inputDivisi.capitalize() == "Pemasaran" or inputDivisi.upper() == "SDM":
            return inputDivisi.capitalize()
        else:
            print(pesan_error)

# Function untuk validasi data Status Karyawan
def val_Status (perintah, pesan_error = "⚠ Input Status tidak valid! Status Karyawan yang tersedia hanya Tetap, Kontrak, dan Magang"):
    while True:
        inputStatus = valInput_huruf(perintah)
        if inputStatus.capitalize() == "Tetap" or inputStatus.capitalize() == "Kontrak" or inputStatus.capitalize() == "Magang":
            return inputStatus.capitalize()
        else:
            print(pesan_error)

# Function untuk validasi data Gaji Karyawan
def val_Gaji (perintah, pesan_error = "⚠ Input tidak valid! Gaji minimum 1.000 dan max 10.000"):
    while True:
        inputGaji = valInput_angka(perintah)
        if inputGaji >=1000 and inputGaji <=10000:
            return inputGaji
        else:
            print(pesan_error)

#============================================================ MENU 1: MENAMPILKAN DAFTAR KARYAWAN (READ) ============================================================

# Function untuk menampilkan data seluruh karyawan
def menu1_showAll_Karyawan():
        for data in daftar_karyawan:
            if data:
                print(f"{50*"="} Daftar Karyawan {50*"="}")
                print(f"{47*"-"} PT Anak Bangsa Ceria {47*"-"}\n")  
                print(tabulate(daftar_karyawan, headers="keys", tablefmt="fancy_grid"))
                print()
                break
        else:
            print("\n⚠ Tidak ada data yang dapat ditampilkan \n")
                
# Function untuk menampilkan data karyawan berdasarkan NIK
def menu1_filterNIK():
    while True:
        filter_NIK = val_NIK_2("Masukkan Nomor Induk Karyawan (NIK): ")
        show_NIK = []
        for data in daftar_karyawan:
            if data ["NIK"] == filter_NIK:
                show_NIK.append(data)
                simpan_data = data # untuk menyimpan data dari dictionary karyawan yang ditemukan dari NIK
        if show_NIK:
            print(f"\n{35*"="} Daftar Karyawan dengan NIK: {filter_NIK} {35*"="}\n")
            print(tabulate(show_NIK, headers="keys", tablefmt="fancy_grid"))
            print()
            return simpan_data
        else:
            print("⚠ Tidak ada data karyawan dengan NIK tersebut! \n")
            print()

# Function untuk menampilkan data karyawan berdasarkan Divisi
def menu1_filterDivisi():
    while True:
        filterDivisi = valInput_huruf("Masukkan Divisi yang ingin ditampilkan: ").lower()
        show_divisi = []
        for data in daftar_karyawan:
            if data["Divisi"].lower() == filterDivisi:
                    show_divisi.append(data)
        if show_divisi:
            print(f"\n{35*"="} Daftar Karyawan di Divisi: {filterDivisi.upper()} {35*"="}\n")
            print(tabulate(show_divisi, headers="keys", tablefmt="fancy_grid"))
            print()
            return show_divisi
        else:
            print("⚠ Tidak ada data karyawan di Divisi tersebut!")
            print()

# Function untuk menampilkan data karyawan berdasarkan Jabatan
def menu1_filterJabatan():
    while True:
        filterJabatan = valInput_huruf("Masukkan Jabatan yang ingin ditampilkan: ").lower()
        show_jabatan = []
        for data in daftar_karyawan:
            if data["Jabatan"].lower() == filterJabatan:
                    show_jabatan.append(data)
        if show_jabatan:
            print(f"\n{35*"="} Daftar Karyawan dengan jabatan: {filterJabatan.upper()} {35*"="}\n")
            print(tabulate(show_jabatan, headers="keys", tablefmt="fancy_grid"))
            print()
            return show_jabatan
        else:
            print("⚠ Tidak ada data karyawan dengan Jabatan tersebut!")
            print()

# Function untuk menampilkan data karyawan berdasarkan Jenis Kelamin
def menu1_filterGender():
    while True:
        filterGender = val_Gender("Masukkan Jenis Kelamin Karyawan yang ingin ditampilkan (L / P): ")
        show_gender = []
        for data in daftar_karyawan:
            if data["Jenis Kelamin"] == filterGender:
                show_gender.append(data) 
        if show_gender:
            print(f"\n{35*"="} Daftar Karyawan dengan Gender: {filterGender.upper()} {35*"="}\n")
            print(tabulate(show_gender, headers="keys", tablefmt="fancy_grid"))
            print()
            return show_gender
        else:
            print("⚠ Tidak ada data karyawan dengan Gender tersebut!")

# Function untuk menampilkan data karyawan berdasarkan Status Karyawan
def menu1_filterStatus():
    while True:
        filterStatus = val_Status("Masukkan Status Karyawan yang ingin ditampilkan: ")
        show_status = []
        for data in daftar_karyawan:
            if data["Status Karyawan"] == filterStatus:
                show_status.append(data)
        if show_status:
            print(f"\n{35*"="} Daftar Karyawan dengan Status: {filterStatus.upper()} {35*"="}\n")
            print(tabulate(show_status, headers="keys", tablefmt="fancy_grid"))
            print()
            return show_status
        else:
            print("⚠ Tidak ada data karyawan dengan Status tersebut!")

# Function untuk menampilkan dan mengakses Sub Menu 3 dalam menu 1
def menu1_subMenu3():
    while True:
        print(f"{10*"="} Sub Menu 3: Menampilkan Daftar Karyawan Berdasarkan Kolom Kriteria {10*"="}")
        print('''
    Menu:
    1. Tampilkan Data Karyawan Berdasarkan Divisi
    2. Tampilkan Data Karyawan Berdasarkan Jabatan
    3. Tampilkan Data Karyawan Berdasarkan Jenis Kelamin
    4. Tampilkan Data Karyawan Berdasarkan Status Karyawan
    0. Kembali ke Menu 1
    ''')
        pilih = input_menu()

        if pilih == 1:
            menu1_filterDivisi()
        elif pilih == 2:
            menu1_filterJabatan()
        elif pilih == 3:
            menu1_filterGender()
        elif pilih == 4:
            menu1_filterStatus()
        elif pilih == 0:
            print()
            return
        else:
            print("⚠ Input tidak valid! Input harus berupa angka 0-4!")
            print()


# Function untuk menampilkan dan mengakses menu 1
def menu1_utama():
    while True:
        print(f"{10*"="} Menu 1: Menampilkan Daftar Karyawan {10*"="}")
        print('''
    Menu:
    1. Tampilkan Seluruh Data Karyawan
    2. Tampilkan Data Karyawan Berdasarkan NIK
    3. Tampilkan Data Karyawan Berdasarkan Kolom Kriteria
    0. Kembali ke Menu Utama
    ''')
        pilih = input_menu()
        
        if pilih == 1:
            menu1_showAll_Karyawan()
        elif pilih == 2:
            menu1_filterNIK()
        elif pilih == 3:
            menu1_subMenu3()
        elif pilih == 0:
            print()
            return
        else:
            print("⚠ Input tidak valid! Input harus berupa angka 0-3!")
            print()
    

#============================================================ MENU 2: MENAMBAH DATA KARYAWAN (CREATE) ============================================================

# Function untuk menambah data karyawan secara manual
def menu2_tambahManual():
    inputNIK = val_NIK("Masukkan NIK Karyawan: ")
    
    input_nama = valInput_huruf("Masukkan Nama Karyawan: ").title()

    input_gender = val_Gender("Masukkan Jenis Kelamin Karyawan (L/P): ")

    input_usia = val_Usia("Masukkan Usia (18-60 tahun): ")

    input_jabatan = val_Jabatan("Masukkan Jabatan: ")

    input_divisi = val_Divisi("Masukkan Divisi: ")

    input_status = val_Status("Masukkan Status Karyawan: ")

    input_gaji = val_Gaji("Masukkan Gaji (tanpa titik): ")

    karyawan_baru = {"NIK": inputNIK, "Nama": input_nama, "Jenis Kelamin": input_gender, "Usia": input_usia, "Jabatan": input_jabatan, "Divisi": input_divisi, "Status Karyawan": input_status, "Gaji": input_gaji}
    
    print(f'\n{33*"="} Tambah Karyawan Baru dengan NIK: {inputNIK} {33*"="}\n')
    print(tabulate([karyawan_baru], headers="keys", tablefmt="fancy_grid"))
    print()
    
    if val_Konfirmasi("Apakah Anda yakin ingin menambahkan data Karyawan ini? (Yes/No): "):
        print()
        daftar_karyawan.append(karyawan_baru)
        
        def urutkan_NIK (daftar_karyawan):
            return daftar_karyawan["NIK"]
        daftar_karyawan.sort(key=urutkan_NIK)
        
        menu1_showAll_Karyawan()
        print(f'✔ Tambah Data Berhasil!')
        print(f"✔ Data Karyawan Baru dengan NIK {inputNIK} atas nama {input_nama} Berhasil ditambahkan ke Daftar Karyawan!")
        print()
    else:
        print("\n✖ Penambahan Data Karyawan dibatalkan! \n")

# Function untuk menambah data karyawan tanpa input NIK. NIK akan ter-generate secara otomatis sesuai Jabatan
kode_jabatan = {
    "Direktur" : 1000,
    "Manager": 2000,
    "Staff": 3000}

def menu2_tambahOtomatis():
    input_nama = valInput_huruf("Masukkan Nama Karyawan: ").title()

    input_gender = val_Gender("Masukkan Jenis Kelamin Karyawan (L/P): ")

    input_usia = val_Usia("Masukkan Usia (18-60 tahun): ")

    input_jabatan = val_Jabatan("Masukkan Jabatan: ")

    input_divisi = val_Divisi("Masukkan Divisi: ")

    input_status = val_Status("Masukkan Status Karyawan: ")

    input_gaji = val_Gaji("Masukkan Gaji (tanpa titik): ")

    jabatan = input_jabatan
    kode_awal = kode_jabatan[jabatan]
    
    NIK_jabatan = [data["NIK"] for data in daftar_karyawan if data["Jabatan"] == input_jabatan]
                
    if NIK_jabatan:
        NIK_baru = max(NIK_jabatan) + 1 # Mencari nilai tertinggi dari NIK berdasarkan jabatan yang telah di-filter, dan menambah dengan 1 utk membauat NIK baru
    else:
        NIK_baru = kode_awal + 1
    
    karyawan_baru = {"NIK": NIK_baru, "Nama": input_nama, "Jenis Kelamin": input_gender, "Usia": input_usia, "Jabatan": input_jabatan, "Divisi": input_divisi, "Status Karyawan": input_status, "Gaji": input_gaji}

    print(f'\n{33*"="} Tambah Karyawan Baru dengan NIK: {NIK_baru} {33*"="}\n')
    print(tabulate([karyawan_baru], headers="keys", tablefmt="fancy_grid"))
    print()

    if val_Konfirmasi("Apakah Anda yakin ingin menambahkan data Karyawan ini? (Yes/No): "):
        print()
        daftar_karyawan.append(karyawan_baru)

        def urutkan_NIK (data):
            return data["NIK"] # Mengembalikan nilai dari key "NIK" dalam dictionary data
        daftar_karyawan.sort(key=urutkan_NIK) # Mengurutkan data NIK dari daftar_karyawan 

        menu1_showAll_Karyawan()
        print(f'✔ Tambah Data Berhasil!')
        print(f"✔ Data Karyawan Baru dengan NIK {NIK_baru} atas nama {input_nama} Berhasil ditambahkan ke Daftar Karyawan!")
        print()
    else:
        print("\n✖ Penambahan Data Karyawan dibatalkan! \n")


# Function untuk menampilkan dan mengakses menu 2
def menu2_utama():
    while True:
        print(f"{10*"="} Menu 2: Menambah Data Karyawan {10*"="}")
        print('''
    Menu:
    1. Tambah Data Karyawan Baru (Manual)
    2. Tambah Data Karyawan Baru (NIK Otomatis)
    0. Kembali ke Menu Utama
    ''')

        pilih = input_menu()
        
        if pilih == 1:
            menu2_tambahManual()
            
        elif pilih == 2:
            menu2_tambahOtomatis()

        elif pilih == 0:
            return
        else:
            print("⚠ Input tidak valid! Input harus berupa angka 0-2!")

#============================================================ MENU 3: UPDATE DATA KARYAWAN (UPDATE) ============================================================

# Function untuk merubah Nama Karyawan
def menu3_updateNama():
    data = menu1_filterNIK() # Memanggil function utk mencari NIK sesuai input. Jika ditemukan, data berisi informasi karyawan dalam bentuk dict dan ditampilkan dalam 1 baris tabel. 
    if data:                 # Data karyawan yang telah ditemukan disimpan dalam variabel "data" agar bisa digunakan kembali
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]}')
        print()
        input_updateNama = valInput_huruf("Masukkan Nama Karyawan yang baru: ").title()
               
        update_data = {"NIK": data["NIK"], "Nama": input_updateNama, "Jenis Kelamin": data["Jenis Kelamin"], "Usia": data["Usia"], "Jabatan": data["Jabatan"], "Divisi": data["Divisi"], "Status Karyawan": data["Status Karyawan"], "Gaji": data["Gaji"]}

        print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
        print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

        print()
        if val_Konfirmasi(f"Apakah Anda yakin untuk merubah Nama Karyawan ini menjadi {input_updateNama}? (Yes/No): "):
            print()
            data["Nama"] = input_updateNama # Menyimpan hasil input_updateNama ke dalam dictionary "data"

            menu1_showAll_Karyawan() # Menampilkan daftar karyawan secara keseluruhan untuk memastikan bahwa data yang di-update juga sudah masuk ke daftar karyawan
            print(f'✔ Update Nama Karyawan Berhasil!')
            print(f'✔ Nama Karyawan dengan NIK {data["NIK"]} telah berhasil diubah menjadi {input_updateNama}!')
            print("✔ Daftar Karyawan telah di-update!\n")
        else:
            print("\n✖ Update Nama Karyawan dibatalkan! \n")
    else:
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")


# Function untuk merubah jabatan karyawan beserta NIK-nya sesuai dengan jabatan barunya
def menu3_updateJabatan():
    data = menu1_filterNIK()

    if data:
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} saat ini menjabat sebagai {data ["Jabatan"].upper()} di Divisi {data["Divisi"]}')
        print()
        input_updateJabatan = val_Jabatan("Masukkan Jabatan Karyawan yang baru: ")

        update_data = {"NIK": data["NIK"], "Nama": data["Nama"], "Jenis Kelamin": data["Jenis Kelamin"], "Usia": data["Usia"], "Jabatan": input_updateJabatan, "Divisi": data["Divisi"], "Status Karyawan": data["Status Karyawan"], "Gaji": data["Gaji"]}

        print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
        print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

        print()
        if val_Konfirmasi(f'Apakah Anda Yakin untuk merubah Jabatan Karyawan ini menjadi {input_updateJabatan.upper()}? (Yes/No): '):
            print()
            kode_awal = kode_jabatan[input_updateJabatan] # Mengambil kode jabatan dari input yang dimasukkan
            NIK_Jabatan = []

            for karyawan in daftar_karyawan:
                if karyawan["Jabatan"] == input_updateJabatan:
                    NIK_Jabatan.append(karyawan["NIK"]) # Jika ada karyawan lain yang memiliki jabatan yang sama dengan jabatan baru, tambahkan NIK-nya ke dalam list NIK_Jabatan

            if NIK_Jabatan:
                NIK_baru = max(NIK_Jabatan) + 1
            else:
                NIK_baru = kode_awal + 1
            
            data["NIK"] = NIK_baru # Mengupdate NIK karyawan dengan hasil dari NIK_baru

            def urutkan_NIK (karyawan):
                return karyawan["NIK"]
            daftar_karyawan.sort(key=urutkan_NIK)

            menu1_showAll_Karyawan()
            print(f'✔ Update Jabatan Karyawan Berhasil!')
            print(f'✔ Karyawan atas nama {data["Nama"]} sekarang menjabat sebagai {input_updateJabatan.upper()} di Divisi {data["Divisi"]}')
            print(f'✔ Nomor Induk Karyawan (NIK) atas nama {data["Nama"]} sekarang menjadi {NIK_baru}')
            print("✔ Daftar Karyawan telah di-update!\n")
        else:
            print("\n✖ Update Jabatan Karyawan dibatalkan! \n")
    else:
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")


# Function untuk merubah Status Karyawan
def menu3_updateStatus():
    data = menu1_filterNIK()
    if data:
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} saat ini Berstatus sebagai Karyawan {data["Status Karyawan"].upper()}')
        print()
        input_updateStatus = val_Status("Masukkan Status Karyawan yang baru: ")  

        update_data = {"NIK": data["NIK"], "Nama": data["Nama"], "Jenis Kelamin": data["Jenis Kelamin"], "Usia": data["Usia"], "Jabatan": data["Jabatan"], "Divisi": data["Divisi"], "Status Karyawan": input_updateStatus, "Gaji": data["Gaji"]}

        print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
        print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))
        print()
        if val_Konfirmasi(f'Apakah Anda yakin untuk merubah Status Karyawan ini menjadi Karyawan {input_updateStatus.upper()}? (Yes/No): '):
            data["Status Karyawan"] = input_updateStatus
            print()
            menu1_showAll_Karyawan()
            print(f'✔ Update Nama Karyawan Berhasil!')
            print(f'✔ Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} sekarang Berstatus sebagai Karyawan {input_updateStatus}')
            print("✔ Daftar Karyawan telah di-update!\n")
        else:
            print("\n✖ Update Status Karyawan dibatalkan! \n")
    else:
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")

# Function untuk merubah data Divisi Karyawan
def menu3_updateDivisi():
    data = menu1_filterNIK()
    if data:
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} saat ini bertugas di Divisi {data["Divisi"]}')
        print()
        input_updateDivisi = val_Divisi("Masukkan Divisi Karyawan yang baru: ")

        update_data = {"NIK": data["NIK"], "Nama": data["Nama"], "Jenis Kelamin": data["Jenis Kelamin"], "Usia": data["Usia"], "Jabatan": data["Jabatan"], "Divisi": input_updateDivisi, "Status Karyawan": data["Status Karyawan"], "Gaji": data["Gaji"]}

        print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
        print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

        if val_Konfirmasi(f'\nApakah Anda yakin untuk merubah Divisi Karyawan ini menjadi Divisi {input_updateDivisi}? (Yes/No): '):
            data["Divisi"] = input_updateDivisi
            print()
            menu1_showAll_Karyawan()
            print(f'✔ Update Divisi Karyawan Berhasil!')
            print(f'✔ Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} sekarang bertugas di Divisi {input_updateDivisi}')
            print("✔ Daftar Karyawan telah di-update!\n") 
        else:
            print("\n✖ Update Divisi Karyawan dibatalkan! \n")
    else:
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")

# Function untuk merubah data Usia Karyawan
def menu3_updateUsia():
    data = menu1_filterNIK()
    if data:
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} saat ini berusia {data["Usia"]} Tahun')
        print()
        while True:
            input_updateUsia = val_Usia("Masukkan Usia karyawan yang baru: ")
            
            if input_updateUsia <= data["Usia"]:
                print(f'Input tidak valid! Usia Karyawan saat ini {data["Usia"]}\n')
                continue
            else:
                update_data = {"NIK": data["NIK"], "Nama": data["Nama"], "Jenis Kelamin": data["Jenis Kelamin"], "Usia": input_updateUsia, "Jabatan": data["Jabatan"], "Divisi": data["Divisi"], "Status Karyawan": data["Status Karyawan"], "Gaji": data["Gaji"]}

                print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
                print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

                if val_Konfirmasi(f'\nApakah Anda yakin Karyawan ini sudah berulang tahun dan merubah data usianya menjadi {input_updateUsia} Tahun? (Yes/No): '):
                    data["Usia"] = input_updateUsia
                    print()
                    menu1_showAll_Karyawan()
                    print(f'✔ Update Usia Karyawan Berhasil!')
                    print(f'✔ Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} sekarang berusia {input_updateUsia} Tahun')
                    print("✔ Daftar Karyawan telah di-update!\n")
                    break
                else:
                    print("\n✖ Update Usia Karyawan dibatalkan! \n")
                    break
    else:
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")

# Function untuk merubah data Jenis Kelamin Karyawan
def menu3_updateGender():
    data = menu1_filterNIK()
    if data:
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} adalah seorang {data["Jenis Kelamin"]}')
        print()
        while True:
            input_updateGender = val_Gender("Masukkan Gender karyawan (L/P): ")

            if input_updateGender == data["Jenis Kelamin"]:
                print(f'Input tidak valid! Jenis Kelamin masih sama!')
                continue
            else:
                update_data = {"NIK": data["NIK"], "Nama": data["Nama"], "Jenis Kelamin": input_updateGender, "Usia": data["Usia"], "Jabatan": data["Jabatan"], "Divisi": data["Divisi"], "Status Karyawan": data["Status Karyawan"], "Gaji": data["Gaji"]}

                print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
                print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

                if val_Konfirmasi(f'\nApakah Anda yakin akan merubah data Jenis Kelamin Karyawan ini menjadi {input_updateGender}? (Yes/No): '):
                    data["Jenis Kelamin"] = input_updateGender
                    print()
                    menu1_showAll_Karyawan()
                    print(f'✔ Update Data Jenis Kelamin Karyawan Berhasil!')
                    print(f'✔ Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} sekarang adalah seorang {input_updateGender}')
                    print("✔ Daftar Karyawan telah di-update!\n")
                    break
                else:
                    print("\n✖ Update Jenis Kelamin Karyawan dibatalkan! \n")
                    break
    else:
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")


# Function untuk merubah data Gaji Karyawan
def menu3_updateGaji():
    data = menu1_filterNIK()
    if data:
        print(f'Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} saat ini memiliki Gaji sebesar USD {data["Gaji"]} per Bulan')
        print()

        while True:
            ubah_gaji = valInput_huruf("Menaikkan Gaji / Menurunkan Gaji? (Naik/Turun): ")
            
            if ubah_gaji.lower() == "naik": 
                input_gaji = val_Gaji("Masukkan nominal penambahan / pengurangan gaji (tanpa titik): ")
                update_data = data.copy()
                update_data["Gaji"] += input_gaji
                print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
                print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

                if val_Konfirmasi(f'\nGaji Karyawan ini akan dinaikkan sebesar USD {input_gaji} menjadi USD {update_data["Gaji"]}. Apakah Anda yakin? (Yes/No): '):
                        data["Gaji"] = data["Gaji"] + input_gaji
                        print()
                        menu1_showAll_Karyawan()
                        print(f'✔ Update Gaji Karyawan Berhasil!')
                        print(f'✔ Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} sekarang memiliki Gaji sebesar USD {data["Gaji"]} per Bulan')
                        print("✔ Daftar Karyawan telah di-update!\n")
                        break                    
                else:
                    print("\n✖ Update Gaji Karyawan dibatalkan! \n")
                    break
            
            elif ubah_gaji.lower() == "turun":
                input_gaji = val_Gaji("Masukkan nominal (tanpa titik): ")
                update_data = data.copy()
                update_data["Gaji"] -= input_gaji
                print(f'\n{35*"="} Daftar Karyawan dengan NIK: {data["NIK"]} {35*"="}\n')
                print(tabulate([update_data], headers="keys", tablefmt="fancy_grid"))

                if val_Konfirmasi(f'\nGaji Karyawan ini akan diturunkan sebesar USD {input_gaji} menjadi USD {update_data["Gaji"]}. Apakah Anda yakin? (Yes/No): '):
                        data["Gaji"] = data["Gaji"] - input_gaji
                        print()
                        menu1_showAll_Karyawan()
                        print(f'✔ Update Gaji Karyawan Berhasil!')
                        print(f'✔ Karyawan dengan NIK {data["NIK"]} atas nama {data["Nama"]} sekarang memiliki Gaji sebesar USD {data["Gaji"]} per Bulan')
                        print("✔ Daftar Karyawan telah di-update!\n")
                        break                    
                else:
                    print("\n✖ Update Gaji Karyawan dibatalkan! \n")
                    break
        
            else:
                print("⚠ Input tidak valid! Ketik Naik/Turun untuk merubah data gaji!")
                continue 
    else: 
        print("⚠ Tidak ada Karyawan dengan NIK tersebut")


# Function untuk menampilkan dan mengakses menu 3
def menu3_utama():
    while True:
        print(f"{10*"="} Menu 3: Update Data Karyawan {10*"="}")
        print('''
    Menu:
    1. Update Data Nama Karyawan
    2. Update Data Jenis Kelamin Karyawan
    3. Update Data Usia Karyawan
    4. Update Data Jabatan Karyawan
    5. Update Data Divisi Karyawan
    6. Update Data Status Karyawan
    7. Update Data Gaji Karyawan
    0. Kembali ke Menu Utama
    ''')

        pilih = input_menu()
        
        if pilih == 1:
            menu3_updateNama() 
        elif pilih == 2:
            menu3_updateGender()
        elif pilih == 3:
            menu3_updateUsia()
        elif pilih == 4:
            menu3_updateJabatan()
        elif pilih == 5:
            menu3_updateDivisi()
        elif pilih == 6:
            menu3_updateStatus()
        elif pilih == 7:
            menu3_updateGaji()
        elif pilih == 0:
            return
        else:
            print("⚠ Input tidak valid! Input harus berupa angka 0-5!")


#============================================================ MENU 4: HAPUS DATA KARYAWAN (DELETE) ============================================================

# Function untuk menghapus data Karyawan berdasarkan NIK
def menu4_hapusData_NIK():
    filter_NIK = menu1_filterNIK()

    if not filter_NIK:
        print("\n⚠ Tidak ada Karyawan dengan NIK tersebut!")
        return
    if val_Konfirmasi(f'Apakah Anda yakin ingin menghapus data karyawan ini? (Yes/No): '):
        print()
        daftar_karyawan.remove(filter_NIK)
            
        menu1_showAll_Karyawan()
        print("✔ Data Karyawan Berhasil Dihapus!\n")
    else:
        print("\n✖ Hapus Data dibatalkan!\n")
        return
    

# Function untuk menghapus semua data Karyawan
def menu4_hapusAll():
    while True:
        menu1_showAll_Karyawan()
        print("Anda memilih untuk MENGHAPUS SEMUA DATA karyawan di atas")
        if val_Konfirmasi("Apakah Anda yakin dengan pilihan Anda? (Yes/No): "):
            daftar_karyawan.clear()
            print()

            menu1_showAll_Karyawan()
            print("✔ Semua Data Karyawan BERHASIL dihapus!\n")
            return True
        else:
            print("\n✖ Hapus Data dibatalkan!\n")
            return False

# Function untuk menghapus data Karyawan secara batch berdasarkan Divisi
def menu4_hapusBatch_divisi():
    filter_divisi = menu1_filterDivisi()

    if not filter_divisi:
            print("\n⚠ Tidak ada Karyawan dengan Divisi tersebut!")
            return

    if val_Konfirmasi(f'Apakah Anda yakin ingin menghapus seluruh data Karyawan di Divisi ini? (Yes/No): '):
        print()
        for data in filter_divisi:
            daftar_karyawan.remove(data)
            
        menu1_showAll_Karyawan()
        print("✔ Data Karyawan Berhasil Dihapus\n")
    else:
        print("\n✖ Hapus Data dibatalkan!\n")
        return

# Function untuk menghapus data Karyawan secara batch berdasarkan Jabatan
def menu4_hapusBatch_jabatan():
    filter_jabatan = menu1_filterJabatan()

    if not filter_jabatan:
            print("\n⚠ Tidak ada Karyawan dengan Jabatan tersebut \n")
            return

    if val_Konfirmasi(f"Apakah Anda yakin ingin menghapus seluruh data Karyawan dengan jabatan ini? (Yes/No): "):   
        print()
        for data in filter_jabatan:
            daftar_karyawan.remove(data)

        menu1_showAll_Karyawan()
        print("✔ Data Karyawan Berhasil Dihapus!\n")

    else:
        print("\n✖ Hapus Data dibatalkan!\n")
        return
                       
# Function untuk menghapus data Karyawan secara batch berdasarkan Jenis Kelamin
def menu4_hapusBatch_gender():
    filter_gender = menu1_filterGender()

    if not filter_gender:
            print("\n⚠ Tidak ada Karyawan dengan Jenis Kelamin tersebut!")
            return

    if val_Konfirmasi(f'Apakah Anda yakin ingin menghapus seluruh data Karyawan dengan Jenis Kelamin ini? (Yes/No): '):
        print()
        for data in filter_gender:
            daftar_karyawan.remove(data)
            
        menu1_showAll_Karyawan()
        print("✔ Data Karyawan Berhasil Dihapus!\n")
    else:
        print("\n✖ Hapus Data dibatalkan!\n")
        return
    
# Function untuk menghapus data Karyawan secara batch berdasarkan Status Karyawan
def menu4_hapusBatch_status():
    filter_status = menu1_filterStatus()

    if not filter_status:
            print("\n⚠ Tidak ada Karyawan dengan Status tersebut!")
            return

    if val_Konfirmasi(f'Apakah Anda yakin ingin menghapus seluruh data Karyawan dengan Status ini? (Yes/No): '):
        print()
        for data in filter_status:
            daftar_karyawan.remove(data)
            
        menu1_showAll_Karyawan()
        print("✔ Data Karyawan Berhasil Dihapus!\n")
    else:
        print("\n✖ Hapus Data dibatalkan!\n")
        return

# Function untuk menampilkan dan mengakses Sub Menu 3 dalam menu 4
def menu4_subMenu3():
    while True:
        print(f"{10*"="} Sub Menu 3: Menghapus Semua Daftar Karyawan Berdasarkan Kolom Kriteria {10*"="}")
        print('''
    Menu:
    1. Hapus Data Karyawan Berdasarkan Divisi
    2. Hapus Data Karyawan Berdasarkan Jabatan
    3. Hapus Data Karyawan Berdasarkan Jenis Kelamin
    4. Hapus Data Karyawan Berdasarkan Status Karyawan
    0. Kembali ke Menu 4
    ''')
        pilih = input_menu()

        if pilih == 1:
            menu4_hapusBatch_divisi()
        elif pilih == 2:
            menu4_hapusBatch_jabatan()
        elif pilih == 3:
            menu4_hapusBatch_gender()
        elif pilih == 4:
            menu4_hapusBatch_status()
        elif pilih == 0:
            print()
            return
        else:
            print("⚠ Input tidak valid! Input harus berupa angka 0-4!")
            print()

# Function untuk menampilkan dan mengakses menu 4
def menu4_utama():
    while True:
        print(f"{10*"="} Menu 4: Hapus Data Karyawan {10*"="}")
        print('''
    Menu:
    1. Hapus Data Karyawan Berdasarkan NIK
    2. Hapus Semua Data Karyawan
    3. Hapus Semua Data Karyawan Berdasarkan Kolom Kriteria
    0. Kembali ke Menu Utama
    ''')
        pilih = input_menu()
        
        if pilih == 1:
            menu4_hapusData_NIK()
        elif pilih == 2:
            menu4_hapusAll()
        elif pilih == 3:
            menu4_subMenu3()           
        elif pilih == 0:
            return
        else:
            print("⚠ Input tidak valid! Input harus berupa angka 0-3!")


#====================================================================== AKSES MENU UTAMA ======================================================================
while True:
    menu_utama()
    try:
        input_menu()
    except:
        print("⚠ Input tidak valid! Input harus berupa angka!")

    if inputMenu == 1:
        menu1_utama()
    elif inputMenu == 2:
        menu2_utama()
    elif inputMenu == 3:
        menu3_utama()
    elif inputMenu == 4:
        menu4_utama()
    elif inputMenu == 0:
        while True:
            if val_Konfirmasi("\nApakah Anda yakin ingin keluaur dari sistem? (Yes/No): "):
                print("\nBerhasil Keluar dari Program")
                print("TERIMA KASIH 😊")
                exit()
            else:
                print("\n✖ Batal Keluar dari Program!\n")
                break
             
    else:
        print("⚠ Input tidak valid! Input harus angka 0-4!")
