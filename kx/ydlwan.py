import pandas as pd
import numpy as np
import os
f = open(r'D:/gzy.txt','r')
a=[i for i in f]
f.close()
list1 = a
list2 = []
for i in list1:
    if not i in list2:
        list2.append(i)
lt = list2
n= len(lt)
for x in range(n-1):
   for y in range(n-1-x):
      if lt[y]>lt[y+1]:
         lt[y],lt[y+1]=lt[y+1],lt[y]
print(lt)
count = 0
sum = 0
catalog = open(r"C:\Users\GZY\PycharmProjects\pythonProject14\kx\rng.py","rb")
t = len(catalog.readlines())#统计行数
for line in catalog.readlines():
    line = line.strip()     #去掉每行头尾空白
    print(line)
    if line == "":
        count += 1
    if line.startswith("#"):    #startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
        sum += 1
print("统计的文件行数为：%d行" %t)
g = np.arange(1,t+1)
del(list2[0])
list2 = list(map(int,list2))
c = len(list2)
i=0
while i<c-1:
	j=i+1
	while j<c:
		if int(list2[j])<int(list2[i]):
			tem=list2[j]
			list2[j]=list2[i]
			list2[i]=tem
			j=i
		j=j+1
	i=i+1
if t in list2:
    o = len(list2)
    e = list2.index(t)
    q=e+1
    del(list2[q:o])
    print(list2)
else:
    list2.insert(0, t)
    list2.sort()
    o = len(list2)
    e = list2.index(t)
    q = e + 1
    del (list2[q:o])
    list2.pop()
    print(list2)
s=0
p = len(list2)
y=0
list3=[]
while s < t :
      list3.insert(s,0)
      s=s+1
print(list3)
print(len(list3))
while y<p:
      b=list2[y]-1
      list3[b]=1
      y=y+1
print(list3)
df = pd.DataFrame({'语句':g,'覆盖':list3})
df = df.set_index('语句')
df.to_excel('D:/ydl.xlsx')
my_file = 'D:/gzy.txt' # 文件路径
if os.path.exists(my_file): # 如果文件存在
    #删除文件，可使用以下两种方法。
    os.remove(my_file) # 则删除
else:
    print('no such file:%s'%my_file)
os.startfile('D:/ydl.xlsx')

