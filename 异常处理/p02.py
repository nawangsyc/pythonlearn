# 简单异常案例
try:
    num = int(input('Plz input your number:'))
    rst = 100/num
    print('计算结果是:',rst)

except:
    print('你输入的啥？')
    # exit是退出程序的意思
    exit()


