a=str(input('請輸入一個五位數:'))
if int(a)>=10000 and int(a)<=99999:
    b=list(a)
    print('結果:')
    print(b[0])
    print(b[1])
    print(b[2])
    print(b[3])
    print(b[4])
else:
    print('位數錯誤')