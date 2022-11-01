# 23/10/22
# Mavzu: FOR LOOP

# for ... in ... - matn ichidagi har bir narsa uchun 

# mexmonlar = ['Ali','Vali'] # print('Salom' , mexmonlar[1]) => Salom Vali
# for mexmon in mexmonlar:
#    print('Salom,',mexmon)
#    print('Hayr,' , mexmon)
# Natija:
# Salom, Ali
# Hayr, Ali
# Salom, Vali
# Hayr, Vali

# mexmonlar = ['Ali', 'Vali' , 'Olim' , 'Guli']
# for mexmon in mexmonlar:
#    print(f'Assalomu alaykum xurmatli {mexmon} sizni va oila a\'zolaringizni 25-oktabr kuni naxorgi oshka taklif qilamiz')
#    print('Xurmat ila Xorinovlar oilasi\n')
# Natija
# Assalomu alaykum xurmatli Ali sizni va oila a'zolaringizni 25-oktabr kuni naxorgi oshka taklif qilamiz
# Xurmat ila Xorinovlar oilasi

# sonlar = list(range(2,10))
# for son in sonlar:
#    print(f'{son} ning kvadrati {son**2} ga teng')
# Natija
# 2 ning kvadrati 4 ga teng
# 3 ning kvadrati 9 ga teng

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#   sonlar_kvadrati.append(son**2)
# print(sonlar) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# print(sonlar_kvadrati) # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting:"))
# print(dostlar)  

# Vazifa
# toq_sonlar = list(range(11,100,2))
# for kub in toq_sonlar:
#   print(kub**3)