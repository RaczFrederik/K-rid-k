



#függvény
def köridő(sor):
    '''
Ha bedobjuk a köridőt string-ként (00:00:00), akkor visszatér a másodpercekkel integer-ként'''
    minute = int(sor[4][3:5])
    sec    = int(sor[4][6:])
    return minute*60 + sec

#Class
class Autóverseny:
    def __init__(self,sor):
        s = sor.strip().split(';')
        self.csapat    = s[0]
        self.versenyző = s[1]
        self.eletkor   = int(s[2])
        self.palya     = s[3]
        self.köridő     = s[4]
        self.köridő_sec    = int(s[4][:2])*3600 + int(s[4][3:5])*60 + int(s[4][6:])
        self.kör       = int(s[5])


with open("autoverseny.csv", 'r', encoding = 'UTF-8-sig') as f:
    fejlec = f.readline()
    matrix = [Autóverseny(sor) for sor in f]

#3.fel.
    
print(f' 3.feladat: {len(matrix)}')

#4.fel.

for sor in matrix:
    if sor.versenyző == 'Fürge Ferenc' and sor.kör == '3' and sor.pálya == 'Gran Prix Circuit':
       print(f' 4. feladat: {sor.köridő_sec} másodperc')
    
#5.fel.
       
print(f' 5. feladat:')
név = input(f' Kérem egy versenyző nevét:\n')

#6.fel.

mini = 2**32
pálya = ''
for sor in matrix:
    if sor.versenyző == név:
        if sor.köridő_sec < mini:
            mini   = sor.köridő_sec
            pálya  = sor.pálya
            köridő = sor.köridő
            if pálya == '':
    print(f'6.feladat: Nincs ilyen versenyző az állományban!')
else:
    print(f'6.feladat: {pálya},{mini}')

    