# -*- coding: utf-8

#import
import os
import telebot
import time

#setting
token = ('')
chat_id = ('')
hostname = ('')
bot = telebot.TeleBot(token)

#testing
#for i in reversed(range(5)):
    #print('Осталось %d секудн' % i)
    #time.sleep(1)

#main
while True:
    #time.sleep(5)
    response = os.system('ping -w 10 ' + hostname)
    if response == 0:
        print(hostname + ' is up!')
    else:
        print(hostname + ' is down!')
        bot.send_message(chat_id,(hostname + ' is down!'))
