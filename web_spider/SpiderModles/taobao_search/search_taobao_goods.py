import requests
import re

def get_html_text(url, i):
    # 获取url的文本信息
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        r = requests.get(url, headers = headers, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('第'+ str(i) + '页的内容没有加载')
        return ''
    
def parse_page(infolist, html):
    # 从商品页面信息中获取商品的名称和价格
    try:
        prices_list = re.findall(r'"view_price":"([\d]*\.[\d]{2})"', html)
        titles_list = re.findall(r'"raw_title":"(.*?)"', html)
        for i in range(len(prices_list)):
            infolist.append([prices_list[i], titles_list[i]])
    except:
        print('')

def print_goods_list(infolist):
    # 打印商品名称和价格,按照价格升序排列
    infolist = sorted(infolist, key = lambda x : float(x[0]))
    tplt = '{0:4}\t{1:8}\t{2:30}'
    print(tplt.format('序号','价格','商品名称'))
    for i in range(len(infolist)):
        print(tplt.format(i+1, infolist[i][0], infolist[i][1]))

def main():
    goods = '笔记本电脑'
    depth = 2
    infolist = []
    for i in range(5):
        start_url = 'https://s.taobao.com/search?q=' + goods + '&s=' + str(i * 44)
        try:
            html = get_html_text(start_url, i)
            parse_page(infolist, html)
        except:
            continue
    print_goods_list(infolist)

main()


