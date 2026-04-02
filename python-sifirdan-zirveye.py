# region Dərs 1 Print

# print ("Ferid","Vaqifzade", sep=" +-+")

"""print ("Salam", "Ferid", end=" ")
print ("Sag ol")"""

'''print (""" salam, necesen? 
       Dunen seni gordum.
       Her sey yaxsidi?
       """)'''

# endregion

# region Dərs 2 Dəyişənlər
"""x = 4
y = 5
z = 6

a,b,c = 1,2,3

a=b=c=3

print(a,b,c)

print(x,y,z)"""

"""a = 10
b = 50

print("Evvel:" ,a,b)

a,b = b,a 

print("Sonra :", a,b)"""

# endregion

# region Dərs 3 Data Types - Məlumat tipləri

# integer - int tipi
"""x = 50
print(x)

# burada type dəyişənin tipini ekrana çıxardır
print(type(x))"""

# float
"""y = 1.09
print(y)
print(type(y))"""

# string -str
"""z="soz"
print(z,":", type(z))"""

# boolean - bool

"""d = True
print(d,type(d))
"""


# endregion

# region Dərs 4 Riyazi operatorlar

# // iki dənə bölmə işarəsi ilə ədədləri bölərkən cavabda yalnız tam hissəni göstərəcək
# % işarəsi ilə bölgü edərkən cavab kimi qalıq hissəni verir.
# ** ədədi qüvvətə yüksəldir

# print(5/2)
# print(5//2)
# print(17%2)
# print(2**3)

# hər hansı bir dəyişənin dəyərini artırmaq üçün 2 yoldan istifadə etmık olar.
# biz x dəyişənini x=x+5 və x+=15 kimi iki fərqli yolla artırdıq

# x = 10
# x = x + 5
# x += 15
# print(x)


# endregion

# region Dərs 5 String

# Burda biz indeksləmə etmişik. Beləki, Azerbaycan sözünün (0 1 2 3 4 5 6 7 8 9 ) indeks
# içərisində istənilən hərfini ekrana yazırıq              (A z e r b a y c a n )

# olke = "Azerbaycan"
# print(olke, olke[2])

# Burda biz indeksləməni 0-cı yerdən 3-cü yerədək ekrana yazırıq, baxmayaraq ki, [0:4]
# aralığını seçmişik.
# olke = "Azerbaycan"
# print(olke[0:4])

#  Qeyd: əvvələ 0 yazmasaq da 0-cıdan sayaraq hesablayacaq və ya əksi də ola bilər.

# olke = "Azerbaycan"
# print(olke[:5])
# print(olke[4:])

# Geridən də saya bilərik. O zaman mənfi (-) işarəsindən istifadə edirik

# olke = "Azerbaycan"
# print(olke, olke[-1])

# Bir sözün uzunluğunu bilmək üçün len (length) - dən istifadə edirik.

# olke = "Azerbaycan"

# print(len(olke))

# String-lərin metodları: metodlardan istifadə etmək üçün nöqtədən (.) istifadə edirik.
# Beləki s dəyişəninin metodlarını cağırmaq üçün s-dən sonra nöqtə qoyuruq.

# s="Python"
# print(s.upper())
# print(s.lower())
# print(s.strip()) # bu metod sağda və solda olan boşluqları silir.
# print(s.replace("n", "z")) # bu metod əvəzedici metoddur.
# print(s.capitalize()) # ilk hərifi böyük yazır ekrana
# print(s.count("y")) # sözün içində olan hər hansı bir hərfin sayını ekrana çıxardır
# print(s.find("t")) # bu metod t hərifinin indeksini göstərir.Python sözündə neçənci yerdədir
# print(s.isdigit()) # bu metod s dəyişənin dəyərinin ədəd olduğunu yoxlayır, ona görə də
# ekrana False çıxardacaq çünki s-in dəyəri string-dir

# print(s.isalpha()) # bu metod dəyişənin dəyərinin əlifbada olub olmadığını yoxlayır.
# Nəticə: True


# Bu metodda .format(ad, soyad) o demekdir ki, biz {}{} bu fiqurlu moterizelere
# arqument (ad, soyad deyisenlerini) gonderirik
# Qeyd: "Salam, {} {}" - bu ozu bir string oldugu ucun bundan sonra noqte (.) qoyub metod
# cagiririq, yeni .format() metodunu

# ad = "Ferid"
# soyad = "Vaqifzade"

# print("Salam, {} {}".format(ad, soyad))

# # ikinci format metodu. f vasitesi ile olur. burda f hem kicik hem de boyuk F ola biler

# print(f"Salam, {ad} {soyad}")


# cumlenin icinde her hansi bir sozu dirnaq icinde yazmaq isteyende \"\" isaresinden
# istifade edirik

