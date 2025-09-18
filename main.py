def is_palindrome():
    """判断5位数字是否为回文数的函数"""
    
    # 获取用户输入
    user_input = input("请输入一个5位数字: ")
    
    # 去除可能的前后空格
    user_input = user_input.strip()
    
    # 检查输入是否为空
    if not user_input:
        print("错误：输入不能为空")
        return
    
    # 检查输入是否为纯数字
    if not user_input.isdigit():
        print("错误：输入必须为纯数字")
        return
    
    # 检查输入是否为5位数字
    if len(user_input) != 5:
        print("错误：输入必须为5位数字")
        return
    
    # 判断是否为回文数
    if user_input == user_input[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

# 主程序
if __name__ == "__main__":
    print("=== 5位回文数判断程序 ===")
    print("说明：请输入一个5位的自然数进行回文数判断")
    print("-" * 30)
    
    is_palindrome()
    
    print("-" * 30)
    print("程序执行完毕")
