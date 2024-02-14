#
# Esercizio 1: Numeri Dimenticati
#
def numeri_dimenticati(A):
    d = 0                       # conto dei numeri dimenticati
    i = 0                       # indice numero enunciato
    while i < len(A):
        if i + d + 1 == A[i]:   # il numero atteso è i + d + 1
            i = i + 1           # trovato: passa al prossimo
        else:
            print(i + d + 1)    # dimenticato: stampalo e 
            d = d + 1           # incrementa d
    if d == 0:
        print('molto bene')

#
# Esercizio 1: Numeri Dimenticati, versione 2
#
def numeri_dimenticati(A):
    bene = True                 # nessun numero dimenticato
    n = 1                       # numero atteso
    i = 0                       # indice numero enunciato
    while i < len(A):
        if n == A[i]:           # se il numero enunciato è quello atteso
            i = i + 1           # passa al prossimo
        else:
            bene = False        # altrimenti non va bene e            
            print(n)            # stampa il numero atteso (dimenticato)
        n = n + 1 
    if bene:
        print('molto bene')

#
# Esercizio 1: Numeri Dimenticati, versione 3
#
def numeri_dimenticati(A):
    bene = True                 # nessun numero dimenticato
    n = 1                       # numero atteso
    for a in A:
        if n < a:               # se Antonio enuncia a > n:
            bene = False
            while n < a:        # stampa tutti i numeri dimenticati
                print(n)
                n = n + 1
        n = n + 1
    if bene:
        print('molto bene')

#
# Esercizio 2: Repetita Juvant
#
def repetita_juvant(T):
    for t in T:                 # per ogni parola tripla t
        w = len(t)//3           # dimensione della parola originale
        for i in range(w):      # per ogni carattere
            # stampa il carattere comune in almeno due copie
            if t[i] == t[i+w] or t[i] == t[i+w+w]:
                print(t[i],end='')
            else:
                print(t[i+w],end='')
        print(' ',end='')
    print()

#
# Esercizio 3: Onda Verde
#
def onda_verde(P,R,V,l):
    t = 0                       # tempo corrente
    p = 0                       # posizione di Luca al tempo t
    for i in range(len(P)):     # per ogni semaforo i
        t = t + (P[i] - p)      # tempo d'arrivo alla posizione P[i]
        p = P[i] 
        ct = t % (R[i]+V[i])    # tempo dall'inizio di un ciclo rosso-verde
        if ct < R[i]:           # se il semaforo è rosso
            t = t + (R[i] - ct) # aspetta il tempo rimanente del rosso
    t = t + (l - p)
    return t

#
# Esercizio 4: Offerta Speciale
#
def offerta_speciale(P):
    X = sorted(P)               # ordina i pezzi per prezzo
    i = len(X)                  # partendo dall'ultimo (più costoso)
    c = 0                       # costo totale
    while i >= 3:               # finché si fanno gruppi di tre
        i = i - 3               # aggiungi il costo dei due maggiori
        c = c + X[i+1] + X[i+2]
    while i > 0:                # in ultimo aggiungi i rimanenti costi
        i = i - 1
        c = c + X[i]
    return c