# cumle = "Python hemcinin \"Piton\" olaraq da adlandirilir"
# print(cumle)


# endregion

# region Type Conversion - Tip Cevirmeleri

# interger - float (kesr ededini) interger (tam edede) cevrilmesi
# a = 1.15
# print(int(a))
# print(a)

# b =1.55
# b= int(b)
# print(b, type(b))

# endregion

# region Input - Istifadeci girishi

# ad =input("Adinizi daxil edin: " )

# print("Salam, " + ad)
# print("Salam,", ad)

# Python-da print funksiyasının daxilindəki f hərfi
# "Formatted String" (Formatlanmış sətir) deməkdir.
# Buna qısaca f-string deyilir
# (Dırnağı bir dəfə açırsan, dəyişəni isə birbaşa { }
# (fiqurlu mötərizə) daxilində yazırsan).
# print(f"Salam, {ad}")

# print(type(ad))

# eded = input("Eded daxil edin: ")

# print(int(eded) * int(eded))
# print(int(eded) ** 2)

# eded = int(input("Eded daxil edin: "))
# print(eded ** 2)

# endregion

# region List (Array) data type - List (Massiv) melumat novu
# Listler ozunde diger tiplerden olan melumatlari saxlaya bilir

# alinacaqlar_listi = ["Kartof", "Sogan", "Nar", "Pomidor", 10, True, "Nar"]

# print(alinacaqlar_listi)
# indeksler    0       1       2       3         4
# meyveler = ["alma", "heyva", "nar", "armud", "portagal"]

# # print(meyveler[:])
# print(meyveler[2])

# s = "Python"
# print(s[:])

# burda meyveler listin icincdeki sonuncu portagal elementini kivi elementine deyisirik
# meyveler[-1] = "kivi"

# print(meyveler[:])

# Append metodu ile biz listlere yeni elementler elave ede bilerik
# meyveler.append("Kivi")
# print(meyveler)

# Insert de listlere yeni elementler elave etmek ucundur sadece append-den bir ferqi var
# Insert-de konkret olaraq hansi yere elave etmeyi bildirmek olar. Append-de ise yalniz
# listin sonuna elave edir

# meyveler.insert(2, "Yeni Elemenet")

# Remove - metodu elementleri silmek ucundur
# meyveler.remove("nar")

# Pop-da element silmek ucundur sadece index uzre
# meyveler.pop(2)

# print(meyveler)

# ededler = [5, 4, -12, 100, 905, 23, 1]

# .Sort metodu elementleri kicikden boyuye dogru siralayir
# ededler.sort() /*DAHA ETRAFLI PYTHON-QEYDLER WORD FALINDA*/

#  Sorted funksiyasi da elementleri kicikden boyuye dogru siralayir
# /*DAHA ETRAFLI PYTHON-QEYDLER WORD FALINDA*/
# ededler = sorted(ededler)


#  Sort(reverse=True) metodu elementleri boyukden kiciye dogru siralayir
# ededler.sort(reverse=True)
# ededler = sorted(ededler, reverse=True)

# print(*ededler)

# Listlerin birleshdirilmesi

# a = [1,2,3]
# b = [4,5,6]
# c = a+b
# print(*c)


# 1-lerden ibaret 5 eded 1 ededini cap edecek
# a=[1]*5
# print(*a)

# a = [1,2,3,4,5]

# Clear metodu listin icini temizleyir
# print(a)
# a.clear()
# print(a)

# Count metodu massivin icindeki elementlerin tekrarlanan sayini sayir
# print(a.count(2))

# Index metodu listin icindeki elementin yerlesdiyi indexi gosterir

# print(a.index(3))

# Reverse metodu listi tersine cevirir
# a.reverse()

# a = list(reversed(a))


# print(a)

# endregion

# region Matrix - 2 olculu siyahilar matrix adlanir
# Elementler: 0          1
# list1 = [[1, 2, 3], [4, [5, 6]]]
# # Elementler:        0     1
# # Element:0  1  2    0   0  1
# # Python-da siyahının (list-in) daxilində neçə element olduğunu bilmək üçün
# # len() (length - uzunluq) funksiyasından istifadə olunur.
# print("Listin icerisindeki element saylari:", len(list1))
# print("Sifirinci elementin 2-ci elementi:", list1[0][2])
# print("Birinci elementin 0-ci elementi:", list1[1][0])
# print("Birinci elementin icerisindeki 1ci elementin 0-ci elementi:", list1[1][1][0])

# # Listin icinde matrixler
# list2 = [(1, 2, 3), (4, 5, 6)]
# print(list2[0][2])

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][2])
# print(matrix[1][0])

# endregion

# region Tuple melumat novu / 2.35.39 /


# endregion
