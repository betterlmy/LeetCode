# author:TYUT-Lmy
# date:2021/12/21
# description:
# test1 把参数读取到一维列表里，分隔符号为逗号或者下划线
# test2 把参数一行一行的读取到一个一维列表里
# test3 把任意行的参数读取到一个二维列表里，以空字符结束输入
# test4 读取输入的n参数，把参数读取到n行的二维列表里
# test5 把参数读取到一维列表里，分隔符号为空格
import sys


## 读取参数输入到一个一维列表里，输入参数以逗号“,”或者下划线“_”隔开，中间可能有任意空格，以换行结束输入
## 示例输入：    1,    2_     3,    5_7     ,8
# 输出[1,2,3,5,7,8]
# 值得注意的是：
# Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。

def input_test1():
    ## input 进来是str的格式
    input_data = input()

    # 对字符串进行初步的处理
    ## 去除里面的空格，需要注意replace不会改变原来输入的内容,
    ## String.replace(old, new, count) 加上数量的话只替换前count个
    no_blank_data = input_data.replace(" ", "")
    no_blank_data = no_blank_data.replace("_", ",")  ##多个字符分割提前替换掉

    # 以逗号为分割符号把字符里的数字存在列表里
    # input_list_test = no_blank_data.split(",")
    input_list_test = no_blank_data.split(",")

    # 将list里的字符串转换为数字
    input_list_test = list(map(int, input_list_test))

    # print(input_list_test)
    # print(type(input_list_test))
    # print(type(input_list_test[0]))
    return input_list_test


# 一行一行的进行输入，每结束一行输入就把输入放到列表里去，指定结束符号为"\n"就是一行空的输入
# 示例输入：
# 12334
# 23456
# 12
# 30
#
# 示例输出： [12334, 23456, 12, 30]
def input_test2():
    lines = []
    try:
        while True:
            # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
            line = sys.stdin.readline().strip()
            ## 指定跳出循环的输出符号，这个地方是一行不输入，直接按回车就会跳出循环
            if line == '':
                break
            else:
                lines.append(line)
    except:
        pass
    # str转换成int格式
    lines = list(map(int, lines))
    return lines


#  不指定行数输入多行数据，以空行或者换行符结束，返回一个二维list
def input_test_3():
    try:
        two_dimemsional_list = []
        while True:
            # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
            row = sys.stdin.readline().strip()
            if row == '':
                break
            row_list = list(map(int, row.split()))  ## 输入时，利用map直接映射成int类型
            two_dimemsional_list.append(row_list)  ## 这边变成extend就可以存储成一个一维数组

    # two_dimemsional_list = list(map(int,two_dimemsional_list))

    except:
        pass

    return two_dimemsional_list


# 第一行输入指定n行m列，然后输入n*m的数据,数据之间用空格隔开，存储到n*m的一个二维列表里
def input_test_4():
    n_and_m = input()
    # 方法1，以空格为分隔符号，自动过滤掉空行
    # n_and_m_list = filter(None,n_and_m.split(" "))

    # 方法2,split()函数默认可以按空格分割，并且把结果中的空字符串删除掉
    n_and_m_list = n_and_m.split()
    n = int(n_and_m_list[0])
    m = int(n_and_m_list[1])

    two_dimemsional_list = []
    for i in range(n):
        row = input().strip()
        row_list = list(map(int, row.split()))  ## 如果就是需要字符串类型，就不用转换成int
        two_dimemsional_list.append(row_list)
        i = i + 1

    return two_dimemsional_list


def test5():
    input_data = input()

    # 对字符串进行初步的处理
    ## String.replace(old, new, count) 加上数量的话只替换前count个
    # 以逗号为分割符号把字符里的数字存在列表里
    # input_list_test = no_blank_data.split(",")
    input_list_test = input_data.split(" ")

    # 将list里的字符串转换为数字
    input_list_test = list(map(int, input_list_test))

    # print(input_list_test)
    # print(type(input_list_test))
    # print(type(input_list_test[0]))
    return input_list_test


def test5():
    input_data = input()

    input_list_test = input_data.split(" ")
    input_list_test = list(map(int, input_list_test))

    return input_list_test


def main():
    n = int(input())
    list1 = test5()[:n]
    list1.sort()
    result = ''
    num = 0
    for i in list1:

        result += (str(i))
        if num != n - 1:
            result += ' '
        num += 1
    return result


if __name__ == '__main__':
    print(main())
