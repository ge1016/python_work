#coding:utf-8
sum = 0
while True: #使用while循环让犯错后能够继续输入
    try:
        num1 = int(input("请输出一个数字："))
        num2 = int(input("请在输入一个数字： "))
    except ValueError:
        print("输入的要是数字哦！")
        continue #强制跳出本次回圈进入下一圈
    else:
        sum = num1 + num2
        print("以上数字求和的结果为： " + str(sum))
        break
