# Algorithmes de tri extraits du manuel de cours UE J1MI2013 : Algorithmes et
# Programmes par Alain Griffault, version du 19 mai 2015.
# Programmes modifiés pour retourner le nombre d'étape élémentaires de calcul

# Fonctions auxiliaires
def estIndice(T,i):
    return(0<=i and i<len(T))

def echange(T,i,j):
    assert(estIndice(T,i) and estIndice(T,j))
    aux  = T[i]
    T[i] = T[j]
    T[j] = aux

def decalageDroite(T,g,d):
    assert(g<=d and estIndice(T,g) and estIndice(T,d))
    nb_etapes = 0
    aux = T[d]
    for k in range(d,g,-1):
        T[k] = T[k-1]
        nb_etapes += 1
    T[g] = aux
    return(nb_etapes)

def decalageGauche(T,g,d):
    assert(g<=d and estIndice(T,g) and estIndice(T,d))
    aux = T[g]
    nb_etapes = 0
    for k in range(g,d):
        T[k] = T[k+1]
        nb_etapes += 1
    T[d] = aux
    return(nb_etapes)

# Fonctions de tris simples (sélection, bulle, insertion)

# Tri selection. Etapes élémentaires = comparaisons entre paires d'éléments
def triSelection(T):
    nb_etapes = 0
    for i in range(len(T)-1):
        iMin=i
        for j in range(i+1,len(T)):
            nb_etapes += 1
            if T[j]<T[iMin]:
                iMin = j
        if iMin != i :
            echange(T,i,iMin)
    return(nb_etapes)

# Tri bulle. Etapes élémentaires = comparaisons entre paires d'éléments et décalages
def triBulle(T):
    nb_etapes = 0
    for i in range(len(T)-1,0,-1):
        for j in range(i):
            nb_etapes += 1
            if T[j]>T[j+1]:
                nb_etapes += decalageDroite(T,j,j+1)
    return(nb_etapes)

# Tri insertion. Etapes élémentaires = comparaisons entre paires d'éléments et décalages
def triInsertion(T):
    nb_etapes = 0
    for i in range(1,len(T)):
        j = i-1;
        while j>=0 and T[i]<T[j]:
            nb_etapes += 1
            j -= 1
        nb_etapes += 1
        nb_etapes += decalageDroite(T,j+1,i)
    return(nb_etapes)

# Tri par fusion. Etapes élémentaires = comparaisons entre paires d'éléments et recopie d'éléments
def fusionner(T,g,m,d):
    R = [0]*(d-g+1)
    i = g
    j = m+1
    k = 0
    nb_etapes = 0
    while i<=m and j<=d:
        nb_etapes += 1
        if T[i]<=T[j]:
            R[k] = T[i]
            i += 1
        else:
            R[k] = T[j]
            j += 1
        k += 1
    while i<=m:
        nb_etapes += 1
        R[k] = T[i]
        i += 1
        k += 1
    while j<=d:
        nb_etapes += 1
        R[k] = T[j]
        j += 1
        k += 1
    for k in range(len(R)):
        nb_etapes += 1
        T[g+k] = R[k]
    return(nb_etapes)
        
def triFusionRec(T,g,d):
    nb_etapes = 0
    if g<d:
        m = (g+d)//2
        nb_etapes += triFusionRec(T,g,m)
        nb_etapes += triFusionRec(T,m+1,d)
        nb_etapes += fusionner(T,g,m,d)
    return(nb_etapes)

def triFusion(T):
    return(triFusionRec(T,0,len(T)-1))

# Tri par tas (tire de http://dept-info.labri.fr/ENSEIGNEMENT/algoprog/examens-DS/DST-2014-corrige.pdf)
# Etapes élémentaires = echanges
def gauche(i):
    return(2*i+1)
def droite(i):
    return(2*(i+1))
def pere(i):
    return((i-1)//2)

def maximum(T,i,limite):
    assert(0<=i and i<limite and limite<=len(T))
    iMax = i
    g = gauche(i)
    d = droite(i)
    # maximum entre T[i], T[g] et T[d] avec getd<limite
    if g<limite and T[g]>T[iMax]:
        iMax = g
    if d<limite and T[ d]>T[iMax]:
        iMax = d
    return(iMax)

def entasser(T,i,limite):
    iMax = maximum(T,i,limite)
    nb_etapes = 0
    while iMax!=i:
        echange(T,i,iMax)
        nb_etapes += 1
        i    = iMax
        iMax = maximum(T,i,limite)
    return(nb_etapes)

def construireTas(T):
    nb_etapes = 0
    for i in range((len(T)-1)//2,-1,-1):
        nb_etapes += entasser(T,i,len(T))   

def trierTas(T):
    nb_etapes = 0
    for i in range(len(T)-1,0,-1):
        echange(T,0,i)
        nb_etapes += 1+entasser(T,0,i)
    return(nb_etapes)

def triParTas(T):
   construireTas(T)
   return(trierTas(T))
