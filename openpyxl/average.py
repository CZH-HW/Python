import os
import numpy as np
import time
from openpyxl import load_workbook 


def get_average(ws):
    """求平均值"""
    # 使用 WorkSheet 的 Cell(单元格)方法
    # 以列 j 为基准，以行数 i 运算
    for j in range(1,10):
        for i in range(0,7200):
            p = np.zeros(100)
            t = 0

            for m in range(0,100):
                if ws.cell(row = m*7200+i+4, column = j).value == None:
                    p[m] = 0
                else:
                    t += 1
                    p[m] = ws.cell(row = m*7200+i+4, column = j).value

            ws.cell(row = i+4, column = j+12, value = np.sum(p)/t)


def get_data(ws):
    """隔n行取值"""
    for j in range(2,11):

        for i in range(0,720):
            v = ws.cell(row = i*10+4, column = j).value
            ws.cell(row = i+4, column = j+12, value = v)


if __name__ == '__main__':
    # 以列表形式返回当前目录下所有文件和目录
    files = os.listdir()
    for f in files:
        try:
            a = time.time()
            # 导入一个Workbook,Workbook相当于一个文件
            wb = load_workbook(f)
            # 获取默认打开的(active)的WorkSheet
            ws = wb.active
            #get_average(ws)
            get_data(ws)
            # 保存文件 
            wb.save(f)
            b = time.time()
            print(str(b-a) + 's' + '   ' + f + ' fished')
            print()
        except:
            continue   