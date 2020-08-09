class Person:
    def who(self):
        print(self)

        
zhangsan = Person()
#第一种方式
zhangsan.who()
#第二种方式
who = zhangsan.who
who()#通过 who 变量调用zhangsan对象中的 who() 方法