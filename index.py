# Строка заканчивается на ?
# Завершите решение так, чтобы оно возвращало значение true, если первый переданный аргумент (строка) заканчивается
# 2м аргументом (также строкой)
# def solution(text, ending):
#     return text.endswith(ending)

# print(solution('alibabc', 'bc')) 


# Учитывая массив целых чисел, удалите наименьшее значение. Не изменяйте исходеый массив/список. Если есть несколько элементов с 
# одинаковым значением, удалите тот, у которого индекс ниже.
# def remove_smal(numbers):
#     if numbers:
#         min_val = min(numbers)
#         return [x for i, x in enumerate(numbers) if i != numbers.index(min_val)]
 

# print(remove_smal([1, 2, 3, 4, 5])) 



#################################################################################################


#Фильтрация списка:
# 1) Напишите функцию filter_even_numbers, которая принимает список чисел и возвращает
# новый список , содержащий только четные числа

# def filter_even_numbers(lst):
#     lst2 = []
#     for i in lst:
#         if i % 2 ==0:
#             lst2.append(i)
#     return lst2        
# print(filter_even_numbers([1,2,3,4,5,6,7,8,9,10,11]))


# Трансформация списка:
# 2) Напишите функцию square_numbers , которая принимает список чисел и возвращает новый список , 
# в котором каждый элемент возводится в квадрат

# def square_numbers(lst):
#     lst2 = []
#     for i in lst:
#         lst2.append(i**2)
#     return lst2        
# print(square_numbers([1,2,3,4,5,6,7,8,9,10,11]))

# Агрегация списка:
# 3) Напишите функцию calculate_average, которая принимает список чисел и возвращает их среднее значение
# def calculate_average(lst):
#     av = sum(lst) / len(lst)
#     return av
# print(calculate_average([4,5,6,7,8,9,10]))


# Обработка строк в списке:
# 4) Напишите функцию filter_long_words, которая принимает список строк и возвращает новый список, содержащий только те строки  ,
# длина которых превышает заданное значение

# def filter_long_words(words, length):
#     filtered_words = []
#     for word in words:
#         if len(word) > length:
#             filtered_words.append(word)
#     return filtered_words

# word_list = ["apple", "banana", "orange", "grape", "watermelon"]
# filtered_list = filter_long_words(word_list, 5)
# print(filtered_list)

# 5) Объединение списков:
# Напишите функцию merge_lists, которая принимает два списка и возвращает новый список, содержащий все элементы обоих списков .

# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# result = merge_lists(list_a, list_b)
# print(result)


# Дайте определение понятию "класс"
# Что такое поле/атрибут класса?
# Как правильно организовать доступ к полям класса?
# Дайте определение поняти "Конструктор"
# Дайте определение понятию "метод/функция"

#####################################################################

# Задача: Библиотечный каталог
# Перед вами стоит задача создать простую систему библиотечного каталога. Реализовать классы для библиотеки и книги.
# Каждая книга должна принандлежать определенной категории, и библиотека должна отслеживать книги в различных категориях

# class LibraryCatalog:
#     def __init__(self, library_name):
#         self.library_name = library_name
#         self.categories = {}

#     def add_category(self,category_name):
#         if category_name not in self.categories:
#             self.categories[category_name] = []

#     def add_book(self,book,category):
#         if category in self.categories:
#             self.categories[category].append(book)
#         else:
#             print("нет такой категории", category)           

#     def books_in_category(self):
#         info_str = f"Библиотека: {self.library_name}\n"
#         for category, books in self.categories.items():
#             info_str += f"{category} категория: {len(books)} книги\n"

#         return info_str


# class Book:
#     def __init__(self, title, author, category):
#         self.title = title
#         self.author = author
#         self.category = category              

#     def __repr__(self)
#         :
#         return f"{self.title} автор {self.author}"      


# library = LibraryCatalog('Бишкек китепканасы')
# library.add_category = ('Кыргызстан тарыхы')
# library.add_category = ('Манас')
# book1 = Book('Курманжаг Датка', 'Алихан Алиханов','Кыргызстан тарыхы')
# book2 = Book('7 осуят', 'Саякбай Каралаев','Манас')
# book3 = Book('Кырыгзский Каганат', 'Айдай Манасова','Кыргызстан тарыхы')
# library.add_book(book1, 'Кыргызстан тарыхы')
# library.add_book(book2, 'Манас')
# library.add_book(book3, 'Кыргызстан тарыхы')
# print(library.books_in_category)


