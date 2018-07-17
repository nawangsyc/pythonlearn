## python3 windows 中显示中文时间时遇到的问题

### 一出现中文就报错
- 代码
        t = time.localtime()
        ft = time.strftime('%Y年%m月%d日 %H:%M',t)
        print(ft)
        
- 报错信息
    - UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: Illegal byte sequence
    
- 解决办法
    - [1](https://segmentfault.com/q/1010000003070325)
    - [2](https://blog.csdn.net/imnisen1992/article/details/53333212)

## windows中system()使用
- [windows常用新建文件命令](https://blog.csdn.net/qiang123___/article/details/78443932)
- [Windows中用“ls”命令](https://blog.csdn.net/qq1987924/article/details/7875994)