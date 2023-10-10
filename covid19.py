"""
Covid-19 test kiti 
author @noah
"""
import time 
while True:
    ad=input("İsminiz:")
    soyad=input("Soyadınız:")
    yas=int(input("Yaşınız:"))

    kangrubu = input("Kan Grubunuz:")
    covidtespit = input("Tahlilde bulunan özellikleri yazınız:") 
    covidarraty = "0x0" #bu özellik hastada varsa covid-19 + dir
    print("AD:",ad ,"SOYAD:",soyad ,"YAŞ:",yas ,"KAN GRUBU:",kangrubu)
    print("SONUÇLAR..")
    time.sleep(2)
    if kangrubu == "0"   and covidtespit == "0x0":
        print("Covid-19 test sonucu +")
    elif  kangrubu =="A" and covidtespit == "0x0":
        print("Covid-19 test sonucu pozitif")
    elif kangrubu=="B" and covidtespit == "0x0":
        print("Covid-19 test sonucu pozitif")
    elif kangrubu=="AB" and covidtespit == "0x0":
        print("Covid-19 test sonucu pozitif")
    else:
        print("Covid-19 test sonucu -")
    cikis = input("İşleme devam etmek istiyorsanız + istemiyorsanız - ")
    if cikis == "+":
        print("Teste devam")
    else:
        print("Çıkılıyor")
        break
