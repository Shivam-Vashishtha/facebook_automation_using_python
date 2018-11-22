from selenium import webdriver
import getpass
import time

username=input("enter the user name")
password=getpass.getpass("enter password")
driver = webdriver.Chrome(executable_path="C:\\Users\\Shivam\\Desktop\\New folder\\New folder\\chromedriver_win32\\chromedriver.exe")
driver.get('https://en-gb.facebook.com/login/')



driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id("pass").send_keys(password)

driver.find_element_by_id("loginbutton").click()

driver.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys('Post by using automation')
driver.find_element_by_xpath("//*[@id='js_2x']/div[2]/div[3]/div[2]/div/div/span/button").click()
