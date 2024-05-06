print('''paradicsom:  1199 Ft/Kg 
paprika:     1349 Ft/Kg 
vöröshagyma:  289 Ft/Kg''')

osszar:int = 0
while input('szeretn-e vásárolni?: ') == 'igen':
        termek:str = input('mit szeretne vásárolni?: ')
        egysegar:int = 0
        if termek == 'paradicsom': egysegar = 1199
        elif termek == 'paprika': egysegar = 1349
        elif termek == 'vöröshagyma': egysegar = 289
        else : print('sajnálom, nincs ilyen tejmék! :(')
        if egysegar != 0:
            mennyiseg:float = float(input(f'hány kg {termek}-et szeretne vásárolni?: '))
            tetel:float = egysegar * mennyiseg
            osszar += tetel
print(f'összesen fizetendő: {osszar}')