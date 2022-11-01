"""
27.10.22
14-dars
Mavzu: Dictionary-Lug'at
Sardorbek Abdulxamidov
"""

# .items() - lug'at ichidagi kalit(key) va qiymat(value) ni alohida chiqarib beradi
# .keys() - lug'atdagi kalitlarni ko'rsatadi
# .values() - Lug'at ichidagi qiymatni ko'rsatadi
# set() - lug'at ichidagi bir xil qiymatni 1 ta qiladi
# set - ma'lumot turi 
"""
car_0 = {'model' : 'ferrari', 'rang': 'qizil'}
print(car_0['model'])
print(car_0['rang'])
"""

"""
eng_uz = {'apple': 'olma', 'cherry':'gilos','grape':'uzum'}
print(eng_uz['apple'])
print(eng_uz['cherry'])
print(eng_uz['grape'])


mevalar = {'olma':10000,'gilos':8000, 'uzum':5000}
print(f"Olmaning narxi {mevalar['olma']} so'm")  # => Olmaning narxi 10000 so'm
"""

"""
talaba_0 = {'ism':'karim zokirov','yosh':20,'t_yil':2002}
print(f"{talaba_0['ism'].title()},\
    {talaba_0['t_yil']}-yilda tug'ilgan,\
    {talaba_0['yosh']} yoshda")
# Lug'at ichiga yangi qiymat qo'shish
talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'IT'
print(talaba_0) # => {'ism': 'karim zokirov', 'yosh': 20, 't_yil': 2002, 'kurs': 4, 'fakultet': 'IT'} yangi ma'lumot qo'shildi
talaba_0['ism'] = 'Akmal' # => print(talaba_0) =>{'ism': 'Akmal', 'yosh': 20, 't_yil': 2002, 'kurs': 4, 'fakultet': 'IT'}
"""

"""
talaba_1 = {} # bo'sh ro'yxat , foydalanuvchi tomonidan to'ldiriladi
talaba_1['ism'] = 'karim odilov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(f"Talaba {talaba_1['ism'].title()},\
{talaba_1['kurs']}-kursda o'qiydi,\
{talaba_1['yosh']} yoshda.") # => Talaba Karim Odilov,3-kursda o'qiydi,20 yoshda.
talaba_1['kurs'] = 4 # QIYMAT O'ZGARDI
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda o'qiydi.") # => Talaba Karim Odilov 4-kursda o'qiydi.

talaba_0 = {'ism':'karim zokirov','yosh':20,'t_yil':2002}
del talaba_0['yosh']  # YOSH ma'lumoti o'chirib tashlandi
print(talaba_0) # => {'ism': 'karim zokirov', 't_yil': 2002}
"""

"""
telefonlar = {
    'Ali' : 'Iphone x',
    'Vali' : 'Galaxy A50',
    'Olim' : 'Nokia 1210',
    'Sardor' : 'Iphone 11 pro'
    }
print(telefonlar) # => {'Ali': 'Iphone x', 'Vali': 'Galaxy A50', 'Olim': 'Nokia 1210', 'Sardor': 'Iphone 11 pro'}
# print(telefonlar['Ali'])  => Iphone x

phone = telefonlar.get('husan','Bunday ism mavjud emas')
print(phone) # => Bunday ism mavjud emas
# phone = telefonlar.get('husan') => agar bo'sh qoldirsak => None   degan javob chiqdi 
"""

# 29.10.22
# 15-dars
# Mavzu:Lug'atlar bilan ishlash 

"""
talaba_0 = {'ism':'karim zokirov',
    'yosh':20,
    't_yil':2002,
    'manzil':'Andijon',
    'kurs':4
    }  
# print(talaba_0.items()) =>([('ism', 'karim zokirov'), ('yosh', 20), ('t_yil', 2002), ('manzil', 'Andijon'), ('kurs', 4)])

for kalit,qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}\n")

Kalit: ism
Qiymat: karim zokirov

Kalit: yosh
Qiymat: 20

Kalit: t_yil
Qiymat: 2002

Kalit: manzil
Qiymat: Andijon

Kalit: kurs
Qiymat: 4
"""

"""
telefonlar = {
    'Ali' : 'Iphone x',
    'Vali' : 'Galaxy A50',
    'Olim' : 'Nokia 1210',
    'Sardor' : 'Iphone 11 pro'
    }
for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

Alining telefoni Iphone x
Valining telefoni Galaxy A50
Olimning telefoni Nokia 1210
Sardorning telefoni Iphone 11 pro
"""
"""
mevalar = {'olma':10000,
    'gilos':8000, 
    'uzum':5000}
# print(mevalar.keys())  # => (['olma', 'gilos', 'uzum'])
# print(mevalar.values()) # => ([10000, 8000, 5000])

print("Do'kondagi mevalar:")
for meva in mevalar.keys():
    print(meva.title())
Do'kondagi mevalar:
Olma
Gilos
Uzum
"""
"""
mevalar = {'olma':10000,'gilos':8000, 'uzum':5000}
bozorlik = ['olma','non','go\'sht','uzum']                                         
for meva in mevalar:
    if meva in bozorlik:
        print(f"{meva.title()} {mevalar[meva]}so'm")
for buyum in bozorlik:
    if buyum not in mevalar:
        print(f"Iltimos do'koningizga {buyum} ham olib keling!")

- Natija:
Olma 10000so'm
Uzum 5000so'm
Iltimos do'koningizga non ham olib keling!
Iltimos do'koningizga go'sht ham olib keling!
"""

# mevalar = {'olma':10000,'gilos':8000, 'uzum':5000}
# print(mevalar.keys()) => (['olma', 'gilos', 'uzum'])
# print("Do'kondagi mevalar:")
# for meva in sorted(mevalar):
#     print(meva.title())
# Natija:
#   Do'kondagi mevalar:
# Gilos
# Olma
# Uzum  

"""
telefonlar = {
    'Ali' : 'Iphone x',
    'Vali' : 'Galaxy A50',
    'Olim' : 'Nokia 1210',
    'Sardor' : 'Iphone 11 pro'
    }
# print(telefonlar.values()) => (['Iphone x', 'Galaxy A50', 'Nokia 1210', 'Iphone 11 pro'])
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefonlar.values():
    print(tel)
"""
"""
telefonlar = {
    'Ali' : 'Iphone x',
    'Vali' : 'Galaxy A50',
    'Olim' : 'Nokia 1210',
    'Sardor' : 'Iphone 11 pro',
    'Karim' : 'Iphone x',
    'Mutal' : 'Galaxy A50',
    'Zoir' : 'Iphone x'
    }
for tel in set(telefonlar.values()):  #set() - bunda takrorlanib kelgan ma'lumot 1 ta qilinadi 
    print(tel)
"""


# SET MA'LUMOT TURI
# toys = {"ball", "toy" , "doll","car","ball"}
# print(type(toys)) # =>  <class 'set'> 
# print(toys)  

