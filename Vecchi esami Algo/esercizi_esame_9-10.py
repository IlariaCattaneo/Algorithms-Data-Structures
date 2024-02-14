#
# Esercizio 9 (due soluzioni)
#
def chilometri_mai_visti(A,B,p,q):
    # L'idea è di indicare ogni passeggiata con un +1 all'inizio e un
    # -1 alla fine.  Più specificatamente, ogni passeggiata che inizia
    # al chilometro A e finisce al chilometro B, con A<B, viene
    # rappresentata due coppie (A,+1) e (B,-1).  In questo modo,
    # percorrendo il sentiero, ossia ordinando le coppie per
    # posizione, basta scorrere le coppie e sommare tutti i valori del
    # secondo elemento delle coppie.  Questo ci dà in ogni posizione
    # il numero di volte che Luca ha visitato quella posizione.

    X = []                      # sequenza delle coppie (pos,+ o - 1)
    n = len(A)
    for i in range(n):
        a = A[i]
        b = B[i]
        if b < a:               # per sicurezza...
            a, b = b, a
        if a < q and b > p:     # escludendo le passeggiate irrilevanti
            x.append((a,+1))
            X.append((b,-1))
    X.append((p,0))             # usiamo delle coppie di inizio e fine
    X.append((q,0))
    X.sort()                    # ordinamento delle coppie
    prev = p
    l = 0                       # somma progressiva o "livello"
    k = 0
    for x in X:                 # calcolo della somma progressiva.
        if l == 0 and x[0] >= p and x[0] <= q:
            # quando siamo tra p e q e il livello è zero (nessuna
            # visita), contiamo il percorso come chilometri mai visti
            k = k + (x[0] - prev)
        l += x[1]
        if l == 0:
            prev = x[0]
    return k

def chilometri_mai_visti2(A,B,p,q):
    # L'idea è di memorizzare una serie di segmenti disgiunti del
    # sentiero.  In particolare, l'idea è di combinare ogni coppia di
    # segmenti parzialmente sovrapposti in un solo segmento, e di
    # farlo ripetutamente finché non rimangono segmenti disgiunti.
    # Con quelli poi possiamo direttamente calcolare le parti non
    # viste.

    X = []                      # X e Y contengono rispettivamente 
    Y = []                      # l'inizio e la fine degli intervalli
                                # rilevanti
    for i in range(len(A)):
        x = A[i]                # inizio dell'intervallo percorso
        y = B[i]                # fine dell'intervallo
        if y < x:               # nel caso l'input sia inverso
            x, y = y, x
        if y <= p or q <= x:    # ignora gli intervalli irrilevanti
            continue
        if x < p:               # taglia quelli rilevanti a [p,q]
            x = p
        if y > q:
            y = q
        X.append(x)
        Y.append(y)
    i = 0
    n = len(X)
    while i < n:                # combiniamo tutti gli intervalli
        j = i + 1               # anche solo parzialmente sovrapposti
        while j < n:
            if X[i] > Y[j] or X[j] > Y[i]:
                j = j + 1
            else:
                # se l'intervallo i si sovrappone anche solo
                # parzialmente all'intervallo j, calcola l'unione
                # dei due intervalli e la assegna all'intervallo i
                if X[i] > X[j]:
                    X[i] = X[j]
                if Y[i] < Y[j]:
                    Y[i] = Y[j]
                # e poi di fatto cancella l'intervallo j spostando in
                # posizione j l'ultimo intervallo rimasto:
                n = n - 1
                X[j] = X[n]
                Y[j] = Y[n]
                # e poi ripartiamo da capo, nel caso che l'unione
                # copra altri intervalli considerati disgiunti
                j = i + 1
        i = i + 1
    # ora X e Y rappresentano n intervalli disgiunti e contenuti
    # nell'intervallo p,q.  Quindi...
    result = q - p
    for i in range(n):
        result = result - (Y[i] - X[i])
    return result
        
#
# Esercizio 10
#
def sport_della_domenica(C):
    # Manteniamo un indice della prossima attività da svolgere.  Ogni
    # sette giorni, contiamo il totale delle calorie, e per ogni 1000
    # calorie in eccesso alle 14000 del fabbisogno settimanale
    # stimato, aggiungiamo un'altra attività dopo quella fissa
    # settimanale.
    S = ['canottaggio', 'corsa', 'trazioni']
    g = 0                       # giorno della settimana
    k = 0                       # calorie totali della settimana
    s = 0                       # indice della prossima attività sportiva 
    for c in C:
        g = g + 1 
        k = k + c
        if g == 7:
            a = 1               # conto delle attività da svolgere
            if k > 14000:
                a += (k - 14000) // 1000
            while a > 0:
                a = a - 1
                print(S[s],end=' ')
                s = s + 1
                if s == len(S):
                    s = 0
            print()
            g = 0
            k = 0
