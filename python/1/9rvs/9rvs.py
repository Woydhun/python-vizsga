szoveg:str = input('írjon be egy legalább 9 karakterből álló szöveget: ')
if len(szoveg) > 8: print(szoveg.lower()[::-1])
else: print('hiba!')

if len(szoveg) > 8:
        for i in range(len(szoveg)):
            print(szoveg[len(szoveg) - i - 1].lower(), end='')
else: print(f'a {szoveg} nincs legalább 9 karakter')