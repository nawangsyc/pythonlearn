'''
《命运》和《寻梦》都是著名科幻作家倪匡的科幻作品。这里给出一个《命运》和《寻梦》的网络版本，
文件名为“命运-网络版.txt”和“寻梦-网络版.txt”。

问题1：请编写程序，对这两个文本中出现的字符进行统计，字符与出现次数之间用冒号:分隔，
将两个文件前 100 个最常用字符分别输出保存到“命运-字符统计.txt”和“寻梦-字符统计.txt”文件中，
该文件要求采用 CSV 格式存储，参考格式如下（注意，不统计回车字符）：

命:90, 运:80, 寻:70, 梦:60
（略）

问题2：请编写程序，对“命运-字符统计.txt”和“寻梦-字符统计.txt”中出现的相同字符打印输出。
“相同字符.txt”文件中，字符间使用逗号分隔。

'''

from collections import Counter
def getTxt1():
    txt1 = open('命运-网络版.txt','r',encoding = 'utf-8').read()
    return txt1
def getTxt2():
    txt2 = open('寻梦-网络版.txt', 'r',encoding = 'utf-8').read()
    return txt2
mingyunTxt = getTxt1()
counter1 = Counter(mingyunTxt)
del counter1['\n']
del counter1['\u3000']
ls1 = list(counter1.items())
ls1.sort(key = lambda x:x[1],reverse = True)
ls3 = []
for i in range(100):
    k,v = ls1[i]
    ls3.append("{}:{}".format(k,v))
f1 = open('命运-字符统计.txt','w')
f1.write(','.join(ls3))
f1.close()

xunmengTxt = getTxt2()
counter2 = Counter(xunmengTxt)
del counter2['\n']
del counter2['\u3000']
ls2 = list(counter2.items())
ls2.sort(key = lambda x:x[1],reverse = True)
ls4 = []
for i in range(100):
    k,v = ls2[i]
    ls4.append("{}:{}".format(k,v))
f2 = open('寻梦-字符统计.txt','w')
f2.write(','.join(ls4))
f2.close()