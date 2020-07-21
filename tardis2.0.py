import datetime
import webbrowser
import time
import os
import random
import json

clear = "TARDIS------TARDIS------TARDIS------TARDIS--------artegoserdev---------------------------------------------------------\n"
print(clear)
vopr = 1
otv = 1
try:
  os.mkdir("settings")
except:
  pass


temp=0
after_id = ''


def xor_cipher( str, key ):
 encript_str = ""
 for letter in str:
  encript_str += chr( ord(letter) ^ key )
 return encript_str
def ciphergenkey():
    cipherkey = "1234567890"
    key = int(random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey))
    speak("Ваш ключ: " + str(key))


#speak("Вас приветствует ТАРДИС. Голосовой помощник.\nЕсли хотите узнать больше информации напишите Информация.\nДля изменения настроек напишите настройки.")



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

year = datetime.datetime.today().strftime("%Y")
day = datetime.datetime.today().strftime("%d")
month = datetime.datetime.today().strftime("%m")
fulltime = datetime.datetime.today().strftime("%H:%M:%S")

intyear = int(year)
to2038 = 2038 - intyear

print("Сегодня "+year+" год, "+day+" день и "+month+" месяц. Время "+fulltime)
print("Берегись, до 2038 года осталось "+ str(to2038) + " лет")




s = 1
while s not in ["пока"]:
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