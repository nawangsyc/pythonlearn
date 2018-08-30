names = ["命运", "寻梦"]
for name in names:
    fi = open(name+"-网络版.txt", "r", encoding="utf-8")
    fo = open(name+"-字符统计.txt", "w", encoding="utf-8")
    txt = fi.read()
    d = {}
    for c in txt:
        d[c] = d.get(c, 0) + 1
    del d['\n']
    ls = list(d.items())
    ls.sort(key=lambda x:x[1], reverse=True)
    for i in range(100):
        ls[i] = "{}:{}".format(ls[i][0], ls[i][1])
    fo.write(",".join(ls[:100]))
    fi.close()
    fo.close()