def somma_tempi(A,B):
    A[3] = A[3] + B[3]          # secondi:
    A[2] = A[2] + A[3] // 60    # normalizzazione e riporto sui minuti
    A[3] = A[3] % 60
    A[2] = A[2] + B[2]          # minuti:
    A[1] = A[1] + A[2] // 60    # normalizzazione e riporto sulle ore
    A[2] = A[2] % 60 
    A[1] = A[1] + B[1]          # ore:
    A[0] = A[0] + A[1] // 24    # normalizzazione e riporto sui giorni
    A[1] = A[1] % 24
    A[0] = A[0] + B[0]          # giorni

def somma_tempi(A,B):
    # Seconda variante: scrivo le somme e i vari riporti in un ciclo
    # invece che scriverli esplicitamente come nella prima variante.
    #
    M = [0,24,60,60]            # array di "moduli" per il calcolo dei
                                # valori e dei riporti.
    for i in [3, 2, 1]:
        A[i] = A[i] + B[i]
        A[i-1] = A[i-1] + A[i] // M[i]
        A[i] = A[i] % M[i]
    A[0] = A[0] + B[0]

def posizione_finale(M):
    x = 0
    y = 0
    for m in M:
        if m == 'N':
            y = y + 1
        elif m == 'S':
            y = y - 1
        elif m == 'E':
            x = x + 1
        elif m == 'O':
            x = x - 1
    print(x,y)

def temperature_medie_giornaliere(T):
    i = 0
    g = 1                       # giorno corrente
    while i + 24 <= len(T):     # ho una giornata intera di misurazioni
        n = 0                   # numero di misurazioni valide
        t = 0                   # totale delle misurazioni valide
        for j in range(i,i+24): # per ogno misurazione del giorno
            if T[j] >= -40 and T[j] <= 50:
                n = n + 1       # conto le misurazioni valide
                t = t + T[j]    # sommo le misurazioni valide
        if n < 5:
            print('giorno',g,'sensore guasto')
        else:
            print('giorno',g,t/n)
        i = i + 24
        g = g + 1

def gioco_della_somma(C):
    n = len(C)
    D = [0]*n                   # mazzo di carte di destra
    i = 0                       # numero di carte sul mazzo di destra
    for c in C:
        if i >= 2 and D[i-1] + D[i-2] == c:
            i = i - 2           # elimino le due carte in cima al mazzo D
        else:
            D[i] = c            # aggiungo c in cima al mazzo di destra
            i = i + 1
    return i*2 < n
