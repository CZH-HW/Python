# 从电影天堂获取某种类型电影的电影名，BT资源地址等相应信息
# 将信息存储在mysql数据库中

import requests
from bs4 import BeautifulSoup
import pymysql


def get_html(url):
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = 'gb2312'
        return r.text
    except:
        return None


def get_info(html, info_list):
    # 获取相应信息
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all('a', attrs = {'class' : 'ulink'})
    for i in range(len(a)):
        try:
            info_list.append([a[i].get_text(), 'http://www.dytt8.net/' + a[i].attrs['href']])
        except:
            continue


def save_mysql(info_list):
    # 将数据存储到数据库
    conn = pymysql.connect(
                            host = 'localhost', 
                            port = 3306, 
                            user = 'root', 
                            password = 'czhsql', 
                            db = 'film', 
                            charset = 'utf8'
                            )
    cur = conn.cursor()
    for i in range(len(info_list)):
        try:
            cur.execute("insert into dytt_film values('%d', '%s', '%s')"%(i+1, info_list[i][0], info_list[i][1]))
            conn.commit()
        except:
            conn.rollback()
            

def main():
    info_list = []
    start_url = 'http://www.dytt8.net/html/gndy/rihan/list_6_'

    for i in range(1, 11):
        html = get_html(start_url + str(i) + '.html')
        get_info(html, info_list)
    save_mysql(info_list)

if __name__ == '__main__':
    main()
