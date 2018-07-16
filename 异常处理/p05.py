# raise案例-1
try:
    print("我爱王晓静")
    print(3.1415926)
    # 手动引发一个异常
    # 注意语法：raise ＥｒｒｏｒＣｌａｓｓＮａｍｅ
    raise ValueError
    print("还没完呀")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行的")