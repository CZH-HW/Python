'''
  Created on Jan 25, 2018
'''

import requests
import hashlib
import time
import random

def createData(transStr):
    '''
    i：需要进行翻译的字符串
    salt：加密用到的盐，就是f变量，时间戳
    sign：签名字符串，使用的是(u + d + f + c)的md5的值

    d：代表的是需要翻译的字符串。
    f：当前时间的时间戳加上0-10的随机字符串。
    u：一个常量——"fanyideskweb"。
    c：一个常量——"rY0D^0'nM0}g5Mm1z%1G4"。
    '''
    salt = str(int(time.time()*1000) + random.randint(1,10))
    u = 'fanyideskweb'
    c = "rY0D^0'nM0}g5Mm1z%1G4"
    digStr = u + transStr + salt + c

    m = hashlib.md5()      # 构造hash对象
    m.update(digStr.encode('utf-8'))
    sign = m.hexdigest()

    data = {
        'i': transStr ,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'true'
    }
    return data

def getTransCont(FormData):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    try:
        re = requests.post(url, data = FormData, headers = headers)
        re.raise_for_status()
        re.encoding = 'utf-8'
        return re.json()
    except:
        print('翻译未成功')


if __name__ == '__main__':
    KeepOn = True
    while KeepOn:
        ip = input('是否进行查询或退出，Y or N :\n')
        if ip is not 'Y':
            break
        
        transStr = input('请输入需要翻译的中文或者英文:\n')
        FormData = createData(transStr)
        json = getTransCont(FormData)

        if json:
            print('翻译结果:')
            print(json['translateResult'][0][0]['tgt'])
            print()
    

