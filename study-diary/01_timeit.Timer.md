@[TOC]( Timeit.Timer 和insert 和 append 插入元素问题 )
## Python: Timeit.Timer()  内置类型性能分析
###  1. Syntactic Structure
```javascript
from timeit import Timer
Timer(stmt='pass', setup='pass', timer=<timer function>)
// stmt  ： 要测试的代码语句，封装成函数
// 'pass'： 字符串
// setup ： 引入要测试的函数设置，因为测试需要在另外一个空间进行，
//          那个空间需要引入要测试的函数
// timer :  定时器,
```
### 2. code analysis
```javascript
//进行列表的extend函数封装
def test_extend_time():
    li = []
    for i in range(1000):
        li.extend([i])

//进行列表的相加操作函数封装
def test_add_time():
    li = []
    for i in range(1000):
        li = li + [i]

//进行列表的append函数封装
def test_append_time():
    li = []
    for i in range(1000):
        li.append(i)

//进行列表的insert每次向第一位插入 函数封装
def test_insert_time():
    li = []
    for i in range(1000):
        li.insert(0, i)

//获得测试结果
get_extend_timer = Timer('test_extend_time()', 'from __main__ import test_extend_time')
print('get_extend_timer: ', get_extend_timer.timeit(1000)) //测试1000次


get_add_timer = Timer('test_add_time', 'from __main__ import test_add_time')
print('get_add_timer: ', get_add_timer.timeit(1000))

get_append_timer = Timer('test_append_time()', 'from __main__ import test_append_time')
print('get_append_timer: ', get_append_timer.timeit(1000))

get_insert_timer = Timer('test_insert_time', 'from __main__ import test_insert_time')
print('get_insert_timer: ', get_insert_timer.timeit(1000))

```
### 3. 测试结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811204031902.png)

## Python 关于列表insert 和 append 插入元素问题
insert 和 append 插入元素，更像是插入一个镜像，被插入列表元素会随着原始原始改变而改变
### insert :
```javascript
li = [1, 2, 3, 4, 5]
li2 = [0]
print("我是原始列表：", li)
li.insert(2, li2)
print("我是插入列表：", li)
li2[0] = 9
print("我是插入后原始列表修改后的：", li)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811205152283.png)
### append:
```javascript
li = [1, 2, 3, 4, 5]
li2 = [0000]
print("我是原始列表：", li)
li.append(li2)
print("我是插入列表：", li)
li2[0] = 99999
print("我是插入后原始列表修改后的：", li)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811205300897.png)
