# 4

# tortlar_soni = int(input("Sizga nechta tort kerak? kerakli tort sonini kiriting: "))
#
# un_bir_tort = 450
# tuxum_bir_tort = 5
# shakar_bir_tort = 250
#
# jami_un = un_bir_tort * tortlar_soni
# jami_tuxum = tuxum_bir_tort * tortlar_soni
# jami_shakar = shakar_bir_tort * tortlar_soni
#
# print(f"{tortlar_soni} ta tort uchun kerak")
# print(f"Un: {jami_un} gramm" )
# print(f"Tuxum: {jami_tuxum} dona")
# print(f"Shakar: {jami_shakar} gramm")

# 5

# boyi = float(input("Bo'y uzunligini kiriting(m):"))
# vazn = float(input("Vaznni kiriting(kg):"))
#
# bmi = vazn / (boyi * boyi)
#
# # Toyifani aniqlash
# if bmi < 10:
#     toifa = "kashshey"
# if bmi < 18.5:
#     toifa = "ozg'in"
# elif bmi < 25:
#     toifa = "normal vazn (ideal)"
# elif bmi < 30:
#     toifa = "ortiqcha vazn"
# else:
#     toifa = "semizlik"
#
# print(f"Sizning BMI: {bmi:.3f}")
# print(f"Toifa: {toifa}")

# 6

# suv = 1200
#
# buglanish_foizi = 0.012
#
# if suv < 1000:
#     print(f"Ogohlantirish: 10 kundan keyin hovuzda {suv} litr suv qoladi.")
# else:
#     print(f"10 kundan keyin hovuzda {suv} litr suv qoladi.")

# 7

# kunlar = (100 + 11) // 12
# print(f"kamola kitobini {kunlar} kunda tugatdi! ")
#
# # 8
#
# burchak = 0 + 30 + 75
# print(f"Robotning yakuniny burchagi {burchak % 360}°")

# 9
# guruh_listi = ["Luiza", "Nurxan", "Durdona", "Aziza", "Mohigul", "Abdulaziz", "Charosbonu", "Zuhra", "Nurxan", "Noila", "Akmurod", "sherzod", "Muhammadjon", "Dilnura", "Amina", "Zebuzar"]
#
# guruh_listi.append("Mashribjon")
# print(guruh_listi)


# talabalar = ['Zuhra', 'Durdona', 'Luiza', 'Muhammadjon', 'Abdulaziz', 'Sherzod', 'Akmurod']
#
#
# for talaba in talabalar:
#
#  if talaba == 'Zuhra':
#      print(f"Salom {talaba} qalaysan")
#
#  elif talaba == 'Durdona':
#      print(f"Qalaysan {talaba}?")
#
#  elif talaba == 'Luiza':
#      print(f"Salom {talaba} nima gap")
#
#  elif talaba == 'Muhammadjon':
#      print(f"Nima gap {talaba}")
#
#  elif talaba == 'Abdulaziz':
#      print(f"Nima gap {talaba}")
#
#  elif talaba == 'Sherzod':
#      print(f"Nima gap {talaba}")
#
#  elif talaba == 'Akmurod':
#      print(f"Nima gap {talaba}")
#
#  else:
#      print(talaba)
#
# chiziq = "------------------------------------------------------------------------------------------"
# print(chiziq)
#
#
# talabalar = ['Zuhra', 'Durdona', 'Luiza', 'Muhammadjon', 'Abdulaziz', 'Sherzod', 'Akmurod']
#
# for indeks in range(len(talabalar)):
#     print(f"{indeks + 1}:  {talabalar[indeks]}")
#
# chiziq = "------------------------------------------------------------------------------------------"
# print(chiziq)
#
#
# for indeks, element in enumerate(talabalar, start=1):
#     print(f"{indeks}. {element}")


# print("     ", end="")
# for i in range(1, 10+1):
#     print(f"{i:4}", end="")
# print()
#
# print("    " + "-" * 41)
#
# for i in range(1, 10+1):
#     print(f"{i:2} |", end="")
#     for j in range(1, 10+1):
#         print(f"{i*j:4}", end="")
#     print()
#
#
#
#
#
#     count = 0
#
#     for hour in range(24):
#         for minute in range(60):
#             for second in range(60):
#                 time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
#                 print(time_str)
#                 count += 1

#     print("\nJami vaqtlar soni:", count)



# # To'g'ri parol
# togri_parol = "Paython123"
# # Urinishlar hisoblagichi
# urinishlar = 3
# # Muvafaqiyat bayrog'i
# muvafaqiyat = False
# print("Tizimga kirish")
# print('-' * 30)
# while urinishlar> 0:
#     # Foydalanuvchidan parol so'rash
#     kiritilgan_parol = input(f"Parol kiriting ({urinishlar} urinish qoldi): ")
#     # Parolni tekshirish
#     if kiritilgan_parol == togri_parol:
#         print("Parol to'g'ri tizimga xush kelibsiz!")
#         muvafaqiyat = True
#         break
#     else:
#         urinishlar -= 1
#         if urinishlar > 0:
#             print(f"Parol noto'g'ri Yana {urinishlar} urinish qoldi.")
#         else:
#             print("Barcha urinishlar tugadi, Hisob bloklandi")
# # Agar parol to'g'ri kiritilgan bo'lsa
# if not muvafaqiyat:
#     print("Iltimos, keyinroq urinib ko'ring adminga murojat qiling.")