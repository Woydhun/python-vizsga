from module import *


paralimpia:list[Verseny]= []
file = open('paralimpia.txt', 'r', encoding='utf-8')
for s in file: paralimpia.append(Verseny(s))

print(f'eggid merendezesre kerult versenyek stama: {len(paralimpia)}')

print(f'az elso paralimpiat, {paralimpia[0].orszag} rendezte')

oe: int = 0
for v in paralimpia:
    oe += v.osszeserem
print(f' magyar ermek szama: {oe} db')

va:int = 0
for v in paralimpia:
    if v.arany > 0:
        va += 1

print(f'osszesen {va} versenyen hoztak el aranyat')

mi:int = 0
for i in range(1, len(paralimpia)):
    if paralimpia[i].osszeserem > paralimpia[mi].osszeserem:
        mi = i
print(f'a legtöbb ermet {paralimpia[mi].varos}-ban/ben szereztek')

ke:int = int(input('írj be egy évet: '))

for v in paralimpia:
    if v.ev == ke:
        print(f'a {v.ev} ban ben paralimpia { v.orszag} ban ben volt')
    break
else:
    print(f'{ke}ben nem volt paralimpia')