"""Bildiğimiz gibi her nesnenin kendine ait nitelikleri ve davranışları vardır. 
Nesneler birbirlerinden farklıdır ve kendi varoluşlarına göre davranırlar ve kendi 
kimliklerine sahiptirler.
OOP sınıflar ve nesneler üzerine kurulmuştur, "Sınıflar" bir problemi soyutlamak ve genelleştirmek 
için kullanılan yapılardır veya kılavuzlardır. Sınıflar, bir nesneye ait tüm özellikleri temsil eder. 
Bu özellikler nesnenin ne tür nitelikleri ve davranışları olacağını belirler.
Mesela "Araba" bir sınıftır. Arabalara ait nitelikler renk, hız, vites sayısı, yakıt türü vb. bir sürü nitelik olabilir.
"""

from pyexpat import model
from statistics import mode


class Araba():
    def cagir(self):
        print("araba gelsin")

opel=Araba()
opel.cagir()

"""---------------"""

class Araba():
    def __init__(self): 
        self.a = 5
        print(self.a)   
        print("naber")
    def cagir(self):
        print(self.a)
        print("araba geldi")

opel=Araba()
opel.cagir()

"""---------------"""

class Araba():
    def __init__(self):     # bu constructur (__init__) ile tekrar çağırmaya gerek yok çalıştırmak için
        print("araba gelsin")

"""---------------"""

class Araba:
    def __init__(self,beygir,tonaj,renk):
        self.beygir = beygir
        self.ton = tonaj
        self.renk = renk

opel = Araba(120,1.5,"kirmizi")
print(opel.beygir)
print(opel.ton)
print(opel.renk)

"""---------------"""

class Employee:
    def __init__(self,yas,tecrübe,pozisyon,maas):
        self.yas = yas
        self.tecrübe = tecrübe
        self.pozisyon = pozisyon
        self.maas = maas
    
emp1 = Employee(15, 5, "front end dev", 54544)
print(emp1.yas)
print(emp1.tecrübe)
print(emp1.pozisyon)
print(emp1.maas)

"""---------------"""

class Student:
    def __init__(self,sinif,yas,notOrt,belge):
        self.sinifNo = sinif
        self.yasi = yas
        self.notOrtalamasi = notOrt
        self.Takdir_Tesekkur = belge

ali = Student(4,9,3.9,"tesekkur")
veli = Student(8,13,5,"takdir")

print(ali.sinifNo)
print(veli.sinifNo)

"""---------------"""

class Araba:
    def __init__(self,beygir,tonaj,renk):
        self.beygir = beygir
        self.ton = tonaj
        self.renk = renk
    def bilgi(self):
        print(""" araba beygir gücü = {}
        araba ağirliği = {}
        araba rengi = {}
        """.format(self.beygir,self.ton,self.renk))
opel = Araba(120,1.5,"kirmizi")
toyota = Araba(150,1.8,"gri")
opel.bilgi()
toyota.bilgi()

"""---------------"""
class Member:
    def __init__(self,year,amount,name):
        self.year = year
        self.amount = amount
        self.name = name
    def write(self):
        print(""" üyelik yılı = {}
        banka tutarı = {}
        üye ismi = {}
        """.format(self.year,self.amount,self.name))
member1 = Member(5,5000,"fatih")
member2 = Member(1,1000,"veli")
member1.write()
member2.write()

"""---------------"""

class HastaneKayit:
    def __init__(self,hastaAdi,hastaliği,sigortaDurumu,yasi,cinsiyeti):
            self.hastaAdi = hastaAdi
            self.hastaliği = hastaliği
            self.sigortaDurumu = sigortaDurumu
            self.yasi = yasi
            self.cinsiyeti = cinsiyeti
    def Kayit(self):
        print("""
                Hastanın adı = {}
                Hastalığı = {}
                Sigorta Var/Yok = {}
                Hastanın Yası = {}
                Hatanın Cinsiyeti = {}
        """.format(self.hastaAdi,self.hastaliği,self.sigortaDurumu,self.yasi,self.cinsiyeti))
hasta1 = HastaneKayit("John","kalp spazmı","No",45,"erkek")
hasta2 = HastaneKayit("Ann","bilek burkulması","yes",25,"bayan")
hasta1.Kayit()
hasta2.Kayit()

"""---------------"""

class insan():
    isim = ""
    kilo = 0
    boy = 0
    def __init__(self,isim,kilo,boy):
        self.isim = isim
        self.kilo = kilo
        self.boy = boy
    def bilgi(self):
        print("""
        İsim = {}
        Kilo = {}
        Boy = {}
        """.format(self.isim,self.kilo,self.boy))
        #Bilgileri güncellemek için
    def bilgi_guncelle(self,a,b,c):
        self.isim = a
        self.kilo = b
        self.boy = c
        #--Güncelleme son--
