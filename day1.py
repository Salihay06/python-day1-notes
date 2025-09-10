'''''''''
#Gün gün çalıştığım konuları buraya not alıyorum

#Burda kodu çalışması terminale py day1.py yazarak yada f5 tuşşuna basıp ordan çalıştırıır
print("Hello World")

print(2+2)  #Burda 2+2 işlemi yapılıp sonucu ekrana yazdırılır
print("2+2") #Burda ise 2+2 işlemi yapılmaz direk ekrana 2+2 yazdırılır
# ** işareti üs olarak kullanılır yani 2**3=2 üzeri 3 demektir
# % işareti ise mod alma işlemi yapar yani 10%3 işlemi 10 un 3 e bölümünden kalanı verir sonuç 1 dir


maasAli= 5000
maasAhmet= 4000
vergi=0.27

print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))

# Değişken Tanımlama kuralları
# 1. Sayı ile başlayamaz
# 2. Boşluk içeremez
# 3. Türkçe karakter içeremez
# 4. Değişken isimleri anlamlı olmalı
# 5. Küçük büyük harf duyarlılığı vardır
# 6. Özel karakterler içeremez _ hariç

number=10
print(number)
number=20
print(number)
number+=30 #number=number+30 ile aynı anlama gelir
print(number)


firstName="Salih"
secondName="Ay"
print(firstName +" "+ secondName) # Salih Ay


x,y,name,isStudent= (1,2.3,"Salih",True) #Birden fazla değişkene aynı anda değer atama



#ÖRNEK
name="Ali"
surname="Yılmaz"
fullName=name+" "+surname
cinsiyet=True
tcNo="12345678901"
dogumYili=2000
yas=2024-dogumYili

#ÖRNEK2
order1=110
order2=120
order3=100
total=order1+order2+order3
print("Toplam Sipariş Tutarı:", total)

# 2 ifade sring olarak toplanırsa arka arkaya yazılır
print("2"+"2") #çıktı 22 olur

#kullanıcıdan veri alma
x = input("Bir sayı giriniz:") #input ile kullanıcıdan veri alırız
y = input("Bir sayı daha giriniz:")

print(type(x)) #input ile alınan veriler str yani string olarak alınır
print(type(y))

toplam = int(x) + int(y) #int ile string olan veriyi integer a çeviririz
print("Toplam:", toplam)



# Dairenin çevresini ve alanını hesaplama

pii=3.14
r= input("Dairenin yarıçapını giriniz:")
perimeter= 2*pii*int(r)
area=pii*pii*int(r)

print("Dairenin çevresi:", perimeter)
print("Dairenin alanı:", area)
#alternatif yazım biçimi
print("area:", area, "perimeter:", perimeter) #Birden fazla değeri ekrana yazdırma

name="Salih"
surname="Ay"
age=20
print("My name is "+ name+" "+ surname+ " and \nI am "+str(age)+" years old")
# \n ifadesi alt satıra geçmeyi sağlar
# \t ifadesi ise tab boşluğu bırakır

greeting="My name is "+ name+" "+ surname+ " and \nI am "+str(age)+" years old"
print(greeting[0:10]) #0 dan 10 a kadar olan karakterleri yazdırır
print(len(greeting)) #len ifadesi stringin uzunluğunu verir
print(greeting.lower()) #tüm karakterleri küçük yapar,
print(greeting.upper()) #tüm karakterleri büyük yapar

name = "Salih"
surname = "Ay"
print("My name is {} {}".format(name,surname)) #format ile değişkenleri stringin içine yerleştirme
print("My name is {1} {0}".format(name,surname)) 
print("My name is {s} {n}".format(n=name,s=surname)) 

result = 200/700
print("Result is {r:1.3}".format(r=result)) #:1.3 ifadesi sonucu 1.si solda kaç basamak olcağı ikincisi virgülden sonra kaç karakter olaacğını belirler

print(f"My name is {name} {surname} and I am {age} years old") #f string ile formatlama


#ÖRNEK

website="www.salihay.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

result=len(course) #course stringinin uzunluğunu verir

result = website[7:10] #7 den 10 a kadar olan karakterleri yazdırı

result=website[12:] #12 den sonuna kadar olan karakterleri yazdırır

result=course[::-1] #course stringini ters çevirir

print(result)

s="12345"*5 #12345 i 5 kere tekrarlar
print(s) #1234512345123451234512345
print(s[::5]) #5 er 5 er atlayarak yazdırır 1111

meessage="Hello There. My name is Salih Ay. I am a Python Developer"
meessage=message.upper() #tüm karakterleri büyük yapar
meessage=message.lower() #tüm karakterleri küçük yapar
meessage=message.title() #her kelimenin ilk harfini büyük yapar
meessage=message.capitalize() #sadece ilk harfi büyük yapar
meessage=message.strip() #başındaki ve sonundaki boşlukları siler
meessage=message.split() #kelimeleri boşluklardan ayırarak liste yapar
meessage=message.split(".") #noktalardan ayırarak liste yapar
meessage="----".join(meessage) #liste elemanlarını --- ile birleştirir
meessage=message.replace(" ","*") #boşlukları * ile değiştirir
meessage=meessage.center(100,"*") #stringi 100 karaktere tamamlar ortalar ve boşlukları * ile doldurur

index=meessage.find("Salih") #Salih kelimesinin başladığı indexi verir

isfound=message.startswith("H") #message ifadesi Hello ile başlıyormu diye kontrol eder True yada False döner
isfound=message.endswith("r") #message ifadesi r ile bitiyormu diye kontrol eder True yada False döner

print(meessage)

#ÖRNEK
website="https://www.salihay.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

result="hello world".strip() #başındaki ve sonundaki boşlukları siler
result="www.salihay.com".strip("w.com") #başındaki ve sonundaki com u siler

result=course.lower()
result=course.upper()
result=course.title()   

result=website.count("a") #website içinde kaç tane a var
result=course.count("a",0,20) #course içinde 0 dan 20 ye kadar olan kısımda kaç tane a var

result=website.find("com") #com un başladığı indexi verir

result=website.startswith("www") #website www ile başlıyormu diye kontrol eder
result=website.startswith("https") #website https ile başlıyormu diye kontrol eder
result=website.endswith("com") #website com ile bitiyormu diye kontrol eder

result=course.isalpha() #course ifadesi sadece harflerden mi oluşuyor diye kontrol eder
result=course.isdigit() #course ifadesi sadece rakamlardan mı oluşuyor diye
result="12345".isdigit() #sadece rakamlardan oluşuyor
result="Hello".isalpha() #sadece harflerden oluşuyor

result="Contents".center(50,"*") #stringi 50 karaktere tamamlar ortalar ve boşlukları * ile doldurur

result=course.replace(" ","-") #boşlukları - ile değiştirir
result=course.replace("Python","Java") #Python kelimesini Java ile değiştirir

result=course.split() #kelimeleri boşluklardan ayırarak liste yapar
result=result[2] #liste elemanlarından 2. indexi alır

print(result)


#LİSTELER       
message="Hello There. My name is Salih Ay. "
print(message[0]) #liste elemanlarından 0. indexi alır

my_list=["Salih", 36, True, 3.14] #liste tanımlama
my_list=[1,2,3]
print(my_list)

list1=["one","two","three"]
list2=["four","five","six"]

numbers=list1+list2 #listeleri birleştirme
print(numbers)
print(len(numbers)) #listenin uzunluğunu verir
#ÖRNEK

arabalar=["bmw","mercedes","opel","mazda"]
result=len(arabalar) #listenin uzunluğunu verir

result=arabalar[0] #listenin 0. indexini verir
result=arabalar[-1] #listenin son elemanını verir

arabalar[-1]="toyota" #listenin son elemanını toyota ile değiştirir
result=arabalar

resullt="mercedes" in arabalar #mercedes listenin içinde varmı diye kontrol eder True yada False döner
resullt="suzuki" in arabalar #suzuki listenin içinde varm

result=arabalar[0:3] #0 dan 3 e kadar olan elemanları verir

arabalar[-2:]=["toyota","renault"] #listenin son 2 elemanını değiştirir
result=arabalar

result=arabalar+["audi","ferrari"] #listeye yeni eleman ekleme

del arabalar[-1] #listenin son elemanını siler
result=arabalar

result=arabalar[::-1] #listeyi ters çevirir

studentA=["Sadık","bilgi",2010,[70,60,70]]
studentB=["Salih","bilgi",2012,[80,80,70]]
studentC=["Ahmet","bilgi",2014,[80,70,90]]

resullt=studentA[3] #studentA listesinin 3. indexini verir
resullt=studentA[3][1] #studentA listesinin 3. indexinin 1. elemanını verir


result=f"{studentA[0]} {studentA[1]} {2024-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3} "

print(result)



numbers=[1,3,5,7,9]
letters=["a","b","c","d","e"]

val=min(numbers) #listenin en küçük elemanını verir
val=max(numbers) #listenin en büyük elemanını verir
val=min(letters) #alfabetik olarak en küçük elemanı verir
val=max(letters) #alfabetik olarak en büyük elemanı verir

val=numbers[3:6] #3 den 6 ya kadar olan elemanları verir
numbers[4]=13 #listenin 4. indexini 13 ile değiştirir

numbers.append(15) #listenin sonuna 15 ekler
numbers.insert(3,78) #3. indexe 78 ekler

numbers.pop() #listenin son elemanını siler
numbers.remove(3) #listeden 3 değerini siler

numbers.sort() #listeyi küçükten büyüğe sıralar
numbers.reverse() #listeyi ters çevirir

print(len(numbers))# listenin uzunluğunu verir
print(numbers.count(5)) #listede kaç tane 5 var

numbers.clear() #listenin tüm elemanlarını siler
print(numbers)
#ÖRNEK

names=["ali","yağmur","hakan","deniz"]
years=[1998,2000,1998,1987]

names.append("Cenk") #listenin sonuna Cenk ekler
names.insert(0,"Sena") #0. indexe Sena ekler
names.insert(len(names),"mehmet") #listenin sonuna mehmet ekler

names.remove("deniz") #deniz i listeden siler
print(names)

index=names.index("hakan") #hakan ın indexini verir
print(index) #hakanın olduğu indexi silmek için names.pop(index) de yazılabilir

result="ali" in names #ali isimli eleman listede varmı diye kontrol eder True yada False döner
result=names.index("ali") #ali nin indexini verir

print(result)

names.reverse() #listeyi ters çevirir

names.sort() #listeyi alfabetik olarak sıralar
years.sort() #listeyi küçükten büyüğe sıralar

print(names)
print(years)

str="Chevrolet,Dacia"
result=str.split(",") #virgülden ayırarak liste yapar
print(result)

min=min.years #listenin en küçük elemanını verir
max=max.years #listenin en büyük elemanını verir
print(min,max)

result=yaerss.count(1998) #listede kaç tane 1998 var
print(result)

years.clear() #listenin tüm elemanlarını siler
print(years)

markalar=[]
marka:input("Lütfen marka giriniz: ") # type: ignore #kullanıcıdan marka alır
markalar.append(marka) #markayı listeye ekler
print(markalar) 


#Dictionarys
#Key-Value (Anahtar-Değer) çiftlerinden oluşur

'''''''''
'''''''''
#dictionary kullanmadan yapılan örnek
sehirler=["kocaeli","istanbul"]
plakalar=[41,34]    
print(plakalar[sehirler.index("kocaeli")]) #kocaelinin plakasını verir

'''''''''
'''''''''
#dictionary ile yapılan örnek
sehirler={"kocaeli":41,"istanbul":34} #dictionary tanımlama
print(sehirler["kocaeli"]) #kocaelinin plakasını verir
print(sehirler["istanbul"]) #istanbulun plakasını verir

sehirler["ankara"]=6 #dictionarye yeni eleman ekleme
print(sehirler)

#ÖRNEK

users={
    "salihay":{
        "age":20,
        "roles":["user"],
        "email":"salihay@gmail.com",
        "address":"kocaeli",
        "phone":"1234567890"
    },
    "deniz":{
        "age":24,
        "roles":["admin","user"],
        "email":"deniz@gmail.com",
        "address":"istanbul",
        "phone":"1234567890"
}
 
 }
print(users) #tüm kullanıcıları yazdırır
print(users["salihay"]) #salihay kullanıcısının bilgilerini yazdır
print(users["deniz"]["email"]) #deniz kullanıcısının emailini yazdır


#ÖRNEK

ogrenciler={}
#1. öğrenci
number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci telefonu: ")

ogrenciler.update({
    number:{
        "name":name,
        "surname":surname,
        "phone":phone
    }
})
#2. öğrenci
number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci telefonu: ")

ogrenciler.update({
    number:{
        "name":name,
        "surname":surname,
        "phone":phone
    }
})
#3. öğrenci
number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci telefonu: ")

ogrenciler.update({
    number:{
        "name":name,
        "surname":surname,
        "phone":phone
    }
})

print("*"*50)

ogrNo=input("öğrenci no: ")
ogrenci=ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['name']} soyadı: {ogrenci['surname']} telefonu: {ogrenci['phone']}")

'''''''''''

