import tugas

print ("Abdullah Azzam farid ma'ruf / 21120119130071\nMuhammad anandito rafiansyah / 21120119130082\nShift 2\nKel 51\n\n")
print ("penghitung bangun ruang")
stop=False
while stop == False:
    print ("1. Balok")
    print ("2. Kerucut")
    print ("3. tabung")
    print ("4. Bola")
    print ("5. Keluar\n")
    i=int(input("masukkan pilihan anda: "))
    while (i<1 or i>5):
        i=int(input("pilihan tidak tersedia, silahkan masukkan lagi pilihan antara 1-5: "))
    if (i==1):
        tugas.balok()
    elif (i==2):
        tugas.kerucut()
    elif (i==3):
        tugas.tabung()
    elif (i==4):
        tugas.bola()
    elif (i==5):
        exit()

    s=input("\nApakah anda ingin mengulang?(Y/T)")
    if (s=='t'):
        stop=True
    elif (s=='y'):
        stop=False
