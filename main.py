# 获取用户输入
user_input = input("请输入一个5位数字: ")

# 检查输入是否为5位纯数字
if not user_input.isdigit():
    print("错误：输入必须为纯数字")
elif len(user_input) != 5:
    print("错误：输入必须为5位数字")
else:
    # 判断是否为回文数
    if user_input == user_input[::-1]:
        print("是回文数")
    else:
        print("不是回文数")# 这里编写你的代码
