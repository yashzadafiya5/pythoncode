#hollow half peramid
row=1
while row<=6:
    column=1
    while column<=row:
        if row==6 or row==1 or row==2:
            print('* ',end='')
        elif column>=2 and column<row:
            print(' ',end=' ')
        else:
            print('*',end=' ')
        column=column+1
    print("")
    row=row+1