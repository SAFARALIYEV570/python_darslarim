cars = ['kaptiva','gm','lacetti','cobalt']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
login = str(input('Yangi loginingizni kiriting:\n>>>>'))
if login.lower() == 'admin':
    print("Xush kelibsiz,Admin.Foydalanuvchilar ro'yxatini ko'raszmi?")
else:
    print("Xush kelibsiz, " + login.title())
a = int(input('son kiriting:'))
if a >= 0 :
    print('sonning ildizi ' + str(a**(1/2)) + ' ga teng')
else:
      print('musbat son kiriting')     
juft_son=int(input("Juft son kiriting:\n>>>"))
c = juft_son/2
if juft_son == 2*int(c):
    print("rahmat")
else:
    print("Bu son juft emas")    
a=str(float(input("1-sonni kiriting: ")))
b=str(float(input("2-sonni kiriting: ")))
if a>b:
    print(a + ">" + b)
elif a<b:
    print(a+    "<"  +b)
else:
    print(a+  "="   +b)
son = float(input("Juft son kiriting: "))
if son%2:
    print("Bu son juft emas.")
else:
    print("Rahmat!")
yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    print('narh=0')
elif yosh < 18:
    print("narh = 10000")
else:
    narh = 20000
    print(f"Chipta {narh} so'm")
