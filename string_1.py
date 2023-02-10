# 5-dars
# Mavzu: Stringlar 

# f-string
# ism = "Sardor"
# familiya = "Abdulxamidov"
# ism_familiya = f"{ism} {familiya}"
# print(ism_familiya) => Sardor Abdulxamidov

# Maxsus belgilar => \t , \n

# \t => uzun bo'shliq qoldiradi
# print("Hello \tWorld!") => Hello   World!

# \n => 2 qator qiladi
# print("Hello \nWorld!")
# Hello
# World!

# string metodlar => upper, lower, title, capitalize, lstrip, rstrip, strip

# ism = "sardor" 
# familiya = "abdulxamidov"
# ism_familiya = f"{ism} {familiya}"
# print(ism_familiya.upper()) # => SARDOR ABDULXAMIDOV (HAR BIR HARFNI KATTA BILAN YOZADI)
# print(ism_familiya.title()) #=> Sardor Abdulxamidov (So'z Boshini Katta Harflar Bilan Yozadi)
# print(ism_familiya.capitalize())# => Sardor abdulxamidov (Matn boshini katta harf bilan yozadi)

# meva = "     olma     "
# print('Men' , meva , 'ni yaxshi ko\'raman') => Men      olma      ni yaxshi ko'raman
# print('Men' , meva.lstrip() , 'ni yaxshi ko\'raman') => Men olma      ni yaxshi ko'raman
# print('Men' , meva.rstrip() , 'ni yaxshi ko\'raman') => Men      olma ni yaxshi ko'raman
# print('Men' , meva.strip() , 'ni yaxshi ko\'raman') => Men olma ni yaxshi ko'raman

# ism = input("Salom ismingiz nima?")
# print('Assalomu alaykum,', ism)

# ism = input("Salom ismingiz nima?\n>>>")
# print('Assalomu alaykum,' ,ism.title()) 

# Vazifa 

# kocha="Mehnatobod"
# mahalla="Zarg'aldoq"
# tuman="Buloqboshi" 
# viloyat="Andijon"
# print(kocha , 'ko\'chasi,' , mahalla , 'mahallasi,' , tuman , 'tumani,' , viloyat , 'viloyati.')
# Natija => Mehnatobod ko'chasi, Zarg'aldoq mahallasi, Buloqboshi tumani, Andijon viloyati

# 6-dars. Sonlar

# ism = 'Sardor'
# yosh = 19
# xabar = ism + ' ' + str(19) + ' yoshda'
# print(xabar)

# t_yil = int(input("Tug'ilgan yilingizni kiriting! "))
# yosh = 2022 - t_yil
# print("siz", yosh , "yoshda ekansiz")
 
# Vazifa

# son = int(input("Istalgan sonni kiriting! ")) butun sonlarni hisoblaydi
# son = float(input("Istalgan sonni kiriting! ")) qoldiq sonlarni hisoblaydi
# kvadrat = son**2
# kub = son**3
# print(son , 'ning kvadrati' ,kvadrat)
# print(son , 'ning kubi' , kub)
# Natija:
# 3 ning kvadrati 9
# 3 ning kubi 27