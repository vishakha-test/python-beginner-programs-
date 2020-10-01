'''
Author: kushuu
Date: Mon Aug 31 2020
File: whatsapp.py
'''

import pywhatkit as kit

#to play a video on youtube.
kit.playonyt("pause prateek")


#to send a whatsapp messsage.
kit.sendwhatmsg("+917387468768", "this is being sent using python on my PC :)", 18, 44)


#to make a google search.
kit.search(input("enter the topic: "))