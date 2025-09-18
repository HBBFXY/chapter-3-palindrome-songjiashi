# 从键盘获取输入
num = input("请输入一个5位数字：")

# 检查输入是否为5位且全为数字
if len(num) != 5 or not num.isdigit():
    print("输入错误，请输入一个5位数字")
else:
    # 判断是否为回文数
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
