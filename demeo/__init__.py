# str = raw_input("please input:")
#
# str = input('please input\n')
# print('you input content:',str)


# fo = open('foo.txt','w')
# print('file name:',fo.name)
# print('file closed:',fo.closed)
# print('file mode:',fo.mode)
# # fo.close()
# # print('file softspace :',fo.s)
# fo.write("this is write content")
# content = fo.read(10)
# print('read content : '+content)

# Fibonacci

# a,b = 0,1
# while a<10:
#     print(a)
#     a,b = b,a+b



# if
# x = int(input('please  enter an integer:'))
# if x<0:
#     x = 0
#     print('negative changed to zero')
# elif x==0:
#     print('zero')
# else:
#     print('more')


# for
# words = ['cat','dog']
# for w in words:
#     print(w,len(w))
#
# user = [{
#     'a':'0',
#     'b':'1'
# },{
#     'a':'1',
#     'b':'2'
# }]
#
# user_obj = {
#     'a':'0',
#     'b':'1'
# }
# print(user_obj.copy().items())
#
# for i in range(3):
#     print(i)
# a = ['1','2','3','4']
# for i in range(len(a)):
#     print(i,a[i])
#
#
# sum(range(2))
# list(range(4))


# def
# def fib(n):
#     a,b = 0,1
#     while a < n:
#         print(a,end=' ')
#         a,b = b ,a+b
#     print()
#
# fib(20)


#loac
# def pos_only(arg,/):
#     print(arg)
#
# def arg_only(*,arg):
#     print(arg)
#
# print(pos_only(1))
# # print(pos_only(arg=1))
# # print(arg_only(2))
# print(arg_only(arg=2))
# print(list(range(3,6)))
# args = [3,6]
# print(list(range(*args)))
#
# def make_incrementor(n):
#     return lambda x:x+n
#
# f= make_incrementor(42)
# result = f(0)
# print(f(1)+result)
#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair:pair[0])
# print(pairs)


# def f(han:str,eggs:str='eggs')->str:
#     print('annotationss:',f.__annotations__)
#     print('arguments:',han,eggs)
#     return han+'and'+eggs
#
# print(f('span'))

# chars = ['a','b','c']
# chars.append('d')
# other_chars = ['m','n']
# chars.extend(other_chars)
# chars.insert(len(chars),'e')
# chars.remove('e')
# chars.pop()
#
# chars.clear()
# chars.count('a')
# chars.sort()
# chars.reverse()
# copy = chars.copy()
# print(chars)
# print(copy)

# a =[]
# for x in range(10):
#     a.append(x**2)
#
# print(a)
#
# b=list(map(lambda x:x**2,range(10)))
# print(b)
#
# c = [x**2 for x in range(10)]
# print(c)
#
#
# d = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(d)
#
# matrix = [
#     [1,3,4.5],
#     [3,5,6,8],
#     [1,0,6,3]
# ]
#
# e = [[row[i] for row in matrix]for i in range(4)]
#
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
#
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)




# a = [1,2,3,4]
# del a[0]
# print(a)
#
# del a[2:]
# print(a)
#
# del a[:1]
# print(a)
# del a
# print(a)

#
#
# t = 1,2,3,4
# # print(t[0])
#
# type(t)


# a = set('abc')
# b = set('def')
# c= a | b
# print(c)
# d = a & b
# print(d)
# e = a - b
# print(e)


# tel = {
#     'a':'a',
#     'b':'b'
# }
# print(tel['a'])
# tel['c'] = 'c'
# print(tel)
# print('a' in tel)
#
# print(list(tel))
#
# print(dict([('a', 1)]))
#
# print({x: x ** 2 for x in (2, 3, 4)})
#
# for k,v in enumerate(['a','b']):
#     print(k,v)
#
#
# question = ['name','age']
# answers = ['tjp','24']
# for q,a in zip(question,answers):
#     print('what is you {0}?it is {1}'.format(q,a))
#
#
# a,b,c = True,False,True
# not_null = a or b or c
# and_not_null = a and b and c
# print(not_null)
# print(and_not_null)

# import fibo,builtins
# fib = fibo.fib
# print(fib(10))
# print(dir(fibo))
# print(dir())

__all__ = ['fibo']
