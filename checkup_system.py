check_up = input("Merhaba, Check-Up yapmak ister misiniz?").lower() 
if check_up == "evet":

    boy = float(input("Boyunuzu giriniz"))
    kilo = float(input("Kilonuzu giriniz"))
    bmi = kilo / (boy * boy)

    print(f"Beden Kitle Endexiniz {round(bmi,1)}")

if bmi >= 40 :

    print("Dikkat Morbid Obezite")

elif bmi >= 30 :

    print("Dikkat Obezite")

elif bmi >= 25 : 

    print("Dikkat Obezite Riski")

elif bmi >= 18.5 : 

    print("İyi bir bmi sahipsiniz")

else: 

    print("Çok Zayıfsınız")

ates_olcumu = input ("Ateş ölçümü yapmak ister misiniz?").lower()

if ates_olcumu == "evet" : 
    sicaklik = float(input("Ateşinizi Giriniz")) 

if sicaklik >= 38 :

    print("Dikkat yüksek ateş")

elif sicaklik >= 37 : 

    print("Hafif Ateş")

elif sicaklik >= 36 : 

    print("Normal Ateş")

else :

    print("Düşük Ateş")

sonuc = input("Başarı ile ölçümlerinizi yaptınız sonuçları ekranda görmek ister misiniz ? ").lower()

if sonuc == "evet" : 

    print(round(bmi,1),sicaklik)


    







