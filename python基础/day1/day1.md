一、python解释器：
当我们编写Python代码时，我们得到的是一个包含Python代码的以.py为扩展名的文本文件。要运行代码，就需要Python解释器去执行.py文件。

由于整个Python语言从规范到解释器都是开源的，所以理论上，只要水平够高，任何人都可以编写Python解释器来执行Python代码（当然难度很大）。事实上，确实存在多种Python解释器。

CPython
当我们从Python官方网站下载并安装好Python 3.x后，我们就直接获得了一个官方版本的解释器：CPython。这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。

CPython是使用最广的Python解释器。教程的所有代码也都在CPython下执行。

IPython
IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的。好比很多国产浏览器虽然外观不同，但内核其实都是调用了IE。

CPython用>>>作为提示符，而IPython用In [序号]:作为提示符。

PyPy
PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。

绝大部分Python代码都可以在PyPy下运行，但是PyPy和CPython有一些是不同的，这就导致相同的Python代码在两种解释器下执行可能会有不同的结果。如果你的代码要放到PyPy下执行，就需要了解PyPy和CPython的不同点。

Jython
Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。

IronPython
IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

小结
Python的解释器很多，但使用最广泛的还是CPython。如果要和Java或.Net平台交互，最好的办法不是用Jython或IronPython，而是通过网络调用来交互，确保各程序之间的独立性。

本教程的所有代码只确保在CPython 3.x版本下运行。请务必在本地安装CPython（也就是从Python官方网站下载的安装程序）。
【廖雪峰的官方网站 https://www.liaoxuefeng.com/wiki/1016959663602400/1016966024263840】

二、注释：

单行注释⾏： # 注释内容 ，快捷键ctrl+/

多行注释⾏： """ 注释内容 """ 或 ''' 注释内容 '''

三、变量
１、标识符：
变量名 = 值
标识符命名规则是Python中定义各种名字的时候的统一规范，具体如下：
由数字、字母、下划线组成
不能以数字开头
不能使用内置关键字
严格区分大小写
False None True and as assert break class 
continue def del elif else except finally for
from global if import in is lambda nonlocal
not or pass raise return try while with 
yield
２、命名习惯：
⻅见名知义。
⼤大驼峰：即每个单词首字母都大写，例如： MyName 。
⼩小驼峰：第二个（含）以后的单词⾸字⺟⼤写，例如： myName 。
  下划线：例如： my_name 。
四、格式化输出：
 １、格式化符号：
 %s：格式化输出字符串
　%d：格式化输出整数
　%f：格式化输出浮点数
２、f-字符串
    f'{表达式}'
    注意：表达式不可为空，否则会报错
    我的名字是TOM，明年19岁了
    print(f'我的名字是{name}, 明年{age + 1}岁了')
３：转义字符
\n：换行
\t：制表符
４、print结束符
print('内容', end="")
五、输入：
input("提示文字”)
1、input特点
当程序执⾏到 input ，等待⽤户输⼊，输⼊完成之后才继续向下执⾏。
在Python中， input 接收⽤户输⼊后，⼀般存储到变量，⽅便使⽤。
在Python中， input 会把接收到的任意⽤户输⼊的数据都当做字符串处理。
2、input输入密码小例子
# example1：密码登录
print("欢迎您，admin用户")
password = input("请输入您的密码\n")
if password == "123456":
    print('密码成功，欢迎您')
else:
    print('密码失败，请重新尝试')

六、转化数据类型
int()：转化为整形
float()：转化为浮点型
str()：转化为字符串类型
list()：转化为列表
tuple()：转化为元组
eval()：将字符串中数据转化为python中原本类型

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


七、运算符
1、算数运算的优先级
    混合运算优先级顺序： () ⾼于 ** ⾼于 * / // % ⾼于 + -
2、赋值运算符
    =
    复合赋值运算符
    +=
    -=
    优先级
    1. 先算复合赋值运算符右侧的表达式
    2. 再算复合赋值运算的算数运算
    3. 最后算赋值运算
3、⽐较运算符
    判断相等： ==
    ⼤于等于： >=
    ⼩于等于：<=
    不等于： !=
4、逻辑运算符
    与： and
    或：or
    ⾮：not
    
八、条件语句：
1、if语句语法
    if 条件:
         条件成⽴执⾏的代码
    if...else...
        if 条件:
         条件成⽴执⾏的代码
        else:
         条件不成⽴执⾏的代码
2、多重判断
    if 条件1:
     条件1成⽴执⾏的代码
    elif 条件2:
     条件2成⽴执⾏的代码
    else:
     以上条件都不成⽴执⾏的代码
3、if嵌套：
    if 条件1:
     条件1成⽴执⾏的代码
    if 条件2:
     条件2成⽴执⾏的代码
3、三⽬运算符
    条件成⽴执⾏的表达式 if 条件 else 条件不成⽴执⾏的表达式
    a = 1 b = 2 c = a if a > b else b
"""# example3 上网管理系统
简单版
 age = 19
 if age > 18:
     print('您符合上网条件')
 else:
     print('对不起，您被禁止入内')
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
    
    
九、循环语句：
循环的作⽤：控制代码重复执⾏
1、while语法
while 条件:
 条件成⽴重复执⾏的代码1
 条件成⽴重复执⾏的代码2
2、while循环嵌套语法
while 条件1:
 条件1成⽴执⾏的代码
 ......
 while 条件2:
 条件2成⽴执⾏的代码
 3、for循环语法
 for 临时变量 in 序列:
 重复执⾏的代码1
 重复执⾏的代码2
4、退出循环
break退出整个循环
continue退出本次循环，继续执⾏下⼀次重复执⾏的代码
else
while和for都可以配合else使⽤
else下⽅缩进的代码含义：当循环正常结束后执⾏的代码
break终⽌循环不会执⾏else下⽅缩进的代码
continue退出循环的⽅式执⾏else下⽅缩进的代码
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

"""# 打印星号：⼀⾏输出5个星号，重复打印5⾏
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