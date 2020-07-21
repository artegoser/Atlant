import datetime
import webbrowser
import time
import os
import random
import json

clear = "TARDIS------TARDIS------TARDIS------TARDIS--------artegoserdev---------------------------------------------------------\n" * 10000
print(clear)
vopr = 1
otv = 1
try:
  os.mkdir("settings")
except:
  pass


temp=0
after_id = ''



#def speak(what):
 # if otv == 0:
  # if golos == 0:
   # try:
    # tts = gTTS(text=what, lang="ru")
     #tts.save(what +'.mp3')
#     mixer.music.load(what +'.mp3')
 #    print(what)
 #    mixer.music.play()
 #    while mixer.music.get_busy():
 #           time.sleep(0.1)
 #   except:
 #    mixer.music.load(what +'.mp3')
 #    print(what)
 #    mixer.music.play()
 #    while mixer.music.get_busy():
 #           time.sleep(0.1)
 #    pass
 # else:
 #   print(what)
 # else:
 #  if golos == 0:
 #   try:
 #    tts = gTTS(text=what, lang="ru")
 #    tts.save('message.mp3')
 #    mixer.music.load('message.mp3')
 #    print(what)
 #    mixer.music.play()
 #    while mixer.music.get_busy():
 #           time.sleep(0.1)
 #    try:
 #     path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'message1.mp3')
 #     os.remove(path)
 #    except:
 #     pass
 #   except:
 #    tts = gTTS(text=what, lang="ru")
 #    tts.save('message1.mp3')
 #    mixer.music.load('message1.mp3')
 #    print(what)
 #    mixer.music.play()
 #    while mixer.music.get_busy():
 #           time.sleep(0.1)
 #    try:
 #     path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'message.mp3')
 #     os.remove(path)
 #    except:
 #     pass
 #  else:
 #   print(what)
#def speake(what):
#  if otv == 0:
#   if golos == 0:
#    try:
#     tts = gTTS(text=what, lang="ru")
#     tts.save(what +'.mp3')
#     mixer.music.load(what +'.mp3')
#     mixer.music.play()
#     while mixer.music.get_busy():
#            time.sleep(0.1)
#    except:
#     mixer.music.load(what +'.mp3')
#     mixer.music.play()
#     while mixer.music.get_busy():
#            time.sleep(0.1)
#     pass
#   else:
#    pass
#
#  else:
#   if golos == 0:
#    try:
#     tts = gTTS(text=what, lang="ru")
#     tts.save('message.mp3')
#     mixer.music.load('message.mp3')
#     mixer.music.play()
#     while mixer.music.get_busy():
#            time.sleep(0.1)
#     try:
#      path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'message1.mp3')
#      os.remove(path)
 #    except:
  #    pass
   # except:
#     tts = gTTS(text=what, lang="ru")
 #    tts.save('message1.mp3')
  #   mixer.music.load('message1.mp3')
   #  mixer.music.play()
#     while mixer.music.get_busy():
 #           time.sleep(0.1)
  #   try:
   #   path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'message.mp3')
#      os.remove(path)
 #    except:
  #    pass
#   else:
 #   pass
def xor_cipher( str, key ):
 encript_str = ""
 for letter in str:
  encript_str += chr( ord(letter) ^ key )
 return encript_str
def ciphergenkey():
    cipherkey = "1234567890"
    key = int(random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey))
    speak("Ваш ключ: " + str(key))

s = 1
#speak("Вас приветствует ТАРДИС. Голосовой помощник.\nЕсли хотите узнать больше информации напишите Информация.\nДля изменения настроек напишите настройки.")
