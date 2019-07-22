# 抓取糗事百科热门段子
# 过滤带有图片的段子

import requests
from headers import HEADERS
import re
from multiprocessing import Pool

def get_page(url):
'''获取整个页面'''
    try:
        r = requests.get(url, headers = HEADERS)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except RequestException:
        return None

def parse_one_page(info_list, html):
    # 提取用户名，内容，点赞数和评论数
    pattern = re.compile(r'clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?</a>(.*?)</a>.*?number">(.*?)</i>.*?number">(.*?)</i>', re.S)
    items = pattern.findall(html)
    for item in items:
        haveImg = re.search("img",item[2])
        if not haveImg:
            info_list.append([item[0], item[1], item[3], item[4]])

def print_stdout(info_list):
    for i in range(len(info_list)):
        print('用户名: '+ info_list[i][0].strip() + '\n' +
            '内容: ' + info_list[i][1].strip() + '\n' +
            '点赞数: ' + info_list[i][2].strip() + '  评论数: ' + info_list[i][3].strip() + '\n')
    
def main(page):
    info_list = []
    url = 'https://www.qiushibaike.com/8hr/page/' + str(page)
    html = get_page(url)
    parse_one_page(info_list, html)
    print_stdout(info_list)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1,4)])

