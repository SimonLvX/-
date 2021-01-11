#-*- coding:utf-8 -*-

import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    word = input('enter a eord:')
    data = {
        'op':'keyword',
        'cname':'',
        'pid':'',
        'keyword': word,
        'pageIndex': '1',
        'pageSize': '10'
    }

    response = requests.post(url=url,data=data,headers=headers)
    text_data = response.text
    fp = open('./KFC.json','w',encoding='utf-8')
    json.dump(text_data,fp=fp,ensure_ascii=False)
    print('over!!!')
