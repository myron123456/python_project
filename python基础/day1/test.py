"""# example1：密码登录
print("欢迎您，admin用户")
password = input("请输入您的密码\n")
if password == "123456":
    print('密码成功，欢迎您')
else:
    print('密码失败，请重新尝试')"""

"""#example2:eval转化方法测试
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(eval(str1))
print(eval(str2))
print(eval(str3))
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))"""


"""# example3 上网管理系统
# 简单版
# age = 19
# if age > 18:
#     print('您符合上网条件')
# else:
#     print('对不起，您被禁止入内')

# 进阶版（支持手动输入年龄,并在系统输入用户当前年龄）
age = input('请输入您的年龄\n')
if int(age) > 18:
    print(f'您的年龄是{age},符合上网条件')
else:
    print(f'对不起，您的年龄是{age},禁止入内')"""


"""# example4工龄判断系统
age = input('请输入您的年龄')
if int(age)<18:
    print(f"您的年龄是{age},属于童工,回去学习")
elif 18<=int(age)<=60:
    print('您的年龄是{},符合用工要求'.format(age))
else:
    print('您的年龄是%s,请安心养老'%age)"""

"""# example5 公交车乘车系统
try:
    money = int(input("请输入您的零钱\n"))
    if money <= 0:
        print('余额不足，请先充值后乘车')
    else:
        seat = int(input("请输入公交车剩余座位\n"))
        if seat<=0:
            print('车内没有空位')
        else:
            print('车内有空位')
except Exception as e:
    print(e)"""

"""# example6 剪刀石头布游戏
# 1代表剪刀、2代表石头、3代表布
import random
computer = random.randint(1,3)
player = int(input('请输入您要出的对应数字'))
if player in range(1,4):
    print(computer)
    if (computer == 2 and player == 1) or (computer == 3 and player == 2) or (computer == 1 and player == 3):
        print('computer win')
    elif computer == player:
        print('平局')
    else:
        print('player win')
else:
    print('输入无效')"""


"""# example7 计算1-100累加和
num =0
i=1
while i<=100:
    num +=i
    i+=1
print(num)
"""
"""# example8 计算1-100偶数和
# 法1：取余数判断
num = 0
i = 0
while i<=100:
    if i%2 == 0:
        num +=i
    i+=1
print(num)
# 法2：计数器控制
num = 0
i = 0
while i<=100:
    num +=i
    i+=2
print(num)"""


"""#example9 打印星号：⼀⾏输出5个星号，重复打印5⾏
i = 1
j = 1
while i<=5:
    j = 1
    while j<=5:
        print('*',end="")
        j+=1
    print('')
    i+=1
"""

"""#example10 打印星号（三角形）：：⼀⾏输出星星的个数和⾏号是相等的，每⾏：重复打印⾏号数字个星号，将打印⾏星号的命令重
# 复执⾏5次实现打印5⾏。
i = 1
j = 1
while i<=5:
    j = 1
    while j<=i:
        print('*',end="")
        j+=1
    i += 1
    print('')"""
"""# example11 打印99乘法表
i = 1
j = 1
while i<=9:
    j = 1
    while j<=i:
        print(f"{j}*{i}=="+str(i*j),end=',')
        j+=1
    i += 1
    print('')"""