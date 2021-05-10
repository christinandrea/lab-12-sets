#Christina Andrea Putri - Universitas Kristen Duta Wacana

# Dhaka membuat program sederhana untuk pendataan buku milik pribadinya. Koleksi bukunya terbagi menjadi 2 kategori, yaitu sastra dan buku pelajaran/pendidikan. 
# Menu yang tersedia adalah tambah dan lihat
# Bagaimana output program jika Dhaka menginput 2 novel dan 2 buku pelajaran miliknya?


#Input : menu, kategori, jumlah, judulnya
#Proses : memilih antara menambah dan melihat data sesuai dengan keinginan kita
#Output : daftar buku sesuai kategori


try:
    while True:
        print("Menu : \n 1. Tambah data \n 2. Lihat data \n 3. Keluar")
        menu = int(input("Menu : "))
        if menu == 1 : 
            emp1, emp2 = set(),set()

            print("Kategori : \n 1. Sastra \n 2. Pendidikan")
            inpkat = int(input("Kategori: "))
            if inpkat==1 : 
                jmlsastra = int(input("Jumlah buku:"))

                for i in range(jmlsastra):
                    inpdata = input("Buku %d:"%(i+1))

                    emp1.add(inpdata)
                fset1 = frozenset(emp1)
                
            elif inpkat==2 : 
                jmlpend = int(input("Jumlah buku:"))

                for x in range(jmlpend):
                    inpdata2 = input("Buku %d:"%(x+1))

                    emp2.add(inpdata2)
                fset2 = frozenset(emp2)
        if menu==2:
            print("Sastra : ")
            for i in fset1:
                print(i)
            print("Pendidikan : ")
            for j in fset2:
                print(j)           
        elif menu==3:
            print("Terimakasih sudah menggunakan layanan ini.")
            
            break
except:
    print("Invalid input")