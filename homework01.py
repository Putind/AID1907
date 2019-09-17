# # 1.在控制台获取输入的月份 显示对应的季度 或提示月份错误
# month = int(input('请输入月份：'))
# if 1 <= month <= 3:
#     print('春天来了')
# elif 4 <= month <=6:
#     print('夏天到了')
# elif 7 <= month <=9:
#     print('秋天凉快了')
# elif 10 <= month <= 12:
#     print('冬天好睡觉')
# else:
#     print('没得这个月')
# #
# # ２.在控制台获取年龄
# # 如果小于0 打印输入错误
# # 如果 小于2  打印是婴儿
# # 如果 小于2~13  儿童
# #        13~20  青年
# #        20~65  成年人
# #        65~130 老年人
# #        超过130 不可能
#
# age = int(input('请输入一个年龄：'))
# if age < 0:
#     print('你很优秀')
# elif age < 2:
#     print('婴儿')
# elif 2 <= age < 13:
#     print('儿童')
# elif 13 <= age <20:
#     print('青年')
# elif 20 <= age <65:
#     print('成年人')
# elif 65<= age <=130:
#     print('老年人')
# else:
#     print('向天再借５００年')
#
# # 3.根据身高和体重 参照BMI 返回身体状况
# # BMI 体重(kg)/身高(m)**2
# # 中国参考标准
# # BMI<18.5   体重过低
# # 18.5<=BMI<24   正常
# # 24<=BMI<28     超重
# # 28<=BMI<30     I度肥胖

# kg = float(input('请输入你体重(kg)'))
# m = float(input('请输入你的身高(m)'))
# BMI = kg/m**2
# if BMI<18.5:
#     print('你有点虚')
# elif 18.5 <= BMI < 24:
#     print('你狠棒')
# elif 24 <= BMI < 28:
#     print('你狠状')
# elif 28 <= BMI < 30:
#     print('有点胖')
# else:
#     print('额　祝你好运')

# 4.题目：企业发放的奖金根据利润提成
# a = 10*(10/100)
# b = a + 10*(7.5/100)
# c = b + 20*(5/100)
# d = c + 20*(3/100)
# e = d + 40*(1.5/100)
#
# I = float(input('请输入当月利润'))
#
# if I<=10:
#     i=I*(10/100)
#
# elif 10<I<20:
#     i = a +(I-10)*(7.5/100)
# elif 20<=I <40:
#     i = b +(I-20)*(5/100)
# elif 40<= I <60:
#     i = c + (I-20)*(3/100)
# elif 60<= I <100:
#     i = d + (I-40)*(1.5/100)
# else:
#     i = e + (I-100)*(1/100)
# print(i)


# 5.输入某年某月某日，判断这一天是这一年的第几天？
# 1 3 5 7 8 10 12 31天
#  4 6 9 11 30天　２　２８天/29天　
# 1年　365天 366天

# year = int(input('请输入某年'))
# month = int(input('请输入某月'))
# day = int(input('请输入某日'))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     a = 29
# else:
#     a = 28
# c = 1
# d = 0
# while c < month:
#     if c == 1 or c == 3 or c == 5 or c == 7\
#             or c == 8 or c == 10 or c == 12:
#         d = d + 31
#
#     elif c == 4 or c == 6 or c == 9 or c == 11:
#         d += 30
#     elif c == 2:
#         d += a
#     else:
#         print('请输入正确的月份')
#      更新循环变量
#     c += 1
# d += day
# print(d)

# 6.打印出1000以内所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
#153
#1**3 + 5**3 + 3**3
#153
#370
#371
#407

# s = 100
# while s < 1000:
#     ge = s % 10
#     shi = s//10 % 10
#     bai = s//100
#     if ge**3+shi**3+bai**3 == s:
#         print(s)
#     s += 1
#
# for i in range(100,1000):
#     ge = i %10
#     shi = i//10%10
#     bai =i //100
#     if ge ** 3+shi**3+bai**3==i:
#         print(str(i)+'是水仙花数')

# for bai in range(1,10):
#     for shi in range(0,10):
#         for ge in range(0,10):
#             i = ge +shi*10+bai*100
#             if(ge**3+shi**3+bai**3)==i:
#                 print(str(i)+'是水仙花数')

# 1   2   3
# 百　十位　个位
# 123 ---'123'
# for i in range(100,1000):
#     #记录每一位数字的立方累加　默认值为０
#     sum_number = 0
#     # 将数字转换为字符串在转为数字　
#     for ch in str(i):
#         # 将字符串转换为数字　将立方值累加到sum_number
#         sum_number += int(ch)**3
#         #
#     if sum_number == i:
#         print(str(i)+'是水仙花数')
