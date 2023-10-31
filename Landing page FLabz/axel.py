import os, random
from colorama import init, Fore, Back, Style
"""
Nombre: Axel Javier Coronado Retiz
Matricula: A01286361
Carrera: Ingenieria Industrial y de Sistemas
Reflexión (qué aprendí): A lo largo de este proyecto, como primer aporte a mi conocimiento
fue el desafiarme a mi mismo del como conseguir que funcionara cada una de las funciones
,pero siento que aunque un fuese un mismo proyecto para todos mis compañeros
cada quien desarrollo la habilidad y el ingenio mental necesario para poder hacer el
proyecto

Fecha de entrega final: 15 de Octubre
"""

figura = "        ?        "

def ajusta_matriz(matriz):
    for r in range (len(matriz)):
        for c in range(len(matriz[0])):
            largo = len(matriz[r][c])
            matriz[r][c] += " " * (20 - largo)


def  despliega_tablero(opcion, tablero, r1 = None, c1 = None, r2 = None, c2 = None):
    """ 5 ptos, función que despliega la matriz en forma de un tablero muy bien formateado
    con una cuadricula. En caso de que la función reciba los parámetros  r1,c1, r2, c2, 
    la función debe resaltar usando un color las cartas seleccionadas y
    muestra el #renglon y #columna de la matriz
    1. Obtener la cantidad de renglones y columnas del tablero
    2. Desplegar los números de columna del tablero
    3. Ir desplegando cuadricula entre cada renglón del tablero
    3. Desplegar el contenido del tablero usando recorrido x posición
    4. Si la función recibe los parámetros r1,c1, r2, c2 -
        la función debe resaltar su contenido al desplegarlas en la pantalla
    """
    # Añade las instrucciones
    #Si r1 and c1 != None: marcar la posicion (emoji)
    
    # Desplegar las columnas de manera organizada y centrada
    print(end="  ")
    for columna in range(len(tablero)):
        print(f'{columna}'.center(13), end="")    
    print('\n'+"  "+"-------------"*len(tablero))
    
    # Desplegar cada renglon
    for r in range(len(tablero)):
        print(r, end="")
        print("|", end="")
        for c in range(len(tablero)):
            # Si posicion = carta destapada - imprime el emoji a un lado
            if ((r1 and c1) or (r2 and c2) != None):
                
                print(f'{tablero[r][c]}'.center(5), end="")
                
                if tablero[r][c] == tablero[r1][c1]:
                    print("\U0001F4A2", end="")
                    
                    
                elif tablero[r][c] == tablero[r2][c2]:
                    print("\U0001F4A2", end="")
                         
            else:
                print(f'{tablero[r][c]}'.center(5), end="")
            print("|", end="")
        print('\n'+"  "+"-------------"*len(tablero))
        

def generar_cartas_compu(tablero):
    """ 10 Ptos,
    - Para la carta 1
    Generar r1, y c1 usando random.randint( inf, sup) hasta que sea válido
    [3 ptos] Validar que no esté destapada 
    [3 ptos] Vuelve a generar la posición, si no es correcta
    - Para la carta2
    #     - generar r2 y c2 usando  random.randint( inf, sup) hasta que sea válido
    [4 ptos] Válidar que sea diferente que la carta1 """
    # Añade las instrucciones
    
    print(Fore.MAGENTA + "Tira la computadora...", Fore.RESET)
    r1 = random.randint(0, 3)
    c1 = random.randint(0, 3)
    
    # Si la primera carta no esta correcta
    while ((r1 < 0 or r1 > 3) or (c1 < 0 or c1 > 3)) or tablero[r1][c1] != figura:
        r1 = random.randint(0, 3)
        c1 = random.randint(0, 3)
        
    r2 = random.randint(0, 3)
    c2 = random.randint(0, 3)
    
    # Si la segunda carta no esta correcta
    
    while ((r2 < 0 or r2 > 3) or (c2 < 0 or c2 > 3)) or tablero[r2][c2] != figura:
        r2 = random.randint(0, 3)
        c2 = random.randint(0, 3)
        
    return r1, c1, r2, c2
         
         
def pares( ):
    """ 10 ptos, función que retorna una lista con emojis y palabras (duplicada)
    para que se formen los pares en la memorama.
    representan la parte derecha de las cartas que se van a descubrir
    """
    lista = []
    pares = """\U0001F600 \U0001F604 \U0001F606 \U0001F923 \U0001F643
\U0001F60A \U0001F618 \U0001F263A4
Safety \U0001F60B \U0001F92A \U0001F917
\U0001FAE3 \U0001F611 \U0001F60F \U0001F925 \U0001F60C \U0001F912"""

    
    lista = pares.split("\n")
    lista = lista * 2
    print(lista)
    print(len(lista))
    print(max(lista))
    return lista


def limpia_consola():
    """ función que limpia la consola """
    if os.name == "nt": # windows
        os.system("cls")
    else: # Mac/Linux
        os.system("clear")
        
        
