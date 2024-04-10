A, B, C = map(float, input().split())

MAIORAB =  (A + B + abs(A-B))/2

if MAIORAB > C :
    print(int(MAIORAB) ,"eh o maior")

else :
    print(int(C) ,"eh o maior")