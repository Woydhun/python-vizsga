from module import *


rcic:str =choice(cicanevek)

eszam:int = 0
for c in rcic.lower: 
    if c == 'e':
        eszam +=1 

print(f'sorsolt cica név: {rcic} (e betu mennyisege: {eszam})')

while input('tetszikez a név?: ') != "igen":
    rcic = choice(cicanevek)
    print(f'új név: {rcic}')

print('grat')