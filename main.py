from random import choice

cartas = {
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
}

lista_cartas = list(cartas)*4

def seleccion_carta():
    carta = choice(lista_cartas)
    score = score = cartas[carta]
    return carta, score

def entregar_carta(entregas):
    carta = list(range(entregas))
    score = 0
    for i in range(entregas):
        carta[int(i)] = seleccion_carta()[0]
        score += seleccion_carta()[1]
    return carta, score

def mostrar_cartas(usuario, resultado, entregas):
    carta, score = entregar_carta(entregas)
    print(usuario, end=" ")
    print(carta, end=" ")
    print(resultado, score)
    return carta, score

def primera_jugada():
    mis_cartas, mi_score = mostrar_cartas("Ha obtenido:", " >>> su puntuación es de", 2)
    banca_cartas, banca_score = mostrar_cartas("La banca tiene:", " >>> su puntuación es de", 2)
    if mi_score == 21 and mi_score != banca_score:
        print("Blackjack! Has Ganado!")
    elif banca_score < mi_score :
         print("Has ganado!")
    else:
        print("Has perdido!")
primera_jugada()    

