# num = 1
# # 短路逻辑逻辑运算时　　如果前面的条件能判断出最终结果
# # 后面的代码就不会执行
# # 尽量降复杂的判断放在后面
# # and 发现第一个结果为False 就有结论了
# # 后续条件不在判断
# result = num > 1 and input('请输入ａ') == 'a'
#
# # or发现第一个结果为Ture
# # 后续条件不在判断
# result1 = num == 1 or input('请输入a') == a
# a = 800
# b = 1000
# #  id函数　获取变量存储对象的地址
# print(id(a))
# print(id(b))
# print(a is b)#is运算本质是通过id 函数进行判断的
# c = a
# print(id(c))
# print(c is a)
#
# d = 1000
# print(b is d)
# 三个物理行　三个逻辑行
# a = 1
# b = a+1
# c = a+2
#  一个物理行，　三个逻辑航
# 　在一个逻辑行中使用多个逻辑行　使用;分隔
# a = 1; b = a+1; c = a+2; #不建议这样写
# 隐式换行　在括号内换行()[]{}

# \折行符　必须放在末尾作用是告诉解释器下一行也是本行的语句


# price = float(input('输入商品单价'))
# count = int(input('请输入商品数量'))
# money = float(input('请输入金额'))
# res = money - price * count
#
# if res>=0:
#     # 金额不足　找零执行代码
#     result = '应找回: ' +str(res)
# else:
#     # 不大于０要执行的
#     result = '金额不足 回家去拿钱再来'
#     # 输出结果
# print(result)
# 选择语句在执行过程中只会选择一个符合的代码
# a = 10
# b = 10
# if a>b:# 如果不满足向下执行
#    #  满足条件a>b 执行代码
#    print('最大数是a')
# elif a == b:#如果不满足向下执行
#     #  满足条件a == b 执行代码
#     print('a和b相等')
# elif a<b:#如果不满足向下执行
#     #  满足条件a<b 执行代码
#    print('最大的数是b')

#else
# pass#占位　

# 调试
# 让程序中断　卓行执行
# 目的　审查程序运行是的变量以及变量取值
# 　审查程序运行的流程
# 步骤
# 1.加断点(调试过程中遇到断点加断点)
# 2.　运行调试shift+f9
# 3.程序会在断点出停止　按f8
# 4.ctrl+f2停止调试

#season = input('请输入一个季度')

# if season == '春':
#     print('1月2月3月')
# if season == '夏':
#     print('４月５月６月')
# if season == '秋':
#     print('７月８月９月')
# if season == '冬':
#     print('１０月１１月１２月')

#
# if season == '春':
#     print('1月2月3月')
# elif season == '夏':
#     print('４月５月６月')
# elif season == '秋':
#     print('７月８月９月')
# elif season == '冬':
#     print('１０月１１月１２月')


op = input('是否有卖西瓜的')

if op == '有':
    count = 1
    print('老王买了' + str(count) + '西瓜')
else:
    count = 4

print('老王买了'+str(count)+'包子')
#
# suzi = input('请输入一个数字')
# op = input('请输入一个运算符')
# suzi1 = input('请在输入一个数字')
# if op == '+':
#    print(suzi+suzi1)
# elif op == '-':
#     print(suzi-suzi1)
# elif op == '*':
#     print(suzi*suzi1)
# elif op == '/':
#     print(suzi+suzi1)
# else:
#     print('运算符有误')

# num = input('请输入第一个数字：')
# num1 = input('请输入第二个数字：')
# if num > num1:
#     print(num1)
# elif num == num1:
#     print(num)
# else:
#     print(nun1)

# num = input('请输入第一个数字：')
# num1 = input('请输入第二个数字：')
# num2 = input('请输入第三个数字：')
# if num > num1:
#     print(num)
#     if num > num2:
#         print(num)
#     else:
#         print(num2)
# else:
#     if num1 > num:
#         print(num1)
#         if num1 > num2:
#             print(num1)
#         else:
#             print(num2)
#
# num1 = input('请输入第一个数字：')
# num2 = input('请输入第二个数字：')
# num3 = input('请输入第三个数字：')
# num4 = input('请输入第四个数字：')
# # 假设第一个数是最大值
# # 将最大值与第二个数比较　如果第二个数比最大值大
# max_value = num1
# if num2 > num1:
#     max_value = num2
# if num3 > num2:
#     max_value = num3
# if num4 > num3:
#     max_value = num4
# print(max_value)

# 下面程序需要修改
# month = str(input('输入一个月份：'))
# if month == "1,3,5,7,8,10,12":
#     print("31天")
# elif month == '6,9,11':
#     print('30天')
# elif month == 2:
#     print('28天')
# else:
#     print('输入错误')

# if 100:
#
#     print('真值为True')

# if '':
#     print('yes')
# else:
#     print('no')

# num = input('输入一个整数')
# if num % 2 == 0:
#     state = '偶数'
# else:
#    state = '奇数'
#
# if num % 2:
#     state = '奇数'
# else:
#     state = '偶数'
#
# state = '奇数'if num % 2 else '偶数'
# print(state)

# year = int(input('输入一个年份：'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     day = 28
# else:
#     day = 29
# print(day)
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: else 28


while True:
    dol = int(input('请输入美元'))
    print(dol*6.9)
    if input('输入exit退出') == 'exit':
        break

