from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()

chromedriver_path = 'chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

# POSTAL CODE - DDD - NUMBER
#exemplo - 5531987654321
webdriver.get('https://wa.me/xxxxxxxxxxxxx')

inicia_conversa = webdriver.find_element_by_css_selector('#action-button')
inicia_conversa.click()

sleep(1.5)

i = 0
while i < 2:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        sleep(0.2)
        i = i + 1       
sleep(0.5)
keyboard.press(Key.enter)

sleep(10)

j = 0
while(j < 200):
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release(Key.ctrl)
        keyboard.release('v')
        keyboard.press(Key.enter)
        sleep(0.3)
        j = j+1
        
print("TRAVADO")

