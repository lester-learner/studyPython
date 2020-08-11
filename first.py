import second


def outer():
    name = "i am outer"

    def inner():
        print(name)
        print("i am inner")

    return inner()


outer()

# li = ['a', 'b', 'c', '\ ', 'n', 'd']
# j = 0
# for i in li:
#     print(i)
#     print(j)
#     if j == '\ ' and i == 'n':
#         print("!!!!!!!!!!!!!")
#     j = i
#     print("---------")

j = 0
with open(
        'C:/Users/Leste/Desktop/test.txt',
        mode='r+',
        encoding='utf-8',
) as f:

    f.seek(0, 0)
    f.read()
    print(f.read())
    f.write(input())
    print(f.read())
    n = list(f.read())
    # print("！！！！！！！！！！！！！")
    print(n)
    for i in n:
        if j == ' ' and i == 'n':
            print("！！！！！！！！！！！！！")
            f.write('\n')
            print(f.read())
            print(n)
        j = i

print(f.closed)
