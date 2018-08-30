# 描述
# 获得用户输入的整数n，输出
# 1!+2!+... + n!的值。

# 如果输入数值为0、负数、非数字或非整数，输出提示信息：输入有误，请输入正整数。

# 输入格式
# 使用input()
# 获得系统输入，不增加额外的提示信息。


try:
    N = input('')
    N.isdigit()==True
    n = int(N)
    if n>0:
        sum = 0
        for j in range(1, n+1):
            m = 1
            for k in range(1, j + 1):
                m *= k
                continue
            sum += m
            continue
        print(sum)
    else:
        print('输入有误，请输入正整数。')
except ValueError as e:
    print('输入有误，请输入正整数。')