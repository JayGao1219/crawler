#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Jay Gao 1219'

from selenium import webdriver;
import datetime
import random
import login
import time

now=datetime.datetime.now()

def prework(name):
    w=[]
    f=open(name)
    cur=f.read()
    cur=cur.split('\n')
    for cc in cur:
        if cc:
            w.append(eval(cc))
            pass;
        pass;
    return w;

def wait(Explorer):
    Explorer.implicitly_wait(20)
    pass

def show(obj,f):
    f.write(str(obj))
    f.write('\n')
    pass;

def handle(obj,Explorer,f):
    cur={}
    already=['name','info','keys','finance_size','website']
    for i in range(len(already)):
        cur[already[i]]=obj[i]
        pass;
    Explorer.get(cur['website'])
    wait(Explorer)
    part=Explorer.find_element_by_css_selector('div.des\-more').text.split('\n')
    part[0]=part[0].split(' ')
    cur['base_name']=part[0][0]
    p1=part[0][1].find('：')
    p2=part[0][2].find('：')
    cur['begin_time']=part[0][1][p1+1:]
    cur['size']=part[0][2][p2+1:]
    cur['state']=part[1]
    #获取融资信息
    try:
        fin=[]
        already=['date','investment','money','company']
        part=Explorer.find_elements_by_css_selector('tr.feedback\-btn\-parent')
        for p in part:
            cp={}
            pp=p.find_elements_by_css_selector('td')
            for i in range(4):
                cp[already[i]]=pp[i].text
                pass;
        cp['detail_url']=pp[1].find_element_by_css_selector('a').get_attribute('href')
        fin.append(cp)
        cur['finance_detail']=fin
        #获取团队成员的信息
        tea=[]
        part=Explorer.find_element_by_css_selector('ul[class="list-unstyled team-list limited-itemnum"]')
        part=part.find_elements_by_css_selector('li')
        for p in part:
            cp={}
            pn=p.find_element_by_css_selector('a.person\-name')
            cp['name']=pn.text
            cp['detail_url']=pn.get_attribute('href')
            cp['position']=p.find_element_by_css_selector('div.per\-position').text
            cp['info']=p.find_element_by_css_selector('div.per\-des').text
            tea.append(cp)
            cur['team']=tea
            pass;
        pass;
    except Exception:
        pass;
    #获取产品信息
    try:
        pro=[]
        part=Explorer.find_element_by_css_selector('ul[class="list-unstyled product-list limited-itemnum"]')
        part=part.find_elements_by_css_selector('li')
        for p in part:
            cp={}
            cp['name']=p.find_element_by_css_selector('a.product\-name').text
            cp['info']=p.find_element_by_css_selector('div[class="product-des line2"]').text
            cp['detal_url']=p.find_element_by_css_selector('a.product\-name').get_attribute('href')#目前这个网址无法打开
            pro.append(cp)
            cur['products']=pro;
            pass;
        pass;
    except Exception:
        pass;
    #获取竞品信息
    try:
        com=[]
        already=['name','place','date','investment','money']
        part=Explorer.find_element_by_css_selector('ul[class="list-main-icnset list-compete-info"]')
        part=part.find_elements_by_css_selector('li')
        for p in part:
            cp={}
            pp=p.find_elements_by_css_selector('span')
            for i in range(1,6):
                cp[already[i-1]]=pp[i].text
                pass;
        cp['detail_url']=p.find_element_by_css_selector('p.title a').get_attribute('href')
        com.append(cp)
        cur['competition_products']=com
        pass;
    except Exception:
        pass;
    #获取工商信息
    try:
        js="var a=document.getElementById('indus_shareholder');a.setAttribute('class','tab-pane fade bussiness_main active in');var a=document.getElementById('indus_foreign_invest');a.setAttribute('class','tab-pane fade bussiness_main active in');var a=document.getElementById('indus_busi_info');a.setAttribute('class','tab-pane fade bussiness_main active in');"
        Explorer.execute_script(js)
        time.sleep(1)
        part=Explorer.find_elements_by_css_selector('table[class="table table-bordered"]')
        already=['base','shareholder','foreign_invest','busi_info']
        for i in range(len(already)):
            cur[already[i]]=part[i].text
            pass;
        pass;
    except Exception:
        pass;
    try:
        part=Explorer.find_element_by_css_selector('div[id="legal-proceedings"]')
        part=part.find_element_by_css_selector('table')
        cur['law']=part.text
        pass;
    except Exception:
        pass;
    show(cur,f)

def investment():
    filename='./data/'+str(now.microsecond)
    filename=filename+'.txt'
    f=open(filename,'w')
    f1=open('histry.txt','w')
    whole=[]
    whole=prework('1.txt')
    browser=webdriver.Chrome()
    login.login(browser,True)
    i=0
    for ww in whole:
        i=i+1
        if i<1391:
            continue
        print(i)
        time.sleep(1+random.uniform(0,1))
        handle(ww,browser,f)
        f1.write(str(i))
        f1.write('\n')        

if __name__=='__main__':
    investment()
    pass;
