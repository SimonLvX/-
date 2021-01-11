#-*- coding:utf-8 -*-

import requests
import json
if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    #post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    response = requests.post(url=post_url,data=data,headers=headers)
    #获取相应数据:json()方法返回的是obj（确认返回数据是json格式，才可以使用json()方法）
    dic_obj = response.json()
    print(dic_obj)

    #持久化存储
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over!!!')
