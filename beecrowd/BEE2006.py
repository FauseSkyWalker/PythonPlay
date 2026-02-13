Cha = int(input())

Palpites = list(map(int,input().split ()))

Certo = 0

for P in Palpites:

    if P == Cha:
        Certo = Certo + 1

print(Certo)