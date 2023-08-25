# # 1-code
# en_uz = {'apple':'olma','key':'kalit','car':'mashina','bear':'ayiq','value':'qiymat'}
# for key,value in en_uz.items():
#     print(f'{key}-{value}')

# # 2-code
# d_p = {"O'zbekiston":'Toshkent',"Amerika":'    New york',"Rossiya":'    Moskva'}
# print(f'Dunyo davlatlari:           Davlat poytaxtlari:')
# for key,value in d_p.items():
#     print(key + "                  "    +   value)

# # 3-code
# d_p = {"Uzbekiston":'Toshkent',"Amerika":'New york',"Rossiya":'Moskva'}
# dav = str(input('Iltimos davlat nomini kiriting:').title())
# if dav in d_p.keys():
#     print(f'{dav} poytaxti {d_p[dav]}')
# else:
#     print("Kecharasiz,bizda bu haqida ma'lumot yo'q")

# # 3-code
# taom_n = {'osh':'30 ming',"kabob":'100 ming','somsa':'12 ming','shashlik':'15 ming'}
# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in taom_n:
#         print(f"{buyurtma.title()} {taom_n[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")