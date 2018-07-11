formula = input('请输入公式：')
value = input('你输入的数值是：')
ready = formula.replace('x', value)

# 将操作符与操作数用空格隔开
ready1 = []
def operator_separate_operand(ready):
    for item in ready:
        if item in ['+', '-', '*', '/', '^']:
            ready1.append(' ')
            ready1.append(item)
            ready1.append(' ')
        else:
            ready1.append(item)
operator_separate_operand(ready)
ready2 =  "".join(ready1)

# 将字符串转换成逆波兰表达式
ready3 = ready2.split(' ')
expression = []
ops = []
ops_rule = {'+': 1,'-': 1,'*': 2,'/': 2, '^': 3}
def middle_to_after(ready3):
    for item in ready3:
        if item in ['+', '-', '*', '/', '^']:
            while len(ops) >= 0:
                if len(ops) == 0:
                    ops.append(item)
                    break
                op = ops.pop()
                if op == '(' or ops_rule[item] > ops_rule[op]:
                    ops.append(op)
                    ops.append(item)
                    break
                else:
                    expression.append(op)
        elif item == '(':
            ops.append(item)
        elif item == ")":
            while len(ops) > 0:
                op = ops.pop()
                if op == '(':
                    break
                else:
                    expression.append(op)
        else:
            expression.append(item)
    while len(ops) > 0:
        expression.append(ops.pop())
    return expression

# 计算逆波兰表达式
stack_value = []
stopMark = False
def abc(expression):
    global stopMark
    for item in expression:
        if item in ['+', '-', '*', '/', '^']:
            n2 = stack_value.pop()
            n1 = stack_value.pop()
            result = cal(n1, n2, item)
            if stopMark:
                stack_value.clear()
                break
            else:
                stack_value.append(result)
        else:
            stack_value.append(int(item))
    if stopMark:
        return None
    else:
        return stack_value[0]
def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        if n2 == 0:
            global stopMark
            stopMark = True
            print('error: 除数不可为0')
            return 0
        else:
            return n1/n2
    if op == '^':
        return n1 ** n2
middle_to_after(ready3)
abc(expression)
print('计算的结果为：{0}'.format(stack_value[0]))