def llena_tablero_visible(figura = "        ?        " ):
    """ 5 ptos, funcion que llena el tablero con las cartas visibles o las cartas volteadas,
    se inicializa con el mismo emoji - tu selecciona el tuyo"""
    tablero = []
    
    for r in range(4):
        renglon = []
        for c in range(4):
            renglon.append(figura)
            
    # Se lleno el renglon,  se añade a tablero
        tablero.append(renglon)

    return tablero


def llena_tablero_escondidas( lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] ):
    """ 10 ptos, función que llena la matriz con el valor derecho de las cartas ,
    es decir se inicializa la matriz con la lista que recibe como parametro de entrada"""
    escondidas = []
    
    # Formar la matriz de la memoria 4X4
    # Crear un nuevo renglon
    pos = 0
    for r in range(4):
        renglon = []
    # Llenar las columnas de renglon
        for c in range(4):
            renglon.append(lista[pos])
            pos = pos + 1
            
    #+ el renglon a la matriz
        escondidas.append(renglon)
    
    
    return escondidas


def leer_cartas_jugador(nombre, tablero):
    """ 10 Ptos,
     Para la  carta1 leer r1 y c2  [r1][c1]  para la carta2 leer r2 y c2 [r2][c2]
    [2.5 ptos] Validar la posicion
    [2.5 ptos] Validar que no esté destapada
    [2.5 ptos] Vuelve a leer si no es correcta
    Para la Carta2 [2.5 ptos] Válidar que sea diferente que la carta1
    retorna las 2 cartas que selecciono el jugador
    """
    print("Tira", nombre)
    r1 = int(input("r1 = "))
    c1 = int(input("c1 = "))
    
    # 1. rango 2. destapado?
    while((r1 < 0 or r1 > 3) or (c1 < 0 or c1 > 3)) or tablero[r1][c1] != figura:
        r1 = int(input("r1 = "))
        c1 = int(input("c1 = "))
       
     
    r2 = int(input("r2 = "))
    c2 = int(input("c2 = "))
    
    # 1. rango 2. esta destapada? 3. = carta1?
    while((r2 < 0 or r2 > 3) or (c2 < 0 or c2 > 3)) or tablero[r2][c2] != figura or (r1 == r2 and c1 == c2):
        r2 = int(input("r2 = "))
        c2 = int(input("c2 = "))
            
    return r1, c1, r2, c2
              

def son_pares(opcion, tablero, escondidas, r1, c1, r2, c2):
    """10 ptos, Retorna 1 si son pares, felicita, marca un sonido y
    Retorna 0 si no son pares y lo indica Destapa las cartas, Si no son pares las vuelve a 
    tapar.
    Para que muestre las cartas de otro color -
    1. poner visibles la carta1 y la carta2 (voltear - visible la parte escondida por eso la función
    recibe las 2 matrices tablero y escondidas
    2. Desplegar el tablero - resaltando las cartas que  eligio el jugador/computadora
        despliega_tablero(modo, tablero, r1, c1, r2, c2),
    3. Verificar si son pares, si si entonces dejar las cartas visibles 
            si si son sonido y retornar 1 y desplegar par
            si no son,  volver a cambiar el tablero a figura y retornar 0 desplegar Impar
    3. limpiar_consola( )
    4. Desplegar de nuevo el tablero sin resaltar las cartas del tablero :despliega_tablero(modo, tablero), """
    # Añade las instrucciones
    # destapar
    
    # 1. Destapar la cartas
    tablero[r1][c1] = escondidas[r1][c1] 
    tablero[r2][c2] = escondidas[r2][c2] 
    
    # 2. Desplegar el tablero
    despliega_tablero(opcion, tablero, r1, c1, r2, c2)
    
    # 3. Determinar si son pares las elecciones
    if escondidas[r1][c1] == escondidas[r2][c2]:
        print(Back.MAGENTA, Fore.YELLOW + "Son Pares, Felicidades!!" + Back.RESET, Fore.RESET)
        return 1
    else:
        print(Back.MAGENTA, Fore.YELLOW + "No Son Pares, Intentalo De Nuevo..." + Back.RESET, Fore.RESET)
        
        # 3.1 Tapar las cartas
        tablero[r1][c1] = figura
        tablero[r2][c2] = figura
        return 0 


def mi_memoria():
    
    pares = """\U0001F920 \U0001F60E \U0001F913 \U0001F615 \U0001F641 \U0001F62E \U0001F62F \U0001F626"""

    
    lista = pares.split("\n")
    lista = lista * 2
    print(lista)
    print(len(lista))
    print(max(lista))
    return lista
    
    
