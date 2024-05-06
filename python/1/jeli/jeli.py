from random import choice

nev:str = input('ird be a neved: ')
ev:str = input('ird be a szuletesi eved: ')
specs:list[chr] = ['#','&','@','!','%']

p1:str = nev[:4]
p2:str = ev[2:]
p3:str = f"{choice(specs)}{choice(specs)}"

jelszo:str = f'{p1.capitalize()}{p2}{p3}'
print(jelszo)
