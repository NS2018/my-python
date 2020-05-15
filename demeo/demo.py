import math
import json
import sys
import os
import glob
from urllib.request import urlopen
# year  = '2020'
# event = 'study python'
# print(f'{year},i am {event}')
#
# print('{0},i am {1}'.format(year, event))
#
# s = 'hello world'
# print(str(s))
# print(repr(s))
#
# i = 1
# print(str(i))
# print(repr(i))

# print(f'pi is {math.pi:.4f}')
#
# table = {
#     'a':'123',
#     'df':'123243'
# }
# for i,j in table.items():
#     print(f'{i:10} ==> {j:10}')


#
# val = 'fafa'
# print(f'aaa{val!r}')
# print(f'aaa{val!s}')
# print(f'aaa{val!a}')




# table = {
#     'a':1,
#     "b":2
# }
#
# print('a:{a:d};b:{b:d}'.format(**table))
#
# for x in range(1,11):
#     print('{0:2d}  {1:3d}  {2:4d}'.format(x, x ** 2, x ** 3))




# with open('foo.txt','r') as f:
#     print(json.dumps(f))
#     # read_data = f.read()
#     # print(f.readline())
#     # print(repr(f.readline()))
#     # f.write('\nappend content\n')
#     # for line in f:
#     #     print(line,end = "")
#     # val = ('a',23)
#     # s = str(val)
#     # f.write(s)
#     f.write(b'975934754979')
#     f.seek(5)
#     print(f.read(1))
#     f.seek(-3,2)
#     print(f.read(1))
#
# print(f.closed)

# print(repr(json.dumps([1, 'z', 'list'])))





# exception
# while True:
#     try:
#         x = int(input('please enter a number:\n'))
#         break
#     except ValueError:
#         print('oops! that was no valid number,try again ...')
#
#
# try:
#     with open('foo.txt') as f:
#         s = f.readline()
#         i = int(s.strip())
# except OSError as err:
#     print('os error:{0}'.format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
# else:
#     print('over')


# try:
#     raise Exception('spam','eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     x,y = inst.args
#
#     print('x = ', x)
#     print('y = ', y)

# try:
#     raise NameError('HiThere')
#     print('111')
# except NameError:
#     print('an exception flew by!')
#     raise ValueError
#     print('bbb')
# except ValueError:
#     print('ccc')

# class Error(Exception):
#     pass
#
# class InputError(Error):
#     def __init__(self,expression,message):
#         self.expression = expression
#         self.message = message
#
# class TransitionError(Error):
#     def __init__(self,previous,next,message):
#         self.previous = previous
#         self.next = next
#         self.message = message
#
#
# def divide(x,y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print('division by zero')
#     else:
#         print('result is :',result)
#     finally:
#         print('executing finally clause')
#
#
# divide(2,1)
# divide(2,0)




# global 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；
# nonlocal 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定。
#LEGB 局部 外部 全局 内置
# def scope_test():
#     def do_local():
#         spam = 'local spam'
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = 'noolocal spam'
#
#     def do_global():
#         global spam
#         spam = 'global spam'
#
#     spam = 'test spam'
#     do_local()
#     print('after local assignment:', spam)
#     do_nonlocal()
#     print('after do_nonlocal assignment:', spam)
#     do_global()
#     print('after do_global assignment:', spam)
#
# scope_test()
# print('in global scope:', spam)
#
#
# class Complex:
#     def __init__(self,realpart,imagpart):
#         self._r = realpart
#         self._i = imagpart
#
# x = Complex(3.0,-4.5)

#
# result = glob.glob('*.py')
# for i in result:
#     print(i)
#
# print(sys.argv)
# sys.stderr.write('warning ,log file not found starting a new one \n')

#
# with urlopen('https://multimedia.api.weibo.com/2/multimedia/user/play_history/report.json?source=2637646381&play_type=1&video_orientation=horizontal&video_duration=244.945&id=4494245987822189&id_type=0&seconds=30&oid=1034:4493987273179159&is_contribution=1&reqHost=https://weibo.com/like/outbox?leftnav=1') as response:
#     for line in response:
#             print(line)