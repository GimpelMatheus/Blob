# -- coding: utf-8 --
N = int(input())

while(True):

    days = 0

    if(N == 0):
        break

    else:
        C = float(input())
        while(C > 1.0):
            C = C/2
            days += 1

        print(f'{days} dias')

    N -= 1
