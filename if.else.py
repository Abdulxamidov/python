# 24/10/22
# 10-dars
# Mavzu:Tarmoqlanish 

# IF-ELSE

# ==
# !=
# >= , <=
# if ... or ...
# if ... or ...
# if ... or ... and ...
# if ... in ...
# if ... not in ...

# cars = ['audi','bmw','ferrari', 'tesla']
# for car in cars:
#    if car == 'bmw':
#        print(car.upper())
#    else:
#        print(car.title())


# ism = input("Salom ismingiz nima?\n>>>")
# if ism.lower() != 'ali':
#    print(f'Uzr {ism.title()}, biz Alini kutyapmiz!')
# else:
#    print('Salom, Ali')

# javob = float(input("6*7 nechchiga teng?\n>>>"))
# if javob == 42:
#    print("Javob to'g'ri!")
# else:
#    print("Javob xato!")

# yosh = int(input("Yoshingiz nechchida?\n>>>"))
# if yosh >= 18:
#    print('Xush kelibsiz!')
# else:
#    print('Sizga kirish mumkin emas!')

# login = input("Marhamat yangi login tanlang:")
# if len(login)<= 5:
#    print('5 tadan ko\'p  bo\'lishi kerak')
# else:
#    print("Qabul qilindi!")

# yosh = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2022-yosh > 18:
#   print("Xush kelibsiz!")
# else:
#    print(f"Yoshingiz {2022-yosh} da ekan")
#    print("sizga kirish mumkin emas")

# yosh = int(input("Yoshingiz nechchida?"))
# print("Siz grip uchun emlatki olishingiz kerak!") if yosh<10 else print("sizga emlatki shart emas")



# 25/10/22
# 11-dars

# IF-ELIF-ELSE

# yosh = int(input("Yoshingiz nechchida?:"))
# if yosh<=5:
#    narh = 0
# elif yosh<=10:
#    narh = 5000
# elif yosh<=20:
#   narh = 8000
# else:
#    narh = 10000
# print(f"Sizga kirish {narh} so'm.")


# IF ... OR ...

# kun = input("Bugun qaysi kun?\n>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    javob = 'dam olish'
# else:
#    javob = 'ish'
#print(f'Bugun {javob} kuni!')

"""
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' or kun.lower()== 'shanba' or kun.lower()== 'juma'  and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' or kun.lower()== 'shanba' or kun.lower()== 'juma' and harorat<30:
    print("Uyda dam olamiz!")    

 Boolean

 narh = 15000 # taom sotib oldi
 choy = True # choy sotib olgani haqida ma'lumot
 salat = True # salat sotib olmagani haqida ma'lumot
 if choy and salat:
    narh = narh+10000
elif choy or salat:
    narh = narh+5000
print(f"Jami {narh} so'm")

narh = 15000  # mijoz sotib olgan ovqatining narhi
choy = 1
non = 1
shirinlik = 1
kompot = 0
if choy:
    print("Mijoz choy oldi.")
    narh = narh + 5000
if non:
    narh = narh + 5000
if shirinlik:
    print("Mijoz shirinlik oldi.")
    narh = narh + 5000
if kompot:
    print("Mijoz kompot olkdi.")
    narh = narh + 5000
print(f"Jami summa {narh} so'm")


menu = ['manti' , 'osh', 'mastava', 'kabob','shashlik']
ovqat = input("Nima ovqat yeysiz?\n>>>")
if ovqat.lower() in menu: # not in buni aksini ko'rsatadi
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bu ovqat yo'q.")

menu = ['manti' , 'osh', 'mastava', 'kabob','shashlik']
buyurtmalar = ['xonim', 'osh', 'kabob','dimlama']
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor.")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q.")    
    if buyurtmalar:
        print(f"Ro'yxatda {len(taom)} ta taom bor")
    else:
        print("Ro'yxat bo'sh")
    

menu = ['manti' , 'osh', 'mastava', 'kabob','shashlik']
buyurtmalar = []
for taom in buyurtmalar:
    if taom in menu:
       print(f"Ro'yxatda {len(taom)} ta taom bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q.")    
else:
        print("Ro'yxat bo'sh")
"""