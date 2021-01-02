import random

start = input('請輸入起點值: ')
end = input('請輸入終點值: ')
start = int(start)
end = int(end)

num = random.randint(start, end)
num = int(num)

count = 0

while True :
    count = count + 1 #count += 1
    num1 = input('請猜一數字')
    num1 = int(num1)
    if num1 == num :
        print('恭喜猜中！')
        print('這是你猜的第', count, '次')
        break

    elif num1 > num :
        print('smaller than you guess')
    elif num1 < num :
        print('bigger than you guess')

    print('這是你猜的第', count, '次')
