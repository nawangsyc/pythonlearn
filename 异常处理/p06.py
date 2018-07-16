# raise案例-2
# 自己定义异常
# 需要注意：　自定义异常必须是系统异常的子类
class DanaValueError(ValueError):
    pass

try:
    print("我爱王晓静")
    print(3.1415926)
    # 手动引发一个异常
    # 注意语法：raise　ＥｒｒｏｒＣｌａｓｓＮａｍｅ
    raise DanaValueError
    print("还没完呀")
except NameError as e:
    print("NameError")
except DanaValueError as e:
    print('DanaValueError')
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行的")