################################################################################]




# def add_category_(self,category_name):
#     if category_name not in self.categories:
#         self.categories[category_name]=[]

# def add_book(self,)


# class biblioteka:

#     def __init__(self, libname):
#         self.libname = libname
#         self.categories = {}

#     def add_category(self, categories_name):
#         if categories_name not in self.categories:
#             self.categories[categories_name]=[]


#     def add_book(self,book,category):
#         if category in self.categories:
#             self.category[category].append(book)
#         else:
#             print('нет такой категории')



#     def info(self):
#         info = f'библотека {self.libname}'
#         for cat, book in self.categories.items():
#             info += f'категория:{cat} ({len(book)})книги:{book}\n'
#             return info



# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         return f"книга: {self.title} \ автор: {self. author}"



# libra = biblioteka('Салымбеков китепканасы')
# libra.add_category('кыргызстан тарыхы')
# libra.add_category('Манас')
# book1 = Book('Кыргыз каганаты', "Омурбек Торокелдиев")
# book2 = Book('Курманжан Датка',"Aйдай Байбекова")
# book3 = Book('7 осуят',"Акмарал Табылдиева")
# libra.add_book(book1,'Кыргызстан тарыхы')
# libra.add_book(book2,'Кыргызстан тарыхы')
# libra.add_book(book3,'Манас')
# print(libra.info())



# class Employee:
#     def __init__(self,name,postotion,slsry):
#         self.name=name
#         self.nampositione=position
#         self.salary =salary

#     def  __repr__(self):
#         return f'{self.name} - {self.position} ({self.saary}$)'

# company = company

# Инкапсуляция = скрытие данных
# 3 вида:
# public = публичный (атрибуты и методы)
# _protected = защищенный (атрибуты и методы)
# __private = приватный (атрибуты и методы)




# class Animal:

#     def __init__(self, name, age, damage=0,hp=100):
#         self.name = name
#         self.__age = age
#         self.damage = damage
#         self.hp = hp

#     @property # getter получатель
#     def age(self):
#         return self.__age


#     @age.setter
#     def age(self,valuem):
#         if valuem <= 20:
#             self.__age = valuem


#     def reName(self, newName):
#         self.name = newName
     
#     def info(self):
#         return f"Имя: {self.name} age: {self.__age}"
# class Cat(Animal):


#     def mau(self):
#         print('mau-mau')    

 
# class Dog(Animal):



#     def gav(self):
#         print('gav-gav')    



# cat1 = Cat("Fernar", 10)
# dog1 = Dog('Bobik', 5)
# cat1.age = 12
# print(cat1.info())
# print(dog1.info())


####################################################################################################
# Задача: Учет продуктов в магазине 
# Создайте классы для представления продуктов и магазина. Каждый продукт должен иметь название, цену и количество в наличии.
# Магазин должен отслеживать все свои продукты и предоставлять информацию о суммарной стоимости продуктов и количестве каждого продукта

# class Store:
#     def __init__(self,storeNaeme):
#         self.storeName = storeNaeme
#         self.products = []


#     def add_product(self,product):
#         self.products.append(product)

#     def total_cost(self):
#         total = 0
#         for prod in self.products:
#             total += prod.price * prod.quantity
#         return total

#     def product_inventory(self):
#         inventory = {}
#         for product in  self.products:
#             name = product.name
#             quantity = product.quantity
#             if name in inventory:
#                 inventory[name]+= quantity
#             else:
#                 inventory[name]= quantity            
#         return inventory
    

#     def info(self):
#         infostr = f"магазин {self.storeName}\n"
#         infostr+= f"общая стоимость: {self.total_cost()} сом\n"
#         infostr+= 'Такие подукты как:\n'
#         for product, quantity in self.product_inventory().items():
#             infostr+= f"{product}: {quantity}шт \n"

#         return infostr    




# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __repr__(self) -> str:
#         return f"{self.name} Цена: {self.price} {self.quantity}"    

# prod1 = Product("Хлеб", 25, 2)
# prod2 = Product("Молоко", 55, 3)
# prod3 = Product("Яйца", 105, 5)
# store = Store("Globus")
# store.add_product(prod1)
# store.add_product(prod2)
# store.add_product(prod3)
# print(store.info())




###########################################################################################

# Задача 2: Учет сотрудников в компании 
# Создайте классы для представления сотрудников и компании. Каждый сотрудник должен иметь имя, должность и 
# заработную плату. Компания должна

###########################################################################################################

# class restaranOrder:
#     def __init__(self, order_number):
#         self.order_number = order_number
#         self.bluda = []


#     def add_bludo(self, bludo):
#         self.bluda.append(bludo)

#     def total_cost(self):
#         total = sum(bludo.price for bludo in self.bluda)
#         return total

#     def order_contents(self):
#         contents = {}
#         for bludo in self.bluda:
#             name = bludo.name 
#             if name in contents:
#                 contents[name] += 1
#             else:
#                 contents[name] = 1
#         return contents


#     def order_info(self):
#         infostr = f"Заказ № {self.order_number}\n"
#         infostr += 'Содержание заказа:\n'
#         for bludo, quantity in self.order_contents().items():
#             infostr += f'{bludo} {quantity} порции\n'
#         infostr += f"Общая стоимость {self.total_cost()}\n"
#         return infostr

# class Dish:
#     def __init__(self, name, price, description):
#         self.name = name 
#         self.price = price 
#         self.description = description    

#     def __repr__(self):
#         return f"{self.name} {self.price} {self.description}"
    

# bludo1 = Dish('Boso Lagman', 189, 'какой то вкусный но...')
# bludo2 = Dish('Рамён', 380, 'Корейская кухня')
# bludo3 = Dish('Рамён', 380, 'Корейская кухня')
# bludo4 = Dish('Рамён', 380, 'Корейская кухня')
# bludo5 = Dish('Баранина антрекот', 420, 'Кавказская кухня')
# order1 = restaranOrder(1)
# order1.add_bludo(bludo1)
# order1.add_bludo(bludo2)
# order1.add_bludo(bludo3)
# order1.add_bludo(bludo4)
# order1.add_bludo(bludo5)
# print(order1.order_info())

#########################################################################
#Задача №2: Учет студентов и курсов в университете 
# Условие: Создайте классы для представления студентов и курсов в университете. Каждый студент должен иметь имя, фамилию и список курсов, 
# которые он посещает. Каждый курс должен иметь название и преподавателя. Университет должен отслеживать всех студентов и предстовлять информацию
# о студентах, их посещаемых курсах и преподавателях 
# class University:
#     def __init__(self):
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def get_all_students_info(self):
#         for student in self.students:
#             print(f"Студенты: {student.first_name} {student.last_name}")
#             print("Посещаемые курсы:")
#             for course in student.courses:
#                 print(f"Курс: {course.title} Преподаватель: {course.teacher}")
#             print("="*30)

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.courses = []

#     def enroll(self, course):
#         self.courses.append(course)

# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher

# uni = University()

# math_course = Course("Math", "Professor Smith")
# history_course = Course("History", "Professor Johnson")

# john = Student("John", "Doe")


# jane = Student("Jane", "Smith")

# john.enroll(math_course)
# jane.enroll(history_course)
# jane.enroll(math_course)  


# uni.add_student(john)
# uni.add_student(jane)

# uni.get_all_students_info()
##########################################################################################################

#Задача 9. Напишите функцию remove_negative_numbers, которая принимает список чисел и возвращает новый список, из которого удалены все
# отрицательные элементы
# def remove_negative_numbers(numbers):
#     return [num for num in numbers if num >= 0]

# numbers = [1, -2, 3, -4, 5]
# result = remove_negative_numbers(numbers)
# print(result)


       



# class Pizza:
#     def __init__(self , name, price, ingredients):
#         self.name = name
#         self. price = price
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f"пицца: {self.name} {self.price} coм"
    

# class Koshelek:
#     def __init__(self,balance=0):
#         self.balance = balance

#     def popolnenie(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         else:
#             print("Деньги не могут быть ниже 0")
#             return False
        
#     def chek_balance(self):
#         return self.balance
    

# class ZakazPizza:
#     def __init__(self):
#          self.menu = [   
#             Pizza('пеперони', 450, ['ТОМАТ', "сыр"]),
#             Pizza('Маргарита', 390, ['Томат', "сыр"]),
#             Pizza('Охотничий', 510,['колбаса',"сыр"])
#         ]
         
#     def display_info(self):
#         print('Меню: ')
#         for piz in self.menu:
#             print(piz)
        
