# 简单异常案例
from collections import Counter
f0 = open('天龙八部-网络版.txt','r',encoding='utf-8')
f1 = open('天龙八部-汉字统计.txt','w',encoding='utf-8')
txt = f0.read()
c = Counter(txt)
del c['\n']
del c['\u3000']
ls=[]
for k,v in c.items():
    ls.append("{}:{}".format(k,v))
print(ls)
f1.write(",".join(ls))
f0.close()
f1.close()





