import math as m
import numpy as np

vertices = np.array([])

#[x, y, z]
#sensör verilerinden aldığımız x,y,z koordinatlarını önce boş bir diziye atayacağız 

dizi = []

#bunun için de for döngüsü içerisinde gelen verileri append edeceğiz
dizi.append([2, 5, 9])

#burada append ettiğimiz koordinatlar dilimleme algoritmasına sokulacak olan köşeler
#yukarıdan 0 ile başlayıp artarak aşağı inecek
dizi.append([3, 8, 10])
dizi = np.array(dizi)
print(dizi)
print(len(dizi))
veri_miktar = np.zeros(200)

dilimler = []

dilimler.append([4, 8])
dilimler.append([9, 14])
dilimler.append([8, 15])

print("DILIMLER")
print(dilimler[0][1])
#dilimlemeyi de bir dilimleme algoritması ile buna otomatik append ederek yaptıktan sonra bunu da yukarıda ki gibi numpy dizisine dönüştüreceğiz
#köşeleri atamak bir nebze kolay burada sıkıntılı kısım dilimleme algoritmasının gerçeklenmesi
#sonuç olarak o algoritma aracılığı ile dilimleme otomatik yapılmalı

#KÖŞELERİ BELİRLEME
#sensör protokolünde x point z value diye gidiyor
#bizim burada x pointimiz z oluyor
#x olanda 1.8 derecelik açı sonucu trigonometrik eşitlikler ile bulunacak
#z value de y oluyor yani en azında başta
#döndükçe y eksenindeki uzaklıkta trigonometrik eşitlikler ile bulunacak

#sağa +x, bana doğru +y, yukarı doğru +z

#köşe belirleme kolay ancak dilimleme kısmında en büyük sorunu aynı veri sayısına sahip olmayan ölçümler oluşturacak gibi



k = m.sin(30*(2*m.pi/360))
l = m.sin(m.radians(30))
print(dizi)