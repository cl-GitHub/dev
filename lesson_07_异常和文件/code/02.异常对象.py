print('异常出现前')
l = []
try:
    # print(c)
    # l[10]
    # 1 + 'hello'
    print(10/0)
except NameError:
    # 如果except后不跟任何的内容，则此时它会捕获到所有的异常
    # 如果在except后跟着一个异常的类型，那么此时它只会捕获该类型的异常
    print('出现 NameError 异常')
except ZeroDivisionError:
    print('出现 ZeroDivisionError 异常')
except IndexError:
    print('出现 IndexError 异常')
# Exception 是所有异常类的父类，所以如果except后跟的是Exception，他也会捕获到所有的异常
# 可以在异常类后边跟着一个 as xx 此时xx就是异常对象
except Exception as e :
    print('未知异常',e,type(e))
finally :
    print('无论是否出现异常，该子句都会执行')

print('异常出现后')

# coding:utf-8
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

# 用列表生成式，生成新的列表
b = [i for i in a if i > 0]
print("大于0的个数：%s" % len(b))

c = [i for i in a if i < 0]
print("小于0的个数：%s" % len(c))
