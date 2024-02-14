#
# Esercizio 11
#
def sopra_la_media(R,k):
    # calcolo la media e poi la confronto col valore in posizione k

    T = 0                       # soma di tutti gli ementi
    for r in R:
        T = T + r
    return R[k] > T/len(R)

#
# Esercizio 12
#
def coniglio_al_guinzaglio(dx,dy,X,Y):
    # provo tutti i punti di coordinate x,y (0<=x<=dx, 0<=y<=dy):
    # ritorno il primo punto P = (x,y) tale che la distanza tra P e
    # tutti i bordi del tetto è maggiore o uguale alla distanza tra P
    # e tutti i vasi.
    
    n = len(X)
    for x in range(1,dx):
        for y in range(1,dy):
            r = x               # calcoliamo la distanza minima r
            if dx - x < r:      # tra il punto (x,y) e uno dei bordi
                r = dx - x      # del tetto.
            if y < r:
                r = y
            if dy - y < r:
                r = dy - y

            found = True        # verifichiamo che il punto (x,y) non sia a 
            for i in range(n):  # distanza maggiore di r da uno dei vasi.
                if x == X[i] and y == Y[i]:
                    found = False
                    break
                if (x - X[i])*(x - X[i]) + (y - Y[i])*(y - Y[i]) > r*r:
                    found = False
                    break
            if found:
                print(x,y)
                return
    print('impossibile')

#
# Esercizio 13
#
def passaggio_nord_sud(M):
    # Si può dimostrare che la mappa è una specie di labirinto
    # speciale, nel senso che i percorsi non si biforcano mai.  Ossia,
    # si tratta semplicemente di seguire ogni singolo percorso
    # partendo dagli ingressi a Nord e procedendo inizialmente verso
    # Sud.  Se il percorso porta ad un'uscita a Sud, il passaggio è
    # trovato.  Altrimenti, se il percorso porta ad un'uscita a Nord,
    # Est o Ovest, si prova il prossima entrata.
    #
    # Il problema è dunque seguire un percorso.  L'idea è di muoversi
    # come una palla che rimbalza sui muri del labirinto.  Per
    # esempio, considera la mappa sotto, con la palla (*) che si muove
    # in direzione Sud (verso il basso):
    #
    #        v
    #        *
    # '╲╱╱╱╲╱╲╲╱╱'              M[0], riga 0
    # '╲╱╱╲╱╱╲╱╲╲'              M[1], riga 1
    # '╲╲╲╲╲╱╲╱╱╱'              ...
    # '╲╱╱╱╱╲╱╲╲╱'
    #
    # La palla entra nella casella in posizione (r,c), dove r è il
    # numero di riga contato partendo da 0 partendo dall'alto, e c è
    # il numero della colonna contato da 0 partendo da sinistra.  La
    # palla entra inizialmente in (r,c) muovendosi in direzione Sud,
    # cioè verso il basso, e lì incontra un muro in diagonale a -45
    # gradi '\', quindi venendo dall'alto rimbalza verso destra,
    # quindi la nuova posizione sarà (r,c=c+1) e la nuova direzione
    # del movimento sarà verso Est.  Nella nuova posizione, c'è di
    # nuovo un muro a -45 gradi (\), ma questa volta la palla arriva
    # muovendosi verso destra, e quindi rimbalza verso il basso nella
    # posizione (r+1,c), e così via.
    #
    NO='\u2572'                 # \
    NE='\u2571'                 # /
    R = len(M)
    C = len(M[0])
    for c in range(C):
        r = 0                   # posizione (r,c) cioè riga,colonna
        d = 'S'                 # direzione di movimento
        while c >= 0 and c < C and r >= 0 and r < R:
            m = M[r][c]         # muro nella posizione (r,c)
            if m == '/':
                m = NE
            elif m == '\\':
                m = NO
            if d == 'S' and m == NE or d == 'N' and m == NO:
                    d = 'O'
                    c = c - 1
            elif d == 'S' and m == NO or d == 'N' and m == NE:
                    d = 'E'
                    c = c + 1
            elif d == 'O' and m == NE or d == 'E' and m == NO:
                    d = 'S'
                    r = r + 1
            elif d == 'O' and m == NO or d == 'E' and m == NE:
                    d = 'N'
                    r = r - 1
            if r == R:          # abbiamo raggiunto il Sud
                return True
            if r < 0 or c < 0 or c >= C:
                break;
    return False

#
# Esercizio 14
#
def anima(T):
    for w in T:                 # per ogni parola w del testo T
        i = 0                   
        while i < len(w):       # per ogni posizione i della parola w 
            print(w[i],end='')  # stampiamo la lettera w[i] in posizione i
            if w[i] == 'a' or w[i] == 'e' or w[i] == 'i' or w[i] == 'o' or w[i] == 'u':
                # se la lettera è una vocale
                if i + 2 < len(w) and w[i+1] == 's' and w[i+2] == w[i]:
                    # e se la vocale è seguita da 's' e dalla stessa vocale
                    # allora saltiamo la 's' e la vocale
                    i = i + 2
            i = i + 1
        print(' ',end='')
    print()

#
# Esercizio 15
#
def percorso_minimo(P):
    # Qui bisogna ragionare su quale può essere un percorso chiuso
    # (cosiddetto "Hamiltoniano") minimo per visitare una serie di
    # punti su una linea.  Si può notare e anche dimostrare
    # formalmente che, partendo da un punto qualunque tra la posizione
    # (coordinata) minima e quella massima, il percorso chiuso minimo
    # è il ciclo che va dal punto di partenza alla coordinata massima,
    # poi a quella minima, e poi di nuovo al punto di partenza (o
    # vice-versa).  Quindi si tratta semplicemente di calcolare il
    # doppio della distanza tra la coordinata massima e quella minima.
    a = P[0]
    b = P[0]
    for p in P:
        if p > b:
            b = p
        elif p < a:
            a = p
        
    return (b - a)*2
>