def main( ):
    global  figura
    """
    [20 ptos]
    Controla el funcionamiento general de la memorama
    0. Leer la opcion del juego 1. memorama de letras 2. memorama de emojis
    opcion 1 despliega la matriz solo con print
    iniciaizar las matrices:  tablero y escondidas
    
    1. Tira jugador (leer las cartas que selecciona el jugador 1  r1, c1, r2, c2)
    2. Validar que las cartas que selecciono el jugador sean correctas
    3. Verificar si son  par las cartas
    4. Si son par incrementar el  contador del jugador en uno
    6. Tiro computadora
    - generar r1, y c1 usando random.randint( inf, sup) hasta que sea válido
    - generar r2 y c2 usando  random.randint( inf, sup) hasta que sea válido
    8. Verificar si son par las cartas
    9. Si son par incrementar el  contador de la computadora en uno
    10. llevar un contador para llevar la cuenta de los pares que se  han destapado
    
    Termina correctamente cuando ya no hay cartas
    Desplegar el mensaje adecuado con Back.COLOR y centrado indicando
     quién gano o si hubo empate
"""
    #init( )
    limpia_consola()
    print("Opcion 2 = J1 vs. J2\n" + "Opcion 3 = J1 vs. Computadora\n")
    #      0. Leer la opcion del juego 1. memorama de letras 2. memorama de emojis
    opcion = int(input("Opcion de Juego: "))
    # 1. Leer el numero de pares que se requieren para ganar
    pares = int(input("Numero de Pares Para Ganar: "))
    
    # 2. Inicializar los contadores de los jugadores pares_jugador 1 pares_computadora jugador
    pares_j1 = 0
    pares_j2 = 0
    
    # 3. Inicializar
    if opcion >= 2:
        memoria = mi_memoria( )
        escondidas = llena_tablero_escondidas(memoria)
        tablero = llena_tablero_visible("    \U0001F92F\U0001F92F    ")
        figura = "    \U0001F92F\U0001F92F    "
        
    else:
        escondidas = llena_tablero_escondidas()
        tablero = llena_tablero_visible()
    
    # Cambia el contenido de cada elemento al mismo tamaño
    #ajusta_matriz(tablero)
    #ajusta_matriz(escondidas)
    #figura = tablero[0][0]
    despliega_tablero(opcion, tablero)
    despliega_tablero(opcion, escondidas)
    destapadas = 0
    # ciclo centinela para se ejecute hasta que se cumpla la codición
    # while destapadas     :
    
    while pares_j1 + pares_j2 < pares:
        # Mostrarle el tablero al Jugador 1
        despliega_tablero(opcion, tablero)
        
        #     1. Tira jugador (leer las cartas que selecciona el jugador 1  r1, c1, r2, c2)
        #print(r1,c1, r2, c2)
        r1, c1, r2, c2 = leer_cartas_jugador("Jugador1", tablero)
        print("carta1 =",r1,",",c1,"carta2 =",r2,",",c2,)
        
        
        # incrementar el contador del jugador
        pares_j1 += son_pares(opcion,tablero,escondidas,r1,c1,r2,c2)
        
        # desplegar pares del jugador
        print(Fore.BLUE + "Pares Jugador1 =", pares_j1, Fore.RESET)
        
        despliega_tablero(opcion, tablero)
        # Verificar si es opcion 1 = otro jugador, opcion 2 =  computadora
        if opcion != 3 and (pares > pares_j1 + pares_j2):
            r1,c1,r2,c2 = leer_cartas_jugador("Jugador2", tablero)
            print("carta1 =",r1,",",c1,"carta2 =",r2,",",c2,)
            pares_j2 += son_pares(opcion,tablero,escondidas,r1,c1,r2,c2)
            print(Fore.MAGENTA + "Pares Jugador2 =", pares_j2, Fore.RESET)
        
        elif opcion == 3 and (pares > pares_j1 + pares_j2): # Jugar contra la computadora
            r1,c1,r2,c2 = generar_cartas_compu(tablero)
            print("carta1 =",r1,",",c1,"carta2 =",r2,",",c2,)
            pares_j2 += son_pares(opcion,tablero,escondidas,r1,c1,r2,c2)
            print(Fore.MAGENTA + "Pares Computadora =", pares_j2, Fore.RESET)
    
            #verificar quien gano. jugador1 jugador2 computadora empate
    if pares_j1 == pares_j2:
            print("\U0001F601\U0001F609\U0001F607\ EMPATE!! \U0001F601\U0001F609\U0001F607\n")
    elif pares_j1 > pares_j2:
            print("\U0001F601\U0001F609\U0001F607\ GANO EL JUGADOR1!! \U0001F601\U0001F609\U0001F607\n")
    elif pares_j2 > pares_j1:
            print("\U0001F601\U0001F609\U0001F607\ GANO EL JUGADOR2!! \U0001F601\U0001F609\U0001F607\n")
    elif opcion == 3 and pares_j2 > pares_j1:
            print("\U0001F601\U0001F609\U0001F607\ GANO LA PC!! \U0001F601\U0001F609\U0001F607\n")


                
main()