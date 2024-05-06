vez = input("írd be a vezetékneved:  ").lower()
ker = input("írd be a keresztneved: ").lower()


import random
random_szam = random.randint(100, 999)


jelszo = vez[:2] + ker[-2:].upper() + str(random_szam)

print("a jelszavad: " + jelszo)