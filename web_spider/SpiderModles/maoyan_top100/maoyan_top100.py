# 抓取猫眼电影top100的信息并保存在txt文件中

import requests
from requests.exceptions import RequestException
import re 
import time
from multiprocessing import Pool

def get_one_page(url):
    # 获取网页内容，处理异常
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except RequestException:
        return None

def parse_one_page(info_list, html):
    # 获取排名，电影名称，图片地址，主演，上映时间，评分
    indexs = re.findall(r'<dd>.*?board-index.*?">(\d+)</i>', html, re.S)
    titles = re.findall(r'</i>.*?<a.*?title="(.*?)"', html, re.S)
    pictures = re.findall(r'<img data-src="(.*?)".*?/>', html, re.S)
    actors = re.findall(r'star">(.*?)</p', html, re.S)
    times = re.findall(r'releasetime">(.*?)</p>', html, re.S)
    integers = re.findall(r'integer">(.*?)</i>', html, re.S)
    fractios = re.findall(r'fraction">(.*?)</i>', html, re.S)
    for i in range(len(indexs)):
        info_list.append({'index':indexs[i], 'title':titles[i], 'picture_adress':pictures[i],
                'actor':actors[i].strip()[3:], 'time':times[i].strip()[5:], 'grade':integers[i]+fractios[i]})  

def write_to_file(info_list):
    # 将获取的信息输入到文件中
    with open('mytop.txt','a') as file:
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write('搜索时间:'+ localtime + '\n')
        for i in range(len(info_list)):
            file.write(str(info_list[i]) + '\n')

def main(page):
    info_list = []
    url = 'http://maoyan.com/board/4?offset=' + str(page)
    html = get_one_page(url)
    parse_one_page(info_list, html)
    write_to_file(info_list)

if __name__ == '__main__':
    a = time.time()
    # 多进程，顺序不太一样
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
    b = time.time()
    print(str(b-a)+'s')

"""
# 不使用多进程
def main():
    info_list = []
    for page in range(10):
        url = 'http://maoyan.com/board/4?offset=' + str(page * 10)
        html = get_one_page(url)
        parse_one_page(info_list, html)
    write_to_file(info_list)

if __name__ == '__main__':
    main()
"""



