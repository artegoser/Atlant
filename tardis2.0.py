import webbrowser
import time
import os
import random
import json
from modules import cipher
from modules import mathematicks as mathe

clear = ["TARDIS------TARDIS------TARDIS------TARDIS--------artegoserdev---------------------------------------------------------"]
def art(arte ,sleep = 0, sleep2 = 0.01):
    for i in arte:
        e = ""
        for a in i:
            e += a
            print(e, end="\r")
            time.sleep(sleep2)
        print(e)
        time.sleep(sleep)


art(clear)

cipher.ciphergenkey()

vopr = 1
otv = 1

temp=0
after_id = ''


#Считывание настроек
try:
    with open("options.tardis", "r", encoding = "utf-8") as options:
        optionsdata = json.load(options)
except:
    optionsdata = {
                "name": "Пользователь",   
                "assname": "ТАРДИС"
            }
    with open("options.tardis", "w", encoding = "utf-8") as options:
            json.dump(optionsdata, options)

name = optionsdata["name"]
assname = optionsdata["assname"]

print("Здравствуйте, " + name + ". Меня зовут, " + assname + ". Я буду вашим компьютерным ассистентом")

year = time.strftime("%Y")
day = time.strftime("%d")
month = time.strftime("%m")
fulltime = time.strftime("%H:%M:%S")

print("Сегодня "+year+" год, "+day+" день и "+month+" месяц. Время "+fulltime)
print("Берегись, до 2038 года осталось "+ str(2038 - int(year)) + " лет")


s = 1
while s not in ["пока"]:
 try:
        s = input()
        if s in ["настройки", "настроить"]:
            #Перезапись настроек

            name = input("Ведите ваше имя(прошлое имя "+name+"): ")
            assname = input("Назовите меня(прошлое имя "+assname+"): ")
            optionsdata = {
                    "name": name,   
                    "assname": assname
                }
            with open("options.tardis", "w", encoding = "utf-8") as options:
                json.dump(optionsdata, options)

        elif s in ["привет", "здравствуй"]:
            privetstvia = ["Здравствуйте, повелитель", "Здравствуйте, "+name, "Привет, я "+assname+" если вы забыли, "+ name]
            print(random.choice(privetstvia))
            
        elif s in ["math","математика"]:
            print("Перехожу в режим вычислений,", name)
            print("""
                    \rпростой калькулятор(калькулятор)
                    \rфакториал
                    \rкорень квадратного уравнения
                    \rдискриминант
                    \rфигуры
                    """)
            
            s = input("Выберите режим: ")
                
            if s == "фигуры":
                print("""
                    \rARect
                    \r    #площадь прямоугольника
        
                    \rPRect
                    \r    #периметр прямоугольника
                        
                    \rPCube
                    \r    # периметр куба ,Общая длинна куба
                        
                    \rASquare
                    \r    #Площадь квадрата
                        
                    \rACube
                    \r    #Площадь куба(поверхность)
                        
                    \rVCube
                    \r    #Объем куба
                    """)
                s = input("Выберите режим: ")  
                if s == "ARect":
                        print("Площадь прямоугольника =",
                              mathe.ARect(float(input("Введите первую сторону прямоугольника: ")), 
                                          float(input("Введите вторую сторону прямоугольника: "))))
                elif s == "PRect":
                    print("Периметр прямоугольника =",
                          mathe.PRect(float(input("Введите первую сторону прямоугольника: ")), 
                                      float(input("Введите вторую сторону прямоугольника: "))))
                
 except Exception as e:
    print(e)
        