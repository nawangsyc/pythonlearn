try:
    score = input('')
    a = ord('0')
    b = ord('9')
    S = ''
    for i in score:
        if a<=ord(i)<=b:
            S += i
            continue
        else:
            break
    s = int(S)
    if 90<= s <=100:
        print("输入成绩属于A级别。\n祝贺你通过考试！")
    elif 80<= s <90:
        print("输入成绩属于B级别。\n祝贺你通过考试！")
    elif 70<= s <80:
        print("输入成绩属于C级别。\n祝贺你通过考试！")
    elif 60<= s <70:
        print("输入成绩属于D级别。\n祝贺你通过考试！")
    elif 0<=s < 60:
        print("输入成绩属于E级别。")
    else:
        print("输入数据有误！")
except ValueError as e:
    print('输入数据有误！')
finally:
    print('好好学习，天天向上！')