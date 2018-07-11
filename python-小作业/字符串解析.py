formula = input('请输入公式：')
value = input('你输入的数值是：')
ready = formula.replace('x', value)
ops = []
expression = []
stack_value = []
ops_rule = {'+': 1,'-': 1,'*': 2,'/': 2,'^': 3}
# 将字符串转换成逆波兰表达式
def middle_to_after(ready):
    for item in ready:
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
def expression_to_value(expression):
    for item in expression:
        if item in ['+', '-', '*', '/', '^']:
            n2 = stack_value.pop()
            n1 = stack_value.pop()
            result = cal(n1, n2, item)
            stack_value.append(result)
        else:
            stack_value.append(int(item))
    return stack_value[0]


def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    if op == '^':
        return n1 ** n2


middle_to_after(ready)
expression_to_value(expression)
print('计算的结果为：{0}'.format(stack_value[0]))