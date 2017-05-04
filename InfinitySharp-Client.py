# Developer: Jesse Scott
# Instagram: @jesse.c.scott
# GitHub: @InfinitySharp
# Version: 1.0

# Needed libraries

import os
import sys
import time
import random
from random import randint
from datetime import datetime
import socket
import smtplib

# App class

class appInfo:
    name = "InfinitySharp Client"
    developer = "Jesse Scott"
    version = 1.0

# Main code

os.system("cls")

print("Required: name, & email")

print("")

email = input("Write text here: ")

content = email

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('client.infinitysharp@gmail.com', 'INFINITYsharp#bu1ld7h3future')

mail.sendmail('client.infinitysharp@gmail.com', 'creepy.tv02@gmail.com', content)

mail.close()
