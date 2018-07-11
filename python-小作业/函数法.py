while True:
    formula = input('请输入公式,公式的变量可以是x或者X：')
    formula = formula.lower()
    value = input('你输入的数值是：')
    value = float(value)
    x = value
    print('结果为:', eval(formula))
    cmd = input("继续吗?是\\否 ")
    cmd = cmd.lower()
    if '否' == cmd:
        break

formula = input('请输入公式：')
value = input('你输入的数值是：')
value = float(value)
x = value
z = eval(formula)
print('结果为:', z)