#     def place_order(self,pizza_index, wallet):
#         if 0 <= pizza_index < len(self.menu):
#             selected_pizza = self.menu[pizza_index]
#             if wallet.chek_balance() >= selected_pizza.price:
#                 wallet.balance -= selected_pizza.price
#                 print(f'Заказ сделан: {selected_pizza.name}')
#                 return True
#             else:
#                 print('Недостаточна средств.Пожалуйста,внесите деньги в свой кошелек')
#                 return False
#         else:
#             print("Ошибка заказа,неправильно заказали")
#             return False

# Koshelek = Koshelek(500)
# Koshelek.popolnenie(200)
# order = ZakazPizza()
# order.display_info()
# order.place_order(1, Koshelek)




##########################################################################################

# class Bird:
#     wing = 'крыло'
            
#     def fly(self):
#         print('птица летит')


# class Chicken(Bird):
#     def runs(self):
#         print('курица бежит')


#Напишите базовый класс
# Транспортное средство с атрибутами:скорость и вместимость от этого класса унаследуйте классы 
# автомобиль и велосипед

# class Vehicle:
#     def __init__(self, speed, capacity):
#         self.speed = speed
#         self.capacity = capacity

# class Car(Vehicle):
#     def __init__(self, speed, capacity):
#         super().__init__(speed, capacity)

# class Bicycle(Vehicle):
#     def __init__(self, speed, capacity):
#         super().__init__(speed, capacity)


# car = Car(100, 5)
# bicycle = Bicycle(20, 2)  

# print("Car - Speed:", car.speed)
# print("Car - Capacity:", car.capacity)

# print("\nBicycle - Speed:", bicycle.speed)
# print("Bicycle - Capacity:", bicycle.capacity)




# Создать класс квадрат а также создать в нем функцию которая будет вычислять его плошадь

# class Square:
#     def calculate_area(self,radius):
#         self.radius = radius
#         print(radius ** 2)

# s = Square()
# s.calculate_area(10)        

# class Figure:
#     def calculate_area(self):
#         pass

# class Circle(Figure):
#     def __init__(self,radius):
#         self.radius = radius   

#     def calculate_area(self):
#         area = 3.14 * self.radius ** 2
#         return area      

# class Rectangle(Figure):
#     def __init__(self,height, width):
#         self.height = height
#         self.width = width

#     def calculate_area(self):
#         area = self.height * self.width
#         return area
#################################################################################################


# import requests 
# from bs4 import BeautifulSoup as BS
# # link = "https://icanhazip.com/"
# # req = requests.get(link)
# # print(req.text)
   
# url = 'https://health-diet.ru/table_calorie'
# req = requests.get(url)
# src = req.text
# print(src)
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)
# soup = BS(src)
# all_product_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
# for item in all_product_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru'+item.get('href')
#     print(f"{item_text} - {item_href}")

###################################################################################################

# import requests, json
# from bs4 import BeautifulSoup as BS 
# url = "https://www.casio-europe.com/ru/products/watches/"
# req = requests.get(url) 
# soup= BS(req.text,'html.parser')
# category_elements = soup.find_all('a', class_='column bg-white')
# category_dict = {}
# for cat_elements in category_elements:
#     cat_name = cat_elements.text.strip()
#     cat_link = cat_elements['href']
#     category_dict[cat_name]=cat_link      
# with open('categories.json', 'w', encoding='utf-8') as file:
#     json.dump(category_dict, file, index, t=4, ensure_ascii=False)





# "//www.casio-europe.com/ru/products/watches/g-shock/" 

##############################################################################################################
# name = input("Ваше имя:")
# names = ["Asan", "Uson", "Aijan", "Nursultan"]
# if name in names:
#     print(f"{name} в нашей группе")
# else:
#     print(f"{name} не в нашей группе")    

# class Worker:
#     def __init__(self, name, surname, rate, days):
#         self.name = name
#         self.surname = surname
#         self.rate = rate
#         self.days = days

#     def getSalary(self):
#         salary = self.rate * self.days
#         return salary

# worker1 = Worker("Иван", "Иванов", 1000, 20)

# salary1 = worker1.getSalary()

# print(f"{worker1.name} {worker1.surname}: Зарплата - {salary1} руб.")

# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)  
# print(my_list)

# d1 = {"john": 40, "peter": 45}
# d2 = {"john": 466, "peter": 45}
# print(d1 == d2)

# age = int(input("Введите свой возраст: "))

