import requests 
import bs4 
from bs4 import BeautifulSoup

def get_university_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fill_university_list(ulist, html):
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')     
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def print_university_list(ulist, num):
    tplt = '{0:^10}\t{1:{3}^20}\t{2:^10}'
    print(tplt.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        print(tplt.format(ulist[i][0],ulist[i][1],ulist[i][2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    html = get_university_html(url)
    fill_university_list(uinfo, html)
    print_university_list(uinfo, 80)
    
main()
