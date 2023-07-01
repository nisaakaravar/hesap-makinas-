# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:47:09 2023

@author: Hayrunnisa
"""

giris="""
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini al
(6) karekökünü al
"""
print(giris)

anahtar=1

while anahtar==1:
    
    soru=input("yapmak istediğiniz işlemin numarasını giriniz(çıkmak için q tuşunu pressleyiniz.)")
    
    if soru=="q":
        print("programdan çıkılıyor")
        anahtar=0

    elif soru=="1":
        sayi1=int(input("birinci sayıyı giriniz:"))
        sayi2=int(input("ikinci sayıyı giriniz:"))
        print(sayi1,"+",sayi2,"=",sayi1+sayi2)
        
    elif soru=="2":
        sayi1=int(input("biirnci sayıyı giriniz:"))
        sayi2=int(input("ikinci sayıyı giriniz:"))
        print(sayi1,"-",sayi2,"=",sayi1-sayi2)
        
    elif soru=="3":
        sayi1=int(input("birinci sayıyı giriniz:"))
        sayi2=int(input("ikinci sayıyı giriniz:"))
        print(sayi1,"*",sayi2,"=",sayi1*sayi2)
    
    elif soru=="4":
        sayi1=int(input("birinci sayıyı giriniz:"))
        sayi2=int(input("ikinci sayıyı giriniz:"))
        print(sayi1,"/",sayi2,"=",sayi1/sayi2)
        
    elif soru=="5":
        sayi1=int(input("sayıyı giriniz:"))
        print(sayi1,"karesini al", sayi1**2)
        
    elif soru=="6":
        sayi1=input("sayıyı giirniz:")
        print(sayi1,"karekökünü al",sayi1**0.5)
        
    else:
        print("Yanlış sayı girdiniz.")
        print("lütfen 1-6 arasında bir değer giirniz.")
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    