import math
import time
import pyperclip
def deg(x):
    temp = (180/math.pi)
    return (x*temp)
def rad(x):
    temp = (math.pi/180)
    return (x*temp)
def cos(x):
    return (math.cos(rad(x)))
def sin(x):
    return (math.sin(rad(x)))
def tan(x):
    return (math.tan(rad(x)))
def acos(x):
    return (deg(math.acos(x)))
def asin(x):
    return (deg(math.asin(x)))
def atan(x):
    return (deg(math.atan(x)))
def sqrt(x):
    return (math.sqrt(x))
pi = math.pi
L = 6.02e23
l = 6.02e23
rd = 3
auto_copy = False
number_whitelist = ['0','1','2','3','4','5','6','7','8','9','(',')','^','√','.']
number_whitelist_trifunc = ['0','1','2','3','4','5','6','7','8','9','^','√','.']
symbol = ['^','*','/','+','-','√','(']
symbol_include_paren = ['^','*','/','+','-','(',')']
symbol_whitelist = ['0','1','2','3','4','5','6','7','8','9','(',')','^','√','*','/','+','-','.']
letter = ['a','b','c']
triangle_function_startwith = ['s','c','t','a']
triangle_functions = ['sin','cos','tan']
triangle_functions_arc = ['asin','acos','atan']
plus_minus = ['+','-']
autoreplace = True
listenclipboard = False
a = 0
last_value = 'start to listen clipboard'
while True:
    if listenclipboard == True:
        while True:#监听剪贴板
                    tmp_value = pyperclip.paste()
                    #print ('content =', tmp_value)
                    if not tmp_value == last_value:
                        if tmp_value != str(round(a, rd)):
                            #print ('go to calculate')
                            last_value = tmp_value
                            inp = tmp_value
                            break
                    #print ('no thing wrong')
                    time.sleep(0.2)
    else:
        inp = input ('>>>')
    if not inp == '':
        if inp.startswith('/'):
            inp = inp.strip('/')
            if inp.startswith('fmla'):#二次方程
                if inp.endswith('1'):
                    fmla1 = input('input: a b c\n')
                    fmla1 = fmla1.split(' ')
                    a = int(fmla1[0])
                    b = int(fmla1[1])
                    c = int(fmla1[2])
                    print (((0-b)+math.sqrt((b**2)-(4*a*c)))/(2*a))
                    print (((0-b)-math.sqrt((b**2)-(4*a*c)))/(2*a))
            elif inp.startswith('rd'):#保留x位小数
                if inp.endswith('off'):
                    rd = 0
                else:
                    rd = int(inp.split(' ')[1])
            elif inp.startswith('autocopy') or inp.startswith('ac'):#是否开启自动复制
                if inp.endswith('off'):
                    auto_copy = False
                    print ('auto copy disabled')
                else:
                    auto_copy = True
                    print ('auto copy enabled')
            elif inp.startswith('autoreplace') or inp.startswith('ar'):#关闭自动格式转换
                autoreplace = not autoreplace
            elif inp.startswith('listenclipboard') or inp.startswith('lc'):#监听剪贴板
                listenclipboard = not listenclipboard
                pyperclip.copy('listening clipboard')
                last_value = pyperclip.paste()
                auto_copy = True
                print('start to listen clipboard')
            elif inp.startswith('status'):
                print ('unfinished function')
            elif inp.startswith('x'):
                break
            else:
                exec (inp)#执行指令
        else:
            if autoreplace == True:
                inp = inp.strip('=')
                inp_ls = list(inp)
                len_inp = len(inp_ls) 
                if len_inp > 1:#格式转换
                    for times in range(len(inp_ls)):
                        try:
                            if inp_ls[times] == ' ' or inp_ls[times] == '⁡':
                                del inp_ls[times]
                                len_inp = len(inp_ls)
                        except IndexError:
                            break
                    for times in range(len(inp_ls)):
                        if str(inp_ls[times]) == '〖':
                            inp_ls[times] = '('
                        elif str(inp_ls[times]) == '〗':
                            inp_ls[times] = ')'
                    times = 0
                    try:
                        while True:#添加乘号
                            #print (times)
                            if inp_ls[times] in symbol_whitelist and inp_ls[times+1] in symbol_whitelist:#如果连续两个字符都是数字或符号
                                #print ('b')
                                pass
                            else:#否则（如果有任意一个不是数字或符号）
                                #print ('a')
                                if not (inp_ls[times] in symbol_include_paren or inp_ls[times+1] in symbol_include_paren):#如果两个字符没有一个是符号
                                    #print ('c')
                                    if times < len(inp_ls)-1:#如果不是最后一位
                                        #print ('d')
                                        if inp_ls[times] in triangle_function_startwith:#如果第一个字符是三角函数首字母
                                            #print ('e')
                                            if inp_ls[times]+inp_ls[times+1]+inp_ls[times+2] in triangle_functions:#如果其与其后两个字符可以组成三角函数
                                                #1print ('a1')
                                                times = times + 2#跳过后两个字符判断
                                                if inp_ls[times+1] != '(':#是否已存在括号
                                                    inp_ls.insert(times+1,'(')#补充开括号
                                                    x=0
                                                    while True:
                                                        if not inp_ls[times+2+x] in number_whitelist_trifunc:#如果三角函数后出现需要截断的运算符
                                                            if x != 0:
                                                                inp_ls.insert(times+2+x,')')#补充关括号
                                                                break
                                                        elif times+2+x >= len(inp_ls)-1:#如果是最后一位
                                                            inp_ls.insert(times+3+x,')')#补充关括号
                                                            break
                                                        x = x+1 
                                            elif inp_ls[times]+inp_ls[times+1]+inp_ls[times+2]+inp_ls[times+3] in triangle_functions_arc:#如果其与其后两个字符可以组成反三角函数
                                                #print ('a2')
                                                times = times + 3#跳过后三个字符判断
                                                if inp_ls[times+1] != '(':#是否已存在括号
                                                    inp_ls.insert(times+1,'(')#补充开括号
                                                    x=0
                                                    while True:
                                                        if not inp_ls[times+2+x] in number_whitelist_trifunc:#如果三角函数后出现需要截断的运算符
                                                            if x != 0:
                                                                inp_ls.insert(times+2+x,')')#补充关括号
                                                                break
                                                        elif times+2+x >= len(inp_ls)-1:#如果是最后一位
                                                            inp_ls.insert(times+3+x,')')#补充关括号
                                                            break
                                                        x = x+1 
                                            else:#添加乘号
                                                #print ('e2')
                                                #print('2added times for variable')
                                                inp_ls.insert(times+1,'*')
                                            #print (3)
                                        else:#添加乘号
                                            #print ('f')
                                            #print('1added times for variable')
                                            inp_ls.insert(times+1,'*')
                            if inp_ls[times] == '(':#为括号之间添加乘号
                                #print ('g')
                                if not inp_ls[times-1] in symbol:
                                    if not times == 0:
                                        if not inp_ls[times-3]+inp_ls[times-2]+inp_ls[times-1] in triangle_functions:
                                            #print ('h')
                                            #print('added times for parentheses')
                                            inp_ls.insert(times,'*')
                                            #print (''.join(inp_ls))
                            times = times+1
                    except IndexError:
                        pass
                inp = ''.join(inp_ls)
            print(inp)
            inp = inp.replace('^','**').replace('√','sqrt')#替换平方和平方根
            try:
                exec ('a = %s' %(inp))#计算结果
                if auto_copy == True:#判断是否复制
                    pyperclip.copy(str(round(a, rd)))
                if rd == 0:#判断是否省略
                    print(a)
                else:
                    print(round(a, rd))
            except SyntaxError:
                print ('Syntax Error')
                print ('input =',inp)
            except NameError:
                print ('Name Error')
                print ('input =',inp)