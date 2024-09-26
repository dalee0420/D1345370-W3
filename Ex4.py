a=str(input('請輸入一個三位數:'))
if int(a)>=100 and int(a)<=999:
    b=list(a)
    print('每位數字的總和:',int(b[0])+int(b[1])+int(b[2]),sep='')
else:
    print('位數錯誤')