		
			


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
    for item in range(1,666):
        url = 'https://pornopics.co/search/amateur-couples/{0}'.format(item)
        print(url)
        html = get_one_page(url)
    
        selector = etree.HTML(html)
        links = selector.xpath('//*[@id="container"]/li/div/div/h5/a/@href')
        for icode in links:
            f_link = "https://pornopics.co/"+icode
            print(f_link)

            html_f = get_one_page(f_link)
            selector2 = etree.HTML(html_f)
            pic_url = selector2.xpath('/html/body/div[2]/div/div[1]/ul/li/div[1]/img/@src')
            for item in pic_url:
                f_url_p =  'https://pornopics.co' + item
                
                with open('t3.txt','a') as file_handle: 
                    file_handle.write(f_url_p)
                    file_handle.write('\n')  
            



