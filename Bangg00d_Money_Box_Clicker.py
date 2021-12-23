from selenium import webdriver
import time
import os
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string, "Program Baslatildi.")	

url = 'https://tr.banggood.com/Casual-Game-Money-Box.html' #sayfa link'i
browser = webdriver.Firefox() #firefox webdriver'ini tanimladik (geckodriver)
time.sleep(3)
browser.get(url) #webdriver uzerinden url'i çagirdik
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(5)
#
#burada sayfada giris yapilmadigi icin buton'a tiklamayacaktir, bizi login sayfasina yonlendirecektir
#
eposta = browser.find_element_by_id('login-email') #e-mail giris id kutusunu id uzerinden bul ve tanimla
eposta.clear()
eposta.send_keys("senin_epostan@mail.com") #e-postayi yazdir
print(dt_string, "E-Mail Girildi.")
time.sleep(1)
parola = browser.find_element_by_id('login-pwd') #parola giris kutusunu id uzerinden bul ve tanimla
parola.clear()
parola.send_keys("senin_parolan") #parolayi yazdir
print(dt_string, "Parola Girildi.")
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/div/form[1]/ul/li[3]').click() #login butonuna tiklayarak giris yap
time.sleep(20)
browser.get(url) #webdriver uzerinden url'i çagirdik
time.sleep(5)

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]').click() #puanlari toplama butonuna tikla
time.sleep(3600)

os.system('rm geckodriver.log')
print(dt_string, "geckodriver.log Temizlendi")
time.sleep(1)
os.system('exit')
