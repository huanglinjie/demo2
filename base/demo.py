#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/10 15:37
# @Author : 黄林杰
# @File : demo.py
# @Software: PyCharm


import urllib.request
from bs4 import BeautifulSoup
request = urllib.request.urlopen('https://www.csdn.net/')
soup = BeautifulSoup(request,'html.parser')
print(type(soup))
print(request)

