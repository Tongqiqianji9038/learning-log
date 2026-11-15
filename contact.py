contacts = {}

while True:
    cmd = input("命令（add/list/find/quit）: ")

    if cmd == "add":
        name = input("姓名: ")
        phone = input("电话: ")
        if name in contacts:
            print(f"注意：{name} 已存在，电话将从 {contacts[name]} 更新为 {phone}")
        contacts[name] = phone
        print(f"已添加/更新联系人 {name}，电话为 {phone}")

    elif cmd == "list":
        #如果没有联系人，提示没有联系人
        if not contacts:
            print("没有联系人喵")
        else:
            print("联系人列表:")
            #使用for循环遍历字典，打印每个联系人姓名和电话
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif cmd == "find":
        #询问用户要查找的联系人姓名
        name = input("请输入要查找的联系人姓名: ")
        #如果联系人存在，打印电话，否则提示联系人不存在
        if name in contacts:
            print(f"{name} 的电话是 {contacts[name]}")
        else:
            print(f"联系人 {name} 不存在喵")
    elif cmd == "quit":
        print("退出程序喵")
        break
    else:
        print("无效的命令喵，请输入 add/list/find/quit")