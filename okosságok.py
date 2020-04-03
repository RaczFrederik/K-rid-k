def köridő(sor):
    '''
Ha bedobjuk a köridőt string-ként (00:00:00), akkor visszatér a másodpercekkel integer-ként'''
    minute = int(sor[4][3:5])
    sec = int(sor[4][6:])
    return minute*60 + sec
