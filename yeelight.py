import sys
import pyautogui
import time
from PIL import Image
import requests
import pprint
import socket
import signal
import cv2
import numpy as np
import os
from os import system, name 


def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale





print("Turning lights on!")

host = '192.168.0.28'
port = 55443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
text_file = open("temp.txt", "wt")
n = text_file.write('{"id":1,"method":"set_power","params":["on", "sudden", 40]}\r\n')
text_file.close()
with open('temp.txt', 'r') as file:
    MESSAGE = file.read().replace('\n', '\r\n')
MESSAGEE = MESSAGE.encode()
#print(MESSAGEE)
s.sendall(MESSAGEE)
s.close()
os.remove("temp.txt")
time.sleep(0.2)
status = 1

def signal_handler(sig, frame):
    host = '192.168.0.28'
    port = 55443
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    text_file = open("temp.txt", "wt")
    n = text_file.write('{"id":1,"method":"set_power","params":["OFF", "sudden", 40]}\r\n')
    text_file.close()
    with open('temp.txt', 'r') as file:
        MESSAGE = file.read().replace('\n', '\r\n')
    MESSAGEE = MESSAGE.encode()
    #print(MESSAGEE)
    s.sendall(MESSAGEE)
    s.close()
    os.remove("temp.txt")
    os.remove("pic.png")
    print("Turning lights off!")
    time.sleep(1)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)
    im = pyautogui.screenshot(region=(960,540,100,100))
    im.save('pic.png') 
    myimg = cv2.imread('pic.png')
    image_bgr = cv2.imread('pic.png', cv2.IMREAD_COLOR)
    channels = cv2.mean(image_bgr)
    observation = np.array([(channels[2], channels[1], channels[0])])
    value = (round(channels[2])*65536) + (round(channels[1]) * 256) + round(channels[0])
    print("RGB_value:", value)
    if value == 0:
        host = '192.168.0.28'
        port = 55443
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        text_file = open("temp.txt", "wt")
        n = text_file.write('{"id":1,"method":"set_power","params":["OFF", "sudden", 40]}\r\n')
        text_file.close()
        with open('temp.txt', 'r') as file:
            MESSAGE = file.read().replace('\n', '\r\n')
        MESSAGEE = MESSAGE.encode()
        #print(MESSAGEE)
        s.sendall(MESSAGEE)
        s.close()
        os.remove("temp.txt")
        time.sleep(0.2)
        status = 0
    else:
        if status == 0:
            host = '192.168.0.28'
            port = 55443
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            text_file = open("temp.txt", "wt")
            n = text_file.write('{"id":1,"method":"set_power","params":["on", "sudden", 40]}\r\n')
            text_file.close()
            with open('temp.txt', 'r') as file:
                MESSAGE = file.read().replace('\n', '\r\n')
            MESSAGEE = MESSAGE.encode()
            #print(MESSAGEE)
            s.sendall(MESSAGEE)
            s.close()
            os.remove("temp.txt")
            time.sleep(0.2)
            status = 1

            time.sleep(1)
            host = '192.168.0.28'
            port = 55443
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            text_file = open("temp.txt", "wt")
            n = text_file.write('{ "id": 1, "method": "set_rgb", "params":[')
            n = text_file.write(str(value))
            n = text_file.write(', "sudden", 40]}\r\n')
            text_file.close()
            with open('temp.txt', 'r') as file:
                MESSAGE = file.read().replace('\n', '\r\n')
            MESSAGEE = MESSAGE.encode()
            #print(MESSAGEE)
            s.sendall(MESSAGEE)
            s.close()
            os.remove("temp.txt")
            time.sleep(0.2)

            file = "pic.png"
            image = Image.open(file)
            level = calculate_brightness(image)*100
            host = '192.168.0.28'
            port = 55443
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            text_file = open("temp.txt", "wt")
            n = text_file.write('{"id":1,"method":"set_bright","params":[')
            n = text_file.write(str(round(level)))
            n = text_file.write(', "sudden", 40]}\r\n')
            text_file.close()
            with open('temp.txt', 'r') as file:
                MESSAGE = file.read().replace('\n', '\r\n')
            MESSAGEE = MESSAGE.encode()
            #print(MESSAGEE)
            s.sendall(MESSAGEE)
            s.close()
            os.remove("temp.txt")
            time.sleep(0.2)
            print("Brightness:", round(level))

        else:
            host = '192.168.0.28'
            port = 55443
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            text_file = open("temp.txt", "wt")
            n = text_file.write('{ "id": 1, "method": "set_rgb", "params":[')
            n = text_file.write(str(value))
            n = text_file.write(', "sudden", 40]}\r\n')
            text_file.close()
            with open('temp.txt', 'r') as file:
                MESSAGE = file.read().replace('\n', '\r\n')
            MESSAGEE = MESSAGE.encode()
            #print(MESSAGEE)
            s.sendall(MESSAGEE)
            s.close()
            os.remove("temp.txt")
            time.sleep(0.2)

            file = "pic.png"
            image = Image.open(file)
            level = calculate_brightness(image)*100
            host = '192.168.0.28'
            port = 55443
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            text_file = open("temp.txt", "wt")
            n = text_file.write('{"id":1,"method":"set_bright","params":[')
            n = text_file.write(str(round(level)))
            n = text_file.write(', "sudden", 40]}\r\n')
            text_file.close()
            with open('temp.txt', 'r') as file:
                MESSAGE = file.read().replace('\n', '\r\n')
            MESSAGEE = MESSAGE.encode()
            #print(MESSAGEE)
            s.sendall(MESSAGEE)
            s.close()
            os.remove("temp.txt")
            time.sleep(0.2)
            print("Brightness:", round(level))
            status = 1
signal.pause()