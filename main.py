# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from random import randint


rand=randint(1,101) #RASTGELE SAYI ATMASI İÇİN RANDİT KULLANDIK
sayac=0
while True:  #SONSUZ DÖNGÜYE GİRMESİ İÇİN TRUE KULLANDIK

    sayac += 1
    sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))

    if (sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi<rand:
        print("daha büyük bir sayı giriniz")
        continue
    elif sayi>rand:
        print("daha küçük sayı giriniz")
        continue
    else:
        print("rasgele seçilen sayı",format(rand))
        print("sizin seçtiğiniz sayı",sayi)

    sayaclar = [sayac]

    for sayac in sayaclar:
         print("denen tüm sayılar", sayac)


        

