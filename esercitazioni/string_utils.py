def imprimeLista(lista):
    i = 0
    while i < len(lista):
        print("[",i,"]",lista[i])
        if type(lista[i]) == type(lista) and type(lista) != type(""):
            imprimeLista(lista[i])
        i=i+1
