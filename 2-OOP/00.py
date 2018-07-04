
class Person():
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def fgetName(self):
        return self._name * 3

    def fsetName(self,name):
        self ._name = name.upper()

    def fgetAge(self):
        return self._age

    def fsetAge(self,age):
        self ._age = int(age)

    Name = property(fgetName, fsetName,'对name进行操作')
    Age = property(fgetAge,fsetAge,"对age进行操作")


class Person():

    def __init__(self, name, age): # 初始化函数
        pass

    def fgetName(self):
        return self._name * 3

    def fsetName(self, name):
        self._name = name.upper()

    def fgetAge(self):
        return self._age

    def fsetAge(self, age):
        self._age = int(age)

    Name = property(fgetName, fsetName, '对name进行操作')
    Age = property(fgetAge, fsetAge, "对age进行操作")
