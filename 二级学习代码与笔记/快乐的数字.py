# 描述
# 编写一个算法来确定一个数字是否“快乐”。 快乐的数字按照如下方式确定：从一个正整数开始，用其每位数的平方之和取代该数，并重复这个过程，直到最后数字要么收敛等于1且一直等于1，要么将无休止地循环下去且最终不会收敛等于1。能够最终收敛等于1的数就是快乐的数字。

# 例如: 19
# 就是一个快乐的数字，计算过程如下：

# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 当输入时快乐的数字时，输出True，否则输出False。

# 输入
# 示例1：19

# 输出
# 示例1：True
try:
    def happy():
        N = eval(input())
        ifHappy(N)
    def ifHappy(n):
        if n==1:
            print(True)
        else:
            value = str(n)
            num = 0
            for i in range(len(value)):
                num += int(value[i])**2
            ifHappy(num)
    if __name__ == '__main__':
        happy()
except:
    print(False)