# if age < 15:
#     print("Ты пока школьник")
# elif 15 <= age <= 18:
#     print("Все ты НАШ")
# elif age > 20:
#     print("Тебе не в колледж, а в универ надо")

# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i)

# file_path = 'путь_к_файлу.txt'

# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = list(set(original_list))


# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# with open('output.txt', 'w', encoding='utf-8') as file:
#     content_to_write = "Привет, мир!"
#     file.write(content_to_write)

# lst = [2, 54, 33, 'PHP!', 'RubyOnRails', '0.0000891', 3.14156]

# first_element = lst[0]
# print("Первый элемент:", first_element)

# middle_index = len(lst) // 2
# middle_element = lst[middle_index]
# print("Средний элемент:", middle_element)

# original_string = "доброе утро"

# words = original_string.split()

# reversed_string = " ".join(reversed(words))

# print(reversed_string)

# text = """
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
# industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type
#  and scrambled it to make a type specimen book. It has survived not only five centuries, but also
#    the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the
#      1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop
#        publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# """

# lowercase_text = text.lower()

# count_p = lowercase_text.count("p")
# count_m = lowercase_text.count("m")

# print("Количество букв 'p':", count_p)
# print("Количество букв 'm':", count_m)

# a = [1, 5, 69, 13, 0]
# b = [5, 13, 5, 123, -0]
# print(len(set(a)&set(b)))

# a = {1: "A", 2: "B", 3: "C"}
# for i, j in a.items():
#     print(i, j, end=" ")

# my_password = ['qwerty', '12345678']
# user_input = input("вВЕДИТЕ ПАРОЛЬ")
# if user_input in my_password:
#     print("Пароль верный")
# else:
#     print("Пароль нет")


# def reverse_and_filter_odd(input_list):
#     result = [num for num in reversed(input_list) if num % 2 != 0]
#     return result

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# result_list = reverse_and_filter_odd(lst)
# print(result_list)


# try:
#     result = 2 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Деление на ноль нельзя")


# class Animal:
#     def __init__(self, food, location):
#         self.food = food
#         self.location = location

#     def makeNoise(self):
#         print("Животное издает звук")

#     def eat(self):
#         print("Животное ест")

#     def sleep(self):
#         print("Животное спит")


# class Dog(Animal):
#     def __init__(self, food, location, breed):
#         super().__init__(food, location)
#         self.breed = breed

#     def makeNoise(self):
#         print("Собака лает")

#     def eat(self):
#         print("Собака кушает косточки")


# class Cat(Animal):
#     def __init__(self, food, location, color):
#         super().__init__(food, location)
#         self.color = color

#     def makeNoise(self):
#         print("Кошка мурлычет")

#     def eat(self):
#         print("Кошка ест рыбу")


# class Horse(Animal):
#     def __init__(self, food, location, breed):
#         super().__init__(food, location)
#         self.breed = breed

#     def makeNoise(self):
#         print("Лошадь ржет")

#     def eat(self):
#         print("Лошадь пасется в поле")


# class Veterinarian:
#     def treatAnimal(self, animal):
#         print(f"Ветеринар обслуживает животное. Еда: {animal.food}, Место: {animal.location}")


# animals = [
#     Dog("Корм", "Дом", "Овчарка"),
#     Cat("Корм", "Квартира", "Рыжий"),
#     Horse("Сено", "Ферма", "Тяжеловоз")
# ]

# vet = Veterinarian()

# for animal in animals:
#     vet.treatAnimal(animal)



   




# from icrawler.builtin import GoogleImageCrawler

# goole_crawler = GoogleImageCrawler(storage={
#     'root_dir':'C:/Users/HP/Desktop/cs 14 arsen'
# })
# quan = int(input("сколько нужно фото парсить?"))
# link = input("дай ссылку сайта фото?")
# # goole_crawler.crawl(keyword=link, max_num=quan)



# import requests
# import img2pdf

# def get_data():
#     for i in range(1,48):
#         url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
#         req = requests.get(url)
#         res = req.content
#         with open(f'arsen/{i}.jpg', 'wb') as file:
    
# #get_dat

# def get_data():
#     for i in range(1,48):
#         url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
#         req = req.get(url)
#         res = req.content
#         with open(f'arsen/{i}.jpg', 'wb') as file:
    
# qdwfeghtfgfqawfegrbwesd


###############################################################################################################################