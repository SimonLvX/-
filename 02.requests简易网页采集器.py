# -*- coding:utf-8 -*-

#UA检测：门户网站的服务器会检测对应请求载体的身份标识，如果检测到的身份标识为某一款浏览器，说明该请求为正常的请求，服务器不会拒绝请求
#但是，如果检测到身份标识不是基于某一款浏览器的，则表示为不正常的请求（爬虫）,那么服务器端很有可能拒绝该次请求

#UA:User-Agent (请求载体的身份标识)
#UA伪装：让爬虫对应的请求载体身份标识伪装成某款浏览器


import requests
if __name__ == "__main__":
    #UA伪装:将对应的User-Agent封装到字典中
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,"保存成功！！！")
