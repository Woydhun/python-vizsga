a:int = int(input('"a" értéke= '))
b:int = int(input('"b" értéke= '))

dif:int = abs(a-b)

print(f'a két szám különbségének abszolut értéke: {dif}')

if dif % 3 == 0: print(f'a(z) {dif} oszható 3al')
else: print(f'a(z) {dif} NEM osztható 3al')