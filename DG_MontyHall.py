#importaciones
import numpy as np
from random import shuffle
#funcion que permite poner aleatorio la lista a generar
def sort_doors():
    lista = ['goat','goat','car']
    #esto revuelve la lista
    shuffle(lista)
    return lista
#funcion de escoger una puerta aleatoria
def choose_doors():
    a = [0,1,2]
    #se escoge dentro del arreglo
    valor = np.random.choice(a)
    return valor
#revela la puerta de la cabra
def reveal_door(lista, choice):
    #recorre la lista verifica si es el del choice osea el del escogido
    #y si no entonces mira si es goat y si es goat lo cambia a GOAT_MONTY
    for i in range(0,3):
        if(i!=choice):
            if(lista[i]=='goat'):
                lista[i]='GOAT_MONTY'
                i = 3
    return lista

#retorna el resultado
def finish_game(lista,choice,change):
    #si no cambia entonces envia el resultado
    if (change==False):
        return lista[choice]
    #si si cambia pues verifica la tercera opcion la que no habia escogido ni
    #la abierta
    else:
        for i in range(0,3):
            if(i!=choice):
                if(lista[i]!='GOAT_MONTY'):
                    return lista[i]
#se simula el juego entre 100
def simular_game():
    #primero si cambia
    change = True
    #lista que se guardara si lo saco bien
    r=[]
    #recorrido de 100
    for i in range(0,100):
        #se inicializa la lista y lo que escogio despues se revela la puerta
        #por ultimo se da el resultado
        lista = sort_doors()
        choice = choose_doors()
        lista = reveal_door(lista,choice)
        resultado = finish_game(lista,choice,change)
        #si el resultado es carro entonces se guarda en la lista uno de correcto
        if(resultado=='car'):
            a = 1
            r.append(a)
            #sino 0 que fue incorrecto
        else:
            a = 0
            r.append(a)
    #Se hace lo mismo pero con false de que no cambia
    change = False
    r2=[]
    for i in range(0,100):
        lista = sort_doors()
        choice = choose_doors()
        lista = reveal_door(lista,choice)
        resultado = finish_game(lista,choice,change)
        
        if(resultado=='car'):
            a = 1
            r2.append(a)
        else:
            a = 0
            r2.append(a)
      
    proba1 = 0
    proba2 = 0
    #Se suma en la lista los valores de cada probabilidad
    for i in range(0,len(r)):
        proba1 = proba1+r[i]
        proba2 = proba2+r2[i]
        
        #se divide por el numero el tamano que en este caso es 100
    proba1 = proba1/100.
    proba2 = proba2/100.
    #Se imprime
    print "La probabilidad de si se cambia es de: "
    print proba1
    print "La probabilidad si no se cambia es de:"
    print proba2
#Se simula
simular_game()
