#
# Esercizio 1
# 
def shopping(P):
    # Con unq semplice scansione dei prezzi, per ogni nuovo prezzo p
    # in P, controlliamo se è maggiore di quello corrente.  Nel caso,
    # Luca compra lo smartphone, quindi aggiungiamo p alla spesa
    # totale e impostiamo il prezzo corrente a p.
    #
    v = 0                       # prezzo dello smartphone corrente
    t = 0                       # spesa totale 
    for p in P:
        if p > v:
            t = t + p
            v = p
    return t

#
# Esercizio 2
#
def trova_criminale(P, k):
    # P è una sequenza di valori tali che P[i] indica la prossima
    # posizione da controllare indicata dalla persona interrogata alla
    # posizione i.  Partiamo quindi da i = 0 e ci spostiamo alla
    # prossima posizione i = P[i] finchè non arriviamo alla posizione
    # k dove si nasconde Luca.  Il problema però è che possiamo
    # entrare in un ciclo, per esempio se la prima persona mi manda
    # alla posizione 3 e la persona alla posizione 3 rimanda alla
    # posizione 0.  In questo caso la polizia non troverà mai Luca e
    # quindi bisgona ritornare -1.  Il problema è capire che siamo
    # entrati in un ciclo.  Lo facciamo tenendo traccia delle
    # posizioni visitate.  Se arriviamo ad una posizione che abbiamo
    # già visitato vuol dire che siamo entrati in un ciclo.
    n = len(P)
    i = 0                       # posizione della polizia
    N = [ False ] * n           # N[i] indica se la posizione è stata controllata
    t = 0                       # tentativi falliti
    while i != k:               # finché non troviamo Luca
        t = t + 1
        if N[i]:                # se siamo già passati dalla posizione i
            return -1           # vuol dire che siamo entrati in un ciclo
        N[i] = True
        i = P[i]
    return t

#
# Esercizio 3
#
def scala(P):
    s = 0
    precedente = None
    for p in P:
        if precedente == None:
            s = p
        elif p - precedente > s:
            s = p - precedente
        precedente = p
    return s

#
# Esercizio 4
#

def taglia(n):
    # Con v tagli verticali e h tagli orizzontali, il numero di fette
    # di torta che si ottengono è (v+1)*(h+1).  Dobbiamo quindi
    # massimizzare il valore del prodotto (v+1)*(h+1) col vincolo che
    # la somma v+h sia uguale a n.  È noto che il valore ottimo si
    # ottiene con v e h il più vicini possibile tra di loro e quindi
    # alla metà di n.
    #
    # Un modo di dimostrare questa condizione è di pensare all'area di
    # un rettangolo di dimensioni AxB con A+B=N.  Ma vorse è ancora
    # più semplice farlo in modo algebrico.  Il problema è simmetrico
    # tra A e B quindi le condizioni valgono scambiando A e B.
    # Partiamo considerando il caso A < B.  Data l'area A*B (con A<B)
    # ci conviene incrementare A e quindi decrementare B?  Il prodotto
    # iniziale è A*B e il prodotto nuovo sarebbe (A+1)(B-1).  La
    # differenza è B - A - 1.  Quindi, ci conviene passare ad A+1,B-1
    # fintanto che B - A > 1.  Quindi il massimo si raggiunge quando
    # B-A <= 1 e per simmetria A-B >=1.  Quindi quando -1 <= B-A <= 1.

    v = n // 2                  # numero ottimale di tagli verticali
    h = n - v                   # numero ottimale di tagli orizzontali
    return (v + 1)*(h + 1)

#
# Esercizio 5
#
def bonta(B, k):
    # troviamo il massimo tra tutte le possibili somme di k elementi
    # consecutivi in B.  Calcoliamo la prima somma dei i primi k
    # elementi e poi calcoliamo ogni somma successiva aggiungendo il
    # prossimo elemento in posizione i e rimuovendo l'elemento in
    # posizione i - k.
    #
    # Complessità: Theta(n)

    n = len(B)
    if n < k:
        return None
    v = 0                       # valore corrente
    for i in range(k):
        v = v + B[i]
    m = v                       # valore della scelta migliore corrente
    for i in range(n - k):
        v = v - B[i] + B[i + k]
        if v > m:
            m = v
    return m

#
# Esercizio 6
#
import math
def buoni_pasto(t):
    # Il modo di usare più buoni possibile è di usare quelli con
    # valore minimo, cioè 1, ma siccome un valore non può essere usato
    # più di due volte, si possono usare tutti i valori crescenti a
    # partire da 1.  Più precisamente, si possono usare al più n buoni
    # per un totale 1+2+...+n <= t.  Siccome 1+2+...+n=n(n+1)/2, il
    # modo più semplice è risolvere l'equazione n(n+1)/2 <= t.
    # Rispolverando la formula dell'equazione quadratica...
    return int((-1 + math.sqrt(1+8*t)) / 2)

#
# Esercizio 7
#
def piega_foglio(w,h,k):
    # l'algoritmo fa le pieghe come dalla specifica del problema.
    for i in range(k):
        if w >= h:
            w = w - w // 2
        else:
            h = h - h // 2
    print(w,h)

#
# Esercizio 8
#
def paia_di_scarpe(S,D):
    # per appaiare le scarpe potremmo cercare nella sequenza di destra
    # ogni valore che leggiamo nella sequenza di sinistra, ma poi
    # dobbiamo preoccuparci di rimuovere in qualche modo le scarpe già
    # usate nella sequenza di destra.  È invece più semplice ed
    # elegante ordinare preventivamente le due sequenze e quindi poi
    # considerare le due sequenze da destra a sinistra...
    # 
    A = sorted(S)               # sequenza di scarpe sinistre ordinate
    B = sorted(D)               # sequenza di scarpe destre ordinate
    i = 0                       # indice nella sequenza di sinistre
    j = 0                       # indice nella sequenza di destre
    c = 0                       # paia di scarpe complete
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i = i + 1
        elif A[i] > B[j]:
            j = j + 1
        else:
            c = c + 1
            i = i + 1
            j = j + 1
    return c

