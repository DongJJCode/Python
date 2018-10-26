# -*- coding: utf-8 -*-

# @Time : 2018/10/26 15:55

# @Author : "DongJJ"

# @File : 01_save_jpg.py

import requests

# 发送请求
repsonse = requests.get("https://www.baidu.com/img/bd_logo1.png?where=super")

# 保存

with open("a.jpg", "wb") as f :
    f.write(repsonse.content)



