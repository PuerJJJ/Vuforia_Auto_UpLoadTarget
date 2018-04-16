# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os
##上传
##文件夹路径
path='C:\\Users\\h1186\\Desktop\\a04\\'
def upfile(filename):
    try:
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get("https://developer.vuforia.com/home-page")
        driver.find_element_by_id('vuforiaLogin').click()
        ##用户名和密码
        driver.find_element_by_id("login_email").send_keys("***")
        driver.find_element_by_id("login_password").send_keys("***")
        driver.find_element_by_id('login').click()
        sleep(3)
        ##进入TargetManage
        driver.find_element_by_id('targetManagerUrl').click()
        ##根据自己的项目名称重新复制xpath
        driver.find_element_by_xpath(
            '/html/body/div/div/section/div/div/div[4]/div[1]/div[2]/table/tbody/tr[2]/td[1]/h5/a').click()
        sleep(3)
        driver.find_element_by_id('addDeviceTargetUserView').click()
        sleep(3)
        js = "document.getElementById('uploadFile').disabled=false"
        driver.execute_script(js)

        #driver.find_element_by_id('uploadFile').send_keys("02_P57_T4")
        driver.find_element_by_id('targetImgFile').send_keys(filename)
        driver.find_element_by_id('targetDimension').send_keys(1)
        #driver.find_element_by_id('targetName').send_keys("02_P57_T4")
        sleep(3)
        driver.find_element_by_id('AddDeviceTargetBtn').click()
        sleep(5)
        image=driver.find_element_by_xpath('/html/body/div/div/section/div/div/div[18]/div[2]/div[2]/table/tbody/tr[2]/td[2]/h5/img').get_attribute('alt')
        if(image in filename):
            return True
        else:
            return False
    except:
        return False
    finally:
        driver.quit()

#bool=upfile('C:\\Users\\h1186\\Desktop\\a04\\02_P57_T4.jpg')
#os.remove(path+'02_P57_T4.jpg')
#123    25   148   245 
def gogo():
    files=os.listdir(path)
    for file in files:
        bool = upfile(path+file)
        if(bool):
            os.remove(path+file)
        else:
            gogo()

gogo()