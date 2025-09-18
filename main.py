def main():
    num_str = input().strip()
    
    # 检查输入是否为5位且为纯数字
    if not num_str.isdigit():
        print("输入错误：必须为纯数字")
        return
        
    if len(num_str) != 5:
        print("输入错误：必须为5位数字")
        return
        
    # 判断是否为回文数
    if num_str == num_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

if __name__ == "__main__":
    main()
