# 从东方财富网获取股票名称和代码
# 再从百度股市通获取股票的最新报价等相关参数，保存到数据库

import requests
import re
from bs4 import BeautifulSoup
import traceback

def get_html_text(url):
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text 
    except RequestsException:
        return None

def get_stock_list(stock_lists, stock_list_url):
    # 获取股票的代码
    html = get_html_text(stock_list_url)
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all('a')
    for i in range(len(a)):
        # findall可能找不到内容，故用try...except...
        try:
            item = a[i].attrs['href']
            stock_lists.append(re.findall(r'/(s[hz].*?).html',item)[0])
        except:
            continue
    del stock_lists[0]        

def get_stock_info(stock_lists, stock_info_url):
    # 获取股票当日的信息
    for stock in stock_lists:
        try:
            html = get_html_text(stock_info_url + stock + '.html')
            info_dict = {}
            soup = BeautifulSoup(html, 'lxml')
            stock_info = soup.find('div', attrs = {'class':'stock-bets'})

            name = stock_info.find(attrs = {'class':'bets-name'})
            info_dict.update({'股票名称':name.text.split()[0]})

            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                value = value_list[i].text.strip()
                info_dict[key] = value
            
        except:
            traceback.print_exc()
            continue
    
def main():
    stock_lists = []
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    get_stock_list(stock_lists, stock_list_url)
    get_stock_info(stock_lists, stock_info_url)

if __name__ == '__main__':
    main()
    
    









