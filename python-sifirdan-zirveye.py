#region Dərs 1 Print 

# print ("Ferid","Vaqifzade", sep=" +-+")

"""print ("Salam", "Ferid", end=" ")
print ("Sag ol")"""

'''print (""" salam, necesen? 
       Dunen seni gordum.
       Her sey yaxsidi?
       """)'''

#endregion 

#region Dərs 2 Dəyişənlər 
'''x = 4
y = 5
z = 6

a,b,c = 1,2,3

a=b=c=3

print(a,b,c)

print(x,y,z)'''

'''a = 10
b = 50

print("Evvel:" ,a,b)

a,b = b,a 

print("Sonra :", a,b)'''

#endregion 

#region Dərs 3 Data Types - Məlumat tipləri

# integer - int tipi
'''x = 50
print(x)

# burada type dəyişənin tipini ekrana çıxardır
print(type(x))'''

# float
'''y = 1.09
print(y)
print(type(y))'''

# string -str
'''z="soz"
print(z,":", type(z))'''

# boolean - bool

'''d = True
print(d,type(d))
'''


#endregion

#region Dərs 4 Riyazi operatorlar

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


#endregion

#region Dərs 5 String

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

s="Python"
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

# 1:46:57 - Ilkin tip cevirmeleri movzusunda qaldim












#endregion



















