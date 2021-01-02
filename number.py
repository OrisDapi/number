import random
num = random.randint(1, 100)
num = int(num)
while True :
    num1 = input('1~100內請猜一數字')
    num1 = int(num1)
    if num1 == num :
        print('恭喜猜中！')
        break      
    elif num1 > num :
        print('smaller than you guess')
    elif num1 < num :
        print('bigger than you guess')

if num1 < '1' and num1 > '100' :
    print('請輸入1～100數字')