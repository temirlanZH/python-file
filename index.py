# Python for Begginers (This is my code)

# Python Math
# x = int (input("Сколько вам лет?: "))
# if x <= 5:
#     print("Привет малыш")
# if x > 5:
#     print("Привет друг")
# if x >= 18:
#     print("Здравствуйте")

# a = 10
# if (a > 5) and (a > 10) or (a < 15):
#     print(a < 15)

# Акинатор с помощью Python

# жёлтый, оранжевый, персиковый, коричневый.
# print('Выберите любой цвет который показан - Желтый, Оранжевый, Персиковый, Коричневый, Черный, Серый, Светло-Черный, Черно-Белый')

# question1 = input('Ваш цвет из семейства желтых?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет оранжевый или жёлтый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет жёлтый?')
#         if question3 == 'Да':
#             print('Ваш цвет жёлтый!')
#             quit()
#         else:
#             print('Ваш цвет оранжевый!')
#             quit()


# question1 = input('Ваш цвет из семейства темно-желтых?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет коричневый или персиковый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет коричневый?')
#         if question3 == 'Да':
#             print('Ваш цвет коричневый!')
#             quit()
#         else:
#             print('Ваш цвет персиковый!')
#             quit()

# question1 = input('Ваш цвет из семейства черных?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет черный или серый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет черный?')
#         if question3 == 'Да':
#             print('Ваш цвет черный!')
#             quit()
#         else:
#             print('Ваш цвет серый!')
#             quit()

# question1 = input('Ваш цвет из семейства Ярко-черных?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет Светло-Черный или Черно-Белый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет Светло-Черный?')
#         if question3 == 'Да':
#             print('Ваш цвет Светло-Черный!')
#             quit()
#         else:
#             print('Ваш цвет Черно-Белый!')
#             quit()

# a = 'love'
# b = 'you'
# c = a + b
# print(c)

# Stroka format 
# name = "Алексей"

# ice_place = "Медео"

# number = 8

# boolean = "Пока нету"

# no_int_nimber = 0.3145

# stroka = 'Привет, меня зовут {}, я увлекаюсь программированием. Я живу в Алмате и у нас есть каток {}. Вчера мы ездили на каток вместо с друзьями, нас было {} человек. Недавно на телефон скачал себе игру Brawl Stars, наличие легендарок - {}, шанс на легу - {}.' .format(name, ice_place, number, boolean, no_int_nimber)
# print(stroka)


# Brawlers modules
# brawlers = "Тик, Шелли, ЛИОН, Пэм, Барли, ЛЕАН, Биби, Фрэнк, Нита, Кольт, Бык, ЛЕОН, Ворон"

# brawlers = (brawlers).lower()
# print(brawlers[67:71])
# from autocorrect import Speller

# spell = Speller(lang="en")
# print(spell("Telegram is the mast multifunctional manager of all. Soooon I will alsa learn how to wgite telegram botc."))

# color = ["Красный", "Желтый", "Синий", "Коричневый", "Черный", "Белый"]

# array and stroka
# array = ["Яблоко", "Подсолнух", 3]

# if "Яблоко" in array:
#      print("Яблоко в картинке присутствует!")

# if "Подсолнух" in array:
#      print("Подсолнух в картинке присутствует!")

# if 3 in array: 
#     print("Число 3 присутствуют в массиве!")

# Операция и методы списка
# my_list1 = ["сок", "компот"]
# my_list2 = [ "молоко", "кофе", "чай"]
# my_list1.extend(my_list2)
# my_list1[0] = "kompot"
# my_list1.sort(reverse=True)
# print(my_list1)

# array = ["Дом 1", "Дом 2", "Дом 3", "Дом 4", "Дом 5", "Дом 6", "Дом 7", "Дом 8", "Дом 9", "Дом 10", "Дом 11", "Дом 12", "Дом 13", "Дом 14" ]
# for i in range(0,14,3):array[i] += " Доставлено"
# print(array)


# 2 Модуль окончен ура!!

# temirlanZH = ["шоколад Milka", "сыр Ементаль", "молоко Казахстанское", "мыло хозяйственное", "колбаса Докторская", "шоколад Nestle",
#          "молоко Домашнее", "сыр Чедер", "Салат Айсберг", "шоколад Казахстанский", "хлеб черный", "хлеб ржаной", "хлеб пшеничный",
#          "хлеб белый", "хлеб кирпичик", "хлеб батон"]

# count = 0

# for index in range(len(temirlanZH)):
#     if "молоко" in temirlanZH[index - count] or "сыр" in temirlanZH[index - count]:
#         temirlanZH.remove(temirlanZH[index - count])
#         count += 1

# count = 0
# xleb_count = 0

# for index in range(len(temirlanZH)):
#     if "хлеб" in temirlanZH[index - count]:
#         if xleb_count == 2:
#             print(temirlanZH[index - count])
#             xleb_count = 0
#         else:
#             temirlanZH.remove(temirlanZH[index - count])
#             xleb_count += 1
#             count += 1

# print(temirlanZH)



# Начинаем с 3 модуля)
# print("Начнем с 3 модуля!")
# Function DEV in phyton
# def summa(a, b):
#   return a + b

# number = summa(2, 3)
# number = number * 2
# print(number)

# def identification(name, age, work):
#     more_18, work_good = False, False

#     if work in ["Доктор", "Программист" , "Программный Инженер" , "Менеджер по продажам" , "Дизайнер" , "Веб-разработчик"]:
#         work_good = True  

#         output = 'Ваше имя {0}, ваша профессия {1}, вам больше 18 лет - {2}'.format(name, work_good, more_18)
#         return output

# print(identification("Mike", 20 , "Программный Инженер"))
# 15 lesson in phyton lang.
# word = input()
# chisla = list(range(1, 11)) #1,2,3,4,5,6,7,8,9,10

# def half(chisla, word):
#     if word == "половина":
#         print(chisla[0:5])
#     else:
#         print(chisla)

# half(chisla, word)

# def decoration_function(func):
#     def wrapper():
#         print("Наша Функция {} - Прошла Функция)" .format(func))
#         func()
#     return wrapper

# @decoration_function
# def hello_world():
#     print("Hello World!")
# hello_world()

# some = str(input())
# a = some[::-1]
# if some == a:
#   print("yes")
# else:
#   print("no")

# name = input("What's your name?")
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

# int()
# float()
# bool()
# str()

# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum: " + str(sum))

# first = input("First: ")
# second = input("Second: ")
# sum = int(first) + int(second)
# print("Sum: " + str(sum))

# course = "Python for Beginners"
# print(course.upper())

# course = "Python for Beginners"
# print(course.lower())

# course = "Python for Beginners"
# print(course.replace('x', '4'))


# course = "Python for Beginners"
# print('Python'in course)

# words = "This is an example!"
# print(words.encode('This is an example!')

# i = 0
# while True:
#     print(i**2)
#     i += 1
#     break

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n + factorial(n-1)


# print(factorial(1000))

# alex_array = []

# def alexey(n):
#     if n < 10:
#         if n in [0, 6, 9]:
#             return n
#         else:
#             return 0
#     return alexey(n - 1) + alexey(n - 2) + alexey(n - 3)

# for i in range(35):
#     if i in [0, 6, 9]:
#         alex_array.append(alexey(i))
#     elif i >= 10:
#         alex_array.append(alexey(i))
        
# print(alex_array)

# def countBits(n):
#     return bin(n).count("1")

# def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False

# word = input()

# try: 
#     if int(word) % 2 == 0:
#         print("Это четное число")
#     else:
#         print("Это нечетное число")

# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# else: 
#     print("Не сработала не одна ошибка")
# finally:
#     print("Это был цикл try-expect-finally")

# def function():
#   numbers = {
#     'сто': 100, 
#     'девяносто': 90,
#     'двенадцать': 12,
#     'пять': 5
# }
#   print(numbers.items())

# slovar = {"one": 100, "two": 100, "three": 100, "four": 100, "five": 100}
# print(slovar.items())

# slovar = {"one": 100, "two": 200, "three": 200, "four": 100, "five": 200}

# for i in slovar:
#     slovar[i] = 100
# print(slovar)

# def printer(**kwargs):
#     for key, value in kwargs.items():
#         if key == "first_name": 
#             output = f"Имя поэта - {value}"
#         elif key == "second_name":
#             output += f" , фамилия поэта - {value}"
#         else:
#             output += f" , еще информация: {key}- {value}"
    
#     return output 


# print(printer(first_name="Александр", second_name="Пушкин", age=28))
# print(printer(first_name="Абай", second_name="Кунанбаев", age=32))
# print(printer(first_name="Ричайд", second_name="Феймон", age=49))


# def myFun(*args,**kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
 
 

# myFun('begginer','for','javascript',first="begginer",mid="for",last="pyth"



# n = int(input()) # кролики
# K = int(input()) # грядки
# r = list(map(int, input().split())) # первоначальная позиция
# q = int(input()) # запросы
# count = [] # count
# for i in range(q):
#     p = list((str, input().split())) 
#     if p[0] == 'G':
#         s = 0
#         number_one = int(p[1])
#         number_two = int(p[2])
#         for j in r: 
#             if number_one <= j <= number_two:
#                 s += 1
#         count.append(s)#     if p[0] == 'R':
#         r[int(p[1])-1] += 1
#     if p[0] == 'L':
#         r[int(p[1])-1] -= 1

# for i in count:
#     print(i)

# array = [{'x': 'x', 'y': 'y', 'unique': True}, 
#          {'1': '2', '3': '4'}, 
#          {'x': 'x', 'y': 'y', 'unique': True}]

# for dict in array:
#   if 'unique' in dict:
#     print(True)
#   else:
#     print(False)

# import math 

# def CalculatePi(roundVal):

# 		somepi = round(math.pi,roundVal);
# 		pi = str(somepi)
# 		someList = list(pi)
# 		return somepi;
# roundTo = input('Enter the number of digits you want after the decimal for Pi: ')
# try:
# 	roundint = int(roundTo);
# 	print(CalculatePi(roundint));
# except:
# 	print("You did not enter an integer");

# import math

# temirlan = int(input("How many spaces? "))

# while temirlan > 50:
# 	print("Number to large")
# 	temirlan = int(input("How many spaces? "))
# else: 
#     print('%.*f' %  (temirlan, math.pi))

# import math


# def is_prime(num):
#     if num < 2:
#         return False

#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True


# def get_next_prime(num):
#     i = num + 1
#     while True:
#         if is_prime(i):
#             return i
#         i += 1

# if __name__ == "__main__":
#     print ("Press enter to continue, done to stop")

#     i = 2
#     while True:
#         print (i),
#         user_input = int(input())
#         if user_input == 'done':
#             break
#         i = get_next_prime(i)

# import numpy as np

# A = np.array([[4, 2, 7], [9, -2, 0]])
# B = np.array([[2, 2], [2, 1], [3, -3]])

# C = B.ravel()
# print(C)

# 43 lesson
objects = ["клавиатура", True, "наушники", "мышка", 112, "монитор", 431, "процессор", "ОЗУ", 43, 123, 4, "плата"]
cleaning_objects = list(map(lambda x: x.upper() ,filter(lambda x: type(x) != int and type(x) != bool, objects)))
print(cleaning_objects)