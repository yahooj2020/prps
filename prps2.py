
#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import wget
import os
import codecs

def get_one_page(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except :
        return None





if __name__ == "__main__":
    f_list = []
    for item in range(1,491):
        url = 'https://pornopics.co/search/asian-juicy/{0}'.format(item)
        html = get_one_page(url)
    
        selector = etree.HTML(html)
        links = selector.xpath('//*[@id="container"]/li/div/div/h5/a/@href')
        for icode in links:
            f_link = "https://pornopics.co/"+icode

            html_f = get_one_page(f_link)
            selector2 = etree.HTML(html_f)
            pic_url = selector2.xpath('/html/body/div[2]/div/div[1]/ul/li/div[1]/img/@src')
            for item in pic_url:
                f_url_p =  'https://pornopics.co' + item
                f_list.append(f_url_p)
    for single_pic in f_list:
        with open('t2.txt','a') as file_handle: 
              # .txt可以不自己新建,代码会自动新建

            file_handle.write(single_pic)     # 写入
            file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据








