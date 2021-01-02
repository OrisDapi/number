import random
num = random.randint(1, 100)
num = int(num)

count = 0

while True :
    count = count + 1 #count += 1
    num1 = input('1~100內請猜一數字')
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

if num1 < '1' and num1 > '100' :
    print('請輸入1～100數字')