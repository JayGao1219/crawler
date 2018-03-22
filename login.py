#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a login model'

__author__='Jay Gao 1219'

from selenium import webdriver;

login_url='https://www.itjuzi.com/user/login'

def login(Explorer,flag):#flag表示是否是第一次调用
    if flag==False:
        Explorer.find_element_by_id('loginurl').click()
        pass;
    else:
        Explorer.get(login_url)
        pass;
    Explorer.implicitly_wait(30)
    Explorer.find_element_by_css_selector('input[name="identity"]').send_keys("13615884019")
    Explorer.find_element_by_css_selector('input[name="password"]').send_keys("Ccissy_586489")
    Explorer.find_element_by_id('login_btn').click()
    pass;

if __name__=='__main__':
    Explorer=webdriver.Chrome();
    login(Explorer,True)
    print("login succeed")
    Explorer.quit()
    pass;
