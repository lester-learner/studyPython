# 如果 a+b+c=1000，且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有a,b,c可能的组合
from timeit import Timer


# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print("a=%d : b=%d : c=%d" % (a, b, c))
# end_time = time.time()
# print("程序运行的时间：", end_time-start_time)


# def test_extend_time():
#     li = []
#     for i in range(1000):
#         li.extend([i])


# def test_add_time():
#     li = []
#     for i in range(1000):
#         li = li + [i]


# def test_append_time():
#     li = []
#     for i in range(1000):
#         li.append(i)


# def test_insert_time():
#     li = []
#     for i in range(1000):
#         li.insert(0, i)


# get_extend_timer = Timer('test_extend_time()', 'from __main__ import test_extend_time')
# print('get_extend_timer: ', get_extend_timer.timeit(1000))

# get_add_timer = Timer('test_add_time', 'from __main__ import test_add_time')
# print('get_add_timer: ', get_add_timer.timeit(1000))

# get_append_timer = Timer('test_append_time()', 'from __main__ import test_append_time')
# print('get_append_timer: ', get_append_timer.timeit(1000))

# get_insert_timer = Timer('test_insert_time', 'from __main__ import test_insert_time')
# print('get_insert_timer: ', get_insert_timer.timeit(1000))

li = [1, 2, 3, 4, 5]
li2 = [0000]
print("我是原始列表：", li)
li.append(li2)
print("我是插入列表：", li)
li2[0] = 99999
print("我是插入后原始列表修改后的：", li)

# li.append(li2)
# print(li)
# li2[0] = 9
# print(li)


