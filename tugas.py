class bangunruang:
    def volbalok(self,panjang,lebar,tinggi):
        volume = panjang*lebar*tinggi
        print ("volume nya sebesar ", volume)
    def selbalok(self,p,l,t):
        ls= 2*((p*l)+(p*t)+(l*t))
        return ls

    def volkerucut(self,jari,tinggi):
        volume = (1/3)*3.14*jari*jari*tinggi
        return volume
    def lkerucut(self,r,s):
        luas=3.14*r*(r+s)
        print('Luas permukaan: ',luas)

    def voltabung(self,jari,tinggi):
        volume=3.14*jari*jari*tinggi
        print ("Volume tabung= ", volume)
    def ltabung(self,r,t):
        luas= 2*3.14*r*(r+t)
        print('Luas permukaan: ',luas)

    def volbola(self,jari):
        volume= 4/3 * 3.14 *jari*jari*jari
        return volume
    def lbola (self,r):
        luas= 4*3.14*r*r
        print('Luas permukaan: ', luas)

a=bangunruang()
def balok():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas Permukaan\nPilihan: '))
    while (pil <1 or pil>2):
        pil=int (input('masukan tidak tersedia\nsilahkan masukan kembali pilihan anda: '))
    p = float(input("masukkan panjang: "))
    l = float(input ("masukkan lebar: "))
    t = float(input ("masukkan tinggi: "))
    if (pil==1):
        a.volbalok(p,l,t)
    elif (pil==2):
       print('Luas selimutnya ', a.selbalok(p,l,t))

def kerucut():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas Permukaan\nPilihan: '))
    while (pil <1 or pil>2):
        pil=int (input('masukan tidak tersedia\nsilahkan masukan kembali pilihan anda: '))
    r = float(input("masukkan jari-jari: "))
    t = float(input ("masukkan tinggi: "))
    if (pil==1):
        print('volumenya sebesar ',a.volkerucut(r,t))
    elif (pil==2):
        s=float(input('masukkan garis pelukis: '))
        a.lkerucut(r,s)

def tabung():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas permukaan\nPilihan: '))
    while (pil <1 or pil>2):
        pil=int (input('masukan tidak tersedia\nsilahkan masukan kembali pilihan anda: '))    
    r = float(input("masukkan jari-jari: "))
    t = float(input ("masukkan tinggi: "))
    if (pil==1):
        a.voltabung(r,t)
    elif (pil==2):
        a.ltabung(r,t)

def bola():
    pil = int(input('\n1. Hitung Volume\n2. Hitung Luas Permukaan\nPilihan: '))
    while (pil <1 or pil>2):
        pil=int (input('masukan tidak tersedia\nsilahkan masukan kembali pilihan anda: '))    
    r = float(input("masukkan jari-jari: "))
    if (pil==1):
        print('volumenya adalah', a.volbola(r))
    elif (pil==2):
        a.lbola(r)
