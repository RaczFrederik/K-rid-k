



#függvény
def köridő(sor):
    '''
Ha bedobjuk a köridőt string-ként (00:00:00), akkor visszatér a másodpercekkel integer-ként'''
    minute = int(sor[4][3:5])
    sec = int(sor[4][6:])
    return minute*60 + sec


with open("autoverseny.csv", 'r', encoding = 'UTF-8-sig') as f:
    fejlec = f.readline()
    matrix = [sor.strip().split(';') for sor in f]

#3.fel.
    
print(f' 3.feladat: {len(matrix)}')

#4.fel.

for sor in matrix:
    if sor[1] == 'Fürge Ferenc' and sor [5] == '3' and sor[3] == 'Gran Prix Circuit':
       print(f' 4. feladat: {köridő(sor)} másodperc')
    
#5.fel.
       
print(f' 5. feladat:')
név = input(f' Kérem egy versenyző nevét:\n')

#6.fel.

mini = '99:99:99'
pálya = ''
for sor in matrix:
    if sor[1] == név:
        if sor[4] < mini:
            mini = sor[4]
            pálya = sor[3]
if pálya == '':
    print(f'6.feladat: Nincs ilyen versenyző az állományban!')
else:
    print(f'6.feladat: {pálya},{mini}')
