a=str(input('輸入三位數字:'))
if int(a)>=100 and int(a)<=999:
    b=list(a)
    print('結果:',b[2]+b[1]+b[0],sep='')
else:
    print('位數錯誤')