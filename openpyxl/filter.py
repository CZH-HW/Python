# -*- coding:utf-8 -*-

import numpy as np
from openpyxl import load_workbook 
# 导入一个Workbook,Workbook相当于一个文件
wb = load_workbook('Workbook1.xlsx')
# 获取默认打开的(active)的WorkSheet
ws = wb.active

# 滤波器的采样频率fs和滤波截止频率fc
fs = 1750 * 7.2/120 
fc = 5.0
# 滤波器阶数n1		 
n1 = int(2 * fs/fc + 1)
# 数组初始化
c = np.zeros(7200)
h = np.zeros(7200)
k = np.zeros(7200)
for u in range(0, 7200):
	# 滤波函数
	if u > 0:
		c[u] = -np.sin(2 * np.pi * u * fc/fs)/(np.pi * u)
	else:
		c[u]= 1 - 2 * fc/fs
	# hanning窗函数
	h[u] = 1.0/2 * (1 + np.cos(2 * np.pi * u/(2 * n1 + 1)))	
    # k数组赋值
	k[u] = h[u] * c[u]

# 使用WorkSheet的Cell(单元格)方法
# 以列为基准，以行数运算
for m in range(26,30):
	# 创建数组并初始化
	p = np.zeros(7200)
	ph = np.zeros(7200)

	for n in range(2,7202):
		# p数组赋值
		p[n-2] = ws.cell(row = n, column = m).value
	
	# 滤波前的最高压力
	print("滤波前最高压力:", np.amax(p))
		
	for t in range(0,7200):
		for j in range(t-n1, t+n1+1):
			if j < 0 or j > 7199:
				ph[t] += 0
			else:
				ph[t] += k[j] * p[j]
	

	# 滤波后的最高压力
	print("滤波后最高压力:", np.amax(ph))
	# 滤波后的最低压力
	print("滤波后的最低压力:", np.amin(ph))
	# 滤波后压力的最大幅值
	print("滤波后压力的最大幅值:", np.ptp(ph))
	print()
	
	
	# 给选中单元格赋值
	for n in range(2,7202):
		ws.cell(row = n, column = m+5, value = ph[n-2])

# 保存文件 
wb.save('Workbook1.xlsx') 