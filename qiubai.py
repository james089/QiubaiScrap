# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:31:27 2017

@author: bojun.lin
"""

# -*- coding:utf-8 -*-
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    #Full page
    content = response.read().decode('utf-8')
    #pattern = re.compile('<div class=author clearfix>.*?<h2>(.*?)</h2>.*?<div class=content>.*?<span>(.*?)</span>.*?</div>.*?<div class=stats.*?i class=number>(.*?)</i>(.*?)</span>.*?<span class=dash.*?i class=number>(.*?)</i>(.*?)</a>',re.S)
    #items = re.match(pattern,content)
    soup = BeautifulSoup(content, "html.parser")    
    #print (content)
    #print(soup.prettify())
    #print (soup.find_all("div", class_="content"))
    soup1 = soup.find_all("div", class_="content")
    
    index = 1
    outputString = ""
        
    file = open("Resetul.txt", "w") 
    for p in soup1:
        #outputString += str(("糗百段子：%s \n"%str(index), p.text))
        file.write("糗百段子：%s"%str(index))
        file.write(p.text)
        file.write("\n")
        index+=1

    
    file.close() 
    #Con = "\n糗百段子：".join([p.text for p in soup1])
    #print(Con)
except urllib.error.HTTPError as e:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)