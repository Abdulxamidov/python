# 22.10.22
# 7(8)-dars  
# Mavzu: list

# index - matn ichidagi buyumlar tartib raqami => 0,1,2 ... deb sanaladi
# __.APPEND('  ') - matn oxriga qo'shadi
# ___.INSERT(index, '...') - istagan joyga qo'shadi 
# DEL ...[0]  - matn ichidan tanlanganini o'chirib tashlaydi 
# ___.REMOVE('...') - matn ichidagi buyum(raqamni) nomini yozsa o'chirib tashlaydi (index ni bilmasa) 
# ___ = ___.POP() - o'zgaruvchi matni ichidan bir buyumni boshqa o'zgaruvchi matniga oladi 
# .SORT() - matn ichidagi ro'yxatni bosh harf va kichik harflar kesimida alifbo tartibida teradi,raqamlarga ham tegishli
# SORT(reverse=True) - sortni aksi
# (sorted(...)) - asl ro'yxatga tegmagan holda matnni o'zgartirib chiqaradi, sort bilan bir xil
# (sorted(... , reverse=True))  
# REVERSE() - bu metod shunchaki matnni oxiridan boshiga qarab o'rnini o'zgartirib qo'yadi xolos
# list(RANGE(... , ...)) - ma'lum belgilangan raqamlar orasidagi sonlarni listga chiqaradi
# ___.MAX(...) - ro'yxat ichidan eng katta qiymatni aniqlaydi
# ___.MIN(...) - kichigini aniqlaydi
# SUM(...) - umumiy hisobni chiqarib beradi
# ... = ...[:] - matn bilan bir xil qilib ko'chirib oladi
# TUPLE - o'zgarmas ro'yxat                             
# print(LEN(...)) - matn ichida nechta buyum borligini sanaydi  

# ro'yxat ichidagi har bir narsa 0 dan boshlab sanaladi (0,1,2,3,4) 

# mevalar = ['olma' , 'anor' , 'bexi' , "o'rik"]
# print(mevalar) => ['olma', 'anor', 'bexi', "o'rik"]
# print(mevalar[0]) => olma
# print(mevalar[3]) => o'rik
# print(mevalar[0].upper()) => OLMA
# mevalar[0] = 'banan' 
# print(mevalar) => ['banan', 'anor', 'bexi', "o'rik"]
# mevalar.append('tarvuz') - oxirgi qatoriga tarvuzni qo'shib qo'ydi
# print(mevalar) => ['olma', 'anor', 'bexi', "o'rik", 'tarvuz']
# mevalar = ['olma' , 'anor' , 'bexi' , "o'rik"]
# mevalar.insert( 2, 'anjir')
# print(mevalar) => ['olma', 'anor', 'anjir', 'bexi', "o'rik"]
# sanashda manfiy sonlar bilan sanash ham mumkin lekin unda matn oxiridan boshlab hisoblanadi
# print(mevalar[-1]) => o'rik
# print(mevalar[-4]) => olma

# narxlar = [18000, 19000, 24000, 30000]
# print(narxlar) => [18000, 19000, 24000, 30000]
# print([narxlar[0]+ narxlar[1]]) => [37000]

# sonlar = ['bir' , 'ikki' , 3, 4, 5]
# print(sonlar) => ['bir', 'ikki', 3, 4, 5]

# ismlar = [ ]   bo'sh qoldirish ham mumkin
# print(ismlar) => []

# cars = []
# cars.append("\"malibu\"") => "malibu" qo'shtirnoq bilan chiqadi
# print(cars[0].title()) => "Malibu"
# cars.append('matiz')
# cars.append('tico')
# print(cars) => ['malibu', 'matiz', 'tico']
# del cars[0] - ro'yxat ichidan tanlaganingni o'chirib tashlaydi:
# print(cars) => ['matiz', 'tico']
# cars.insert(0 , 'Nexia-3') - matn boshiga qo'shib qo'ydi:
# print(cars) => ['Nexia-3', 'matiz', 'tico']
# cars.remove('matiz') - ro'yxatdan keraksiz ma'lumotni nomini yozsa o'chirib tashladi
# print(cars) => ['tico']