insan1 = insan("Cem",70,1.75)
insan2 = insan("Ahmet",80,1.80)

insan1.bilgi_guncelle("Cemil",80,1.95)
insan2.bilgi_guncelle("Ahmet",80,1.95)
insan1.bilgi()
insan2.bilgi()

"""---------------"""

class BMW:
    def __init__(self,model,yas,hasarKaydı,Boya):
            self.model = model
            self.yas = yas
            self.hasarKaydı = hasarKaydı
            self.Boya = Boya
    def yazdir(self):
        print("""
            arabanın modeli = {}
            arabanın yaşı = {}
            Araçta hasar kaydı var mı? = {}
            Araçta lokal boya var mı? = {}  
        """.format(self.model,self.yas,self.hasarKaydı,self.Boya))
    def güncelle(self,a,b,c,d):
        self.model = a
        self.yas = b
        self.hasarKaydı = c
        self.Boya = d

arac1 = BMW(3.20,5,"YOK","YOK")
arac2 = BMW(5.20,1,"var","3 parça lokal boya tespit edildi")

arac1.güncelle(3.20,6,"Kazalı","Komple Boya")
arac2.güncelle(5.20,3,"pert","pert")
arac1.yazdir()
arac2.yazdir()

"""---------------"""

class insan():
    def __init__(self,isim,kilo,boy):
        self.isim = isim
        self.kilo = kilo
        self.boy = boy
    def bilgi(self):
        print("""
        İsim = {}
        Kilo = {}
        Boy = {}
        """.format(self.isim,self.kilo,self.boy))
        #Bilgileri güncellemek için
    def bilgi_guncelle(self,a,b):
        if b == 1:
            self.isim = a
        elif b == 2:
            self.kilo = a
        elif b == 3:
            self.boy = a
        #--Güncelleme son--
insan1 = insan("Cem",70,1.75)
insan2 = insan("Ahmet",80,1.80)
insan1.bilgi()
insan2.bilgi()
insan1.bilgi_guncelle("Cemil",1)
insan2.bilgi_guncelle("Hasan",1)
insan1.bilgi()
insan2.bilgi()

"""---------------"""

class yilan ():
    def __init__(self,yilan_yas,yil_uzunluk,yilan_zehir):
        self.yilan_yas = yilan_yas
        self.yil_uzunluk = yil_uzunluk
        self.yilan_zehir = yilan_zehir
    def bilgiler(self):
        print("""yilan yaşı ={}
yilan uzunluk = {}
yilan zehir durumu = {}
-------------------""".format(self.yilan_yas,self.yil_uzunluk,self.yilan_zehir))

liste = [5,3]
liste2 = [2,3]
liste3 = ["var","yok"]
liste_yilan_obje = []
for i in range(10):
    if i %2 == 0:
        liste_yilan_obje.append(yilan(liste[0],liste2[0],liste3[0]))
    else:
        liste_yilan_obje.append(yilan(liste[1],liste2[1],liste3[1]))

for i in liste_yilan_obje:
    i.bilgiler()


"""---------------"""

class surungen:
    def __init__(self,yas,uzunluk,kilo):
            self.yas = yas
            self.uzunluk= uzunluk
            self.kilo = kilo
    def bilgi(self):
        print(self.yas,self.uzunluk,self.kilo)
class yilan(surungen):
    def __init__(self,yas,uzunluk,kilo,zehir):
        self.zehir = zehir
        super().__init__(yas,uzunluk,kilo)
y1 = yilan(5,"6",70,"var")
y1.bilgi()
print(y1.zehir)

"""---------------"""

class Tesla():
    def __init__(self,model,yil,km,hasarKaydi):
            self.model = model
            self.yil = yil
            self.km = km
            self.hasarKaydi = hasarKaydi
    def yazdir(self):
        print("""
            aracın modeli = {}
            aracın yılı = {}
            aracın km si = {}
            aracın hasar Kaydı = {}
            """.format(self.model,self.yil,self.km,self.hasarKaydi))
    def guncelle(self,a,b,c,d):
        self.model = a
        self.yil = b
        self.km = c
        self.hasarKaydi = d
class Truck(Tesla):
    def __init__(self, model, yil, km, hasarKaydi):
        super().__init__(model, yil, km, hasarKaydi)

aracc = Tesla("S",2022,0,"yok")
aracc.yazdir()
aracc.guncelle("X",2023,0,"Yok")
aracc.yazdir()
truck = Truck("truck",2020,0,"var")
truck.yazdir()