# hayvonlar = ['it' , 'mushuk' , 'qo\'y' , 'sigir' , 'it' , 'quyon']
# print(hayvonlar) => ['it', 'mushuk', "qo'y", 'sigir', 'it' , 'quyon']
# hayvonlar.remove('it') - ro'yxat ichidan faqat 1-duch kelgan 'it' ni o'chiradi , keyingi o'rindagi 'it' lar qoladi
# print(hayvonlar) => ['mushuk', "qo'y", 'sigir', 'it', 'quyon']
# gosht_uchun = hayvonlar.pop(5) - quyon hayvonlar listidan gosht_uchun listiga o'tib qoladi
# print(gosht_uchun) => quyon 
# print(hayvonlar) => ['it', 'mushuk', "qo'y", 'sigir', 'it']

# bozorlik = ['guruch', 'un' , 'yog\'' ,'piyoz', 'konfet']
# mahsulot = bozorlik.pop(2)
# print('Men' + ' ' + mahsulot + ' ' + 'sotib oldim') => Men yog' sotib oldim
# print('Qolgan narsalar: ' ,  bozorlik) => Qolgan narsalar:  ['guruch', 'un', 'piyoz', 'konfet']

# taomlar = ['Osh' , 'Dimlama' , 'Mastava']
# suyuq_ovqat = taomlar.pop()
# print(suyuq_ovqat) => Mastava
# print(taomlar) => ['Osh', 'Dimlama']
 



# 23/10/22
# 8-dars
# Mavzu: Lists

# cars = ['matiz' , 'onix' , 'nexia' , 'malibu' , 'Ferrari' , 'bmw' , 'audi']
# cars.sort()
# print(cars) => ['Ferrari', 'audi', 'bmw', 'malibu', 'matiz', 'nexia', 'onix'] -
# cars.sort(reverse=True)
# print(cars) => ['onix', 'nexia', 'matiz', 'malibu', 'bmw', 'audi', 'Ferrari']
# print(sorted(cars)) => ['Ferrari', 'audi', 'bmw', 'malibu', 'matiz', 'nexia', 'onix']
# cars.reverse() => ['audi', 'bmw', 'Ferrari', 'malibu', 'nexia', 'onix', 'matiz']



# sonlar = [12,20,10,7,-3,4.5,-8.2]
# sonlar.sort() => [-8.2, -3, 4.5, 7, 10, 12, 20]
# sonlar.sort(reverse=True) => [20, 12, 10, 7, 4.5, -3, -8.2]
# print(sonlar) 

# sonlar = list(range(0,10)) => print(sonlar) ===> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# son = list(range(21,22))  => print(son) => [21]
# juft_sonlar = list(range(0,20,2)) => print(juft_sonlar) =>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# narxlar = [5000,12000,3500,24000,10000,32000]
# max_qiymat = max(narxlar) 
# min_qiymat = min(narxlar)
# umumiy_qiymat = sum(narxlar) 
# print('bugungi bozorlikdagi eng arzon tovar' , min_qiymat , ',eng qimmati' , max_qiymat , ',hammasi bo\'lib' , umumiy_qiymat )
# Natija => bugungi bozorlikdagi eng arzon tovar 3500 ,eng qimmati 32000 ,hammasi bo'lib 86500
# print(narxlar[0:3]) => [5000, 12000, 3500]
# print(narxlar[0:]) => [5000, 12000, 3500, 24000, 10000, 32000]
# skidka = narxlar[:] => ko'chirib oldi
# skidka.remove(12000) => print(skidka)  =>[5000, 3500, 24000, 10000, 32000]

# toys = ('bear' , 'car' , 'teddy' , 'bigo' , 'moto') #=> print(type(toys))  ->  tuple o'zgarmas ro'yxat
# toys.append('bubu')  => print(toys) => 'tuple' object has no attribute 'append' -> qo'shib bo'lmadi
# toys = list(toys) => print(type(toys)) => <class 'list'> => 'list'  ya'ni o'zgaruvchan matnga aylandi
# toys.append('bubu') => print(toys) => ['bear', 'car', 'teddy', 'bigo', 'moto', 'bubu'] => 'bubu' so'zi qo'shildi
# toys = tuple(toys) => print(type(toys)) => <class 'tuple'>  ==> 'tuple' yana o'zgarmas matnga aylandi
# print(len(toys)) => 6