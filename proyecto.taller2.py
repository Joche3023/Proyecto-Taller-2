import random

"""
ÍNDICE DE CÓDIGO:

(0) Mensajes de error
(1) Funciones secundarias del menú
(2) Listas y funciones para las areas verdes
(3) Listas y funciones para las personas
(4) Asignación y distribución de personas en las areas verdes
(5) Interacción jugador-persona
(6) Menú principal y nombre del jugador

"""

# (0) Mensajes de error y validaciones

def validar_entero(texto):
    """
    Funcion que recibe un texto y devuelve True si el elemento que
    representa el string es un entero positivo Por ejemplo:
    validar_entero("951") = True, validar_entero("lol") = False
    E: texto
    S: True si representa un entero, False si no
    R: entrada debe ser texto. Además, hay que validar que si es vacio, 
    la salida sea False. (es necesario que sea así para el proyecto)
    """
    if texto == "":
        return False
        
    else:
        return validar_entero_aux(texto, 0, len(texto))

def validar_entero_aux(texto,ind,fin):

    lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    if ind == fin:
        return True
        
    elif en(texto[ind],lista) == False:
        return False
        
    else:
        return validar_entero_aux(texto,ind+1,fin)

def en(elem, lista):
    """
    Funcion que devuelve True si elem está en la lista, False si no
    es una función auxiliar de validar_entero(texto,ind) no hace 
    validaciones.
    
    E: Elemento cualquiera y lista
    S: True si el elemento esta en la lista, False si no
    R: Lista debe ser list
    """
    return en_aux(elem, lista, 0, len(lista))

def en_aux(elem,lista,ind,fin): #Fn auxiliar
    if ind == fin:
        return False
        
    elif elem == lista[ind]:
        return True
        
    else:
        return en_aux(elem,lista,ind+1,fin)

def error_numero(personas): 
    """
    Función de error cuando se ingresa un numero que no está en la lista
    dada en la funcion seleccionar_persona_aux
    """
    ind = input("Ingrese un numero valido [ ]: ")
    
    if validar_entero(ind) == False:
        return error_numero(personas)
        
    else:
        ind = int(ind)
        
        if ind >= 1 and ind <= len(personas):
            return personas[ind - 1]
            
        else:
            return error_numero(personas)

def error_1tecla(): #Mensaje de error para cuando solo hay una tecla válida 
    newtecla = input("Tecla inválida, favor presionar una tecla válida. [1]: ")
    
    if newtecla == "1":
        return menu_principal(name)
        
    else:
        return error_1tecla()

def error_tipo_1(): #Error para inputs no int de crear_areas_verdes()
    nuevas_areas = input("Valor invalido, digite un numero valido [ ] " )
    if validar_entero(nuevas_areas) == False:
        return error_tipo_1()
        
    else: 
        areas = int(nuevas_areas)
        return crear_areas_verdes_aux(areas, [])

def error_tipo_2(): #Error para inputs no int de crear_personas()
    nuevas_personas = input("Valor invalido, digite un numero valido [ ] " )
    
    if validar_entero(nuevas_personas) == False:
        return error_tipo_2()
        
    else: 
        personas = int(nuevas_personas)
        return crear_personas_aux(personas, [])

def error_tipo_3(personas): #Error para inputs no int de seleccionar_personas()
    nueva_seleccion = input("Valor invalido, digite un numero valido [ ] " )
    
    if validar_entero(nueva_seleccion) == False:
        return error_tipo_3(personas)
        
    else: 
        seleccion = int(nueva_seleccion)
        return seleccionar_persona_aux(personas, seleccion)

def error_tipo_4(distribuidas):
    """
    Error para cuando el input de la funcion seleccionar_area_aux() no es
    un entero o esta fuera del rango permitido
    """
    nueva_seleccion = input("¿Segur@ que quieres salir? [-] " )
    
    if validar_entero(nueva_seleccion) == False:
        return salir()
        
    else:
        seleccion = int(nueva_seleccion)
        if seleccion >= 1 and seleccion <= len(distribuidas):
            return distribuidas[seleccion - 1]
        else:
            return salir()

def error_3tecla(): #Mensaje de error para cuando hay tres teclas válidas
    newtecla = input("Tecla inválida, favor presionar una tecla válida. [1] [2] [3]: ")
    
    if newtecla == "1":
        return distribuir()
        
    elif newtecla == "2":
        return reglas_juego()
        
    elif newtecla == "3":
        return salir()
        
    else:
        return error_3tecla()

# (1) Funciones secundarias del menú

def salir(): #Función simple que cierra el programa
    print("Gracias por jugar.")
    exit()

def reglas_juego(): #Función simple que printea las reglas del juego
    print()
    print("Tu objetivo se centra en la creación de áreas verdes y en el diálogo con personas asignadas.")
    print("Las áreas verdes son auto generadas al igual que las personas.\n")
    print("Reglas del juego: \n")
    print("1. Elige cuántas áreas verdes quieres crear.")
    print("2. Elige cuántas personas quieres asignar a las respectivas áreas.")
    print("3. Escoge una pregunta antes de hablar con alguien.\n")
    print("Controles del juego: \n")
    print("[x] Significa que x es una posible tecla a presionar en esa opción.")
    print("[ ] Significa que se puede presionar cualquier tecla para esa opción.")
    print()
    tecla = input("Ingresa cualquier tecla para volver al menú principal [ ] ")
    return menu_principal(name="")

# (2) Listas y funciones para las areas verdes

areas_verdes_uno = ["Parque ", "Reserva ", "Centro ", "Vivero ", "Parque Nacional ", "Potrero "]

largo_areas_uno = len(areas_verdes_uno)

areas_verdes_dos = ["Tárcoles", "Manuel Antonio", "Braulio Carrillo", "el Bosque", "Sarapiquí", "Prusia", "de la Hoja", "del Este", "Corcovado"]

largo_areas_dos = len(areas_verdes_dos)

def crear_areas_verdes():
    """
    Función que le pide al usuario la cantidad de areas verdes con
    las que desea trabajar y las genera tomando el tipo de area de
    la lista [areas_verdes_uno] y el nombre de [areas_verdes_dos] aleatoriamente.
    """
    print()
    areas = input("¿Cuántas áreas verdes desea crear? []\n")
    
    if validar_entero(areas) == False:
        return error_tipo_1()
        
    else:
        areas = int(areas)
        return crear_areas_verdes_aux(areas, [])

def crear_areas_verdes_aux(areas, res): #Fn auxiliar
    
    if areas == 0:
        return res
        
    else:
        a = random.randint(0, largo_areas_uno - 1)
        b = random.randint(0, largo_areas_dos - 1)
        nombre = areas_verdes_uno[a] + areas_verdes_dos[b]
        return crear_areas_verdes_aux(areas - 1, res + [nombre])

# (3) Listas y funciones para las personas

personas_uno = ["Juan ", "Luis ", "María ", "Aurelio ", "Valeria ", "Julián ", "Jimena "]

largo_personas_uno = len(personas_uno)

personas_dos = ["Álvarez ", "Matamoros ", "Sanabria ", "Castro ", "Naranjo ", "Guevara "]

personas_tres = ["Álvarez", "Matamoros", "Sanabria", "Castro", "Naranjo", "Guevara"]

largo_personas_dos = len(personas_dos)

def crear_personas():
    """
    Función que le pide al usuario la cantidad de personas que
    desea generar. La función crea a las personas tomando el primer
    nombre de la lista [personas_uno] y el primer apellido de la lista
    [personas_dos] y el tercero de la lista [personas_tres]. 
    Los 3 son de forma aleatoria.
    """
    personas = input("¿Cuántas personas quiere en su simulación? []\n")
    if validar_entero(personas) == False:
        return error_tipo_2()
        
    else:
        personas = int(personas)
        return crear_personas_aux(personas, [])

def crear_personas_aux(personas, res): #Fn auxiliar
    if personas == 0:
        return res
        
    else:
        c = random.randint(0, largo_personas_uno - 1)
        d = random.randint(0, largo_personas_dos - 1)
        e = random.randint(0, largo_personas_dos - 1)
        nombre = personas_uno[c] + personas_dos[d] + personas_tres[e]
        return crear_personas_aux(personas - 1, res + [nombre])

# (4) Asignación y distribución de personas en las areas verdes

def asignar(personas, num):
    """
    Función que le asigna a cada persona un numero que está entre 0 y len(areas)-1
    """
    return asignar_aux(personas, num, 0, len(personas))

def asignar_aux(personas, num, ind, fin): #Fn auxiliar
    
    if ind == fin:
        return personas
        
    else:
        personas[ind] = [personas[ind], random.randint(0, num - 1)]
        return asignar_aux(personas, num, ind + 1, fin)

def listas_vacias(num):
    """
    Función que crea una lista cuyos elementos son listas vacías y
    len(lista) = num
    E: Num, el largo de la lista
    S: Lista cuyos elementos son listas vacías
    R: Entrada debe ser un num entero (int)
    """
    if type(num) != int:
        return "Error"
        
    else:
        return listas_vacias_aux(num, 0, [])

def listas_vacias_aux(num, ind, res): #Fn auxiliar
    if ind == num:
        return res
        
    else:
        return listas_vacias_aux(num, ind + 1, res + [[]])

def distribuir():
    """
    Función que distribuye a las personas en las areas verdes disponible.
    """
    areas_verdes = crear_areas_verdes()
    print()
    print("Áreas verdes creadas:", areas_verdes)
    print()
    print(r"""      ccee88oo
  C8O8O8Q8PoOb o8oo
 dOB69QO8PdUOpugoO9bD
CgggbU8OU qOp qOdoUOdcb
    6OuU  /p u gcoUodpP
      \\\//  /douUP
        \\\////
         |||/\
         |||\/
         |||||
   .....//||||\....
""")
    personas = crear_personas()
    print()
    print("Personas creadas:", personas)
    print()
    print(r""" O     O     O
/|\   /|\   /|\
/ \   / \   / \
""")
    input("Presione cualquier botón para asignar las personas en las áreas verdes creadas. [] \n")

    personas = asignar(personas, len(areas_verdes))
    agrupado = agrupar_aux(personas, areas_verdes, 0, 0, len(personas), len(areas_verdes), listas_vacias(len(areas_verdes)))
    distribuidas = distribuir_aux(agrupado, areas_verdes, 0, len(agrupado))

    print("Distribución de personas en áreas verdes:", distribuidas)
    return seleccionar_area(distribuidas)

def agrupar_aux(personas, areas_verdes, i, j, fin_1, fin_2, res):
    """
    Funcion que solo llama distribuir, agrupa a las personas segun el
    numero que tienen despues de asignar( )
    """
    if j == fin_2:
        return res
        
    if i == fin_1:
        return agrupar_aux(personas, areas_verdes, 0, j + 1, fin_1, fin_2, res)
        
    elif personas[i][1] == j:
        res[j] = res[j] + [personas[i][0]]
        return agrupar_aux(personas, areas_verdes, i + 1, j, fin_1, fin_2, res)
        
    else:
        return agrupar_aux(personas, areas_verdes, i + 1, j, fin_1, fin_2, res)

def distribuir_aux(personas, areas_verdes, ind, fin):
    """
    Segunda función auxiliar de distribuir, despues de que agrupar_aux
    agrupe a las personas, esta función las asigna a un area verde disponible
    """
    if ind == fin:
        return personas
    else:
        personas[ind] = [areas_verdes[ind]] + [personas[ind]]
        return distribuir_aux(personas, areas_verdes, ind + 1, fin)

# (5) Interacción jugador-persona

respuestas = ["Siempre es bueno estar al aire libre.", "Ando paseando en mi día libre.", "Este lugar es hermoso, me encanta.",
                            "Me gusta despejar mi mente aquí despúes de un largo día.", "*Respira*, que bien se siente el aire fresco.", "Hace lindo día, ¿no?",
                            "Siempre solía venir aquí con mi pareja, pero me dejó.", "Ando paseando a mi perro, se llama Firulais",  
                            "La naturaleza es una esfera infinita cuyo centro está en todas partes y la circunferencia en ninguna.","Que corta que es la vida..."]

def dialogo(nombre, pregunta, respuestas):
    """
    Función que da una respuesta aleatora de la persona a la que se le preguntó.
    """
    respuesta = random.choice(respuestas)
    print()
    print(nombre, "dice:", respuesta)

def seleccionar_pregunta():
    """
    Función que permite hacer una pregunta. No tiene ningún
    efecto en la respuesta de la persona, es solo para personalizar.
    """
    print()
    pregunta = input ("Haz una pregunta: ")
    return pregunta

def seleccionar_persona(personas, indice, distribuidas):
    """
    Función que muestra las posibles personas a hablar y que permite seleccionar una.
    E: input
    S: persona que el jugador elige
    R: la entrada del input debe ser un entero en el rando establecido
    """
    if personas == []:
        print ("No hay personas en este área...")
        print ()
        tecla = input("Presione cualquier tecla para seleccionar otra area verde [ ]: " )
        print ()
        return seleccionar_area(distribuidas)
            
    elif indice == len(personas):
        print()
        seleccion = input("Selecciona una opción [ ]:")
        if validar_entero(seleccion) == False:
            return error_tipo_3(personas)
            
        else:
            seleccion = int(seleccion)
            return seleccionar_persona_aux(personas, seleccion)
            
    else:
        print("[" + str(indice+1) + "] " + personas[indice])
        return seleccionar_persona(personas, indice + 1, distribuidas)


def seleccionar_persona_aux(personas, ind): #Fn auxiliar
    
    if ind >= 1 and ind <= len(personas):
        return personas[ind - 1]
        
    else:
        return error_numero(personas)


def interactuar_con_personas_area(personas, distribuidas):
    """
    Funcion que permite que el jugador interactue con las personas
    llama a otras funciones para esto
    """
    persona = seleccionar_persona(personas,0,distribuidas)
    pregunta = seleccionar_pregunta()
    dialogo(persona, pregunta, respuestas)
    print()
    continuar = input("¿Deseas hablar con otra persona en esta área? [ ] Si [n] No: ")
    
    if continuar == "s":
        return interactuar_con_personas_area(personas, distribuidas)
        
    elif continuar == "n":
        return seleccionar_area(distribuidas)
        
    else:
        print("")
        return interactuar_con_personas_area(personas, distribuidas)

def seleccionar_area(distribuidas):
    """
    Función que muestra y permite interactuar con algun area verde.
    """
    print()
    print(r"""      ccee88oo
  C8O8O8Q8PoOb o8oo
 dOB69QO8PdUOpugoO9bD
CgggbU8OU qOp qOdoUOdcb
    6OuU  /p u gcoUodpP
      \\\//  /douUP
        \\\////
         |||/\
         |||\/
         |||||
   .....//||||\....
      O     O     O
     /|\   /|\   /|\
     / \   / \   / \
""")
    print()
    print("Presiona cualquier otra tecla para salir [-]")
    print("Selecciona un área verde para interactuar:")
    print()
    area = seleccionar_area_aux(distribuidas, 0)
    print()
    print("Personas en", area[0],":")
    print()
    interactuar_con_personas_area(area[1], distribuidas)

def seleccionar_area_aux(distribuidas, indice): #Fn auxiliar
    if indice == len(distribuidas):
        print()
        seleccion = input("Selecciona una opción [ ]: ")
        
        if validar_entero(seleccion) == False:
            return error_tipo_4(distribuidas)
            
        else:
            seleccion = int(seleccion)
            
            if 1 <= seleccion and seleccion <= len(distribuidas):
                return distribuidas[seleccion - 1]
            else:
                return error_tipo_4(distribuidas)
                
    else:
        print("[" + str(indice+1) + "] " + distribuidas[indice][0])
        return seleccionar_area_aux(distribuidas, indice + 1)

# (6) Menú principal y nombre del jugador

def menu_principal(name):  #Menu principal, de aquí, se conectan las demás funciones del juego.
    print()
    print("Bienvenid@", name, "al Comité de Gestión de Áreas Verdes\n")     
    print("[1] Iniciar proyecto de creación de áreas verdes\n")
    print("[2] Reglas y controles del juego\n")
    print("[3] Salir\n")
    tecla = input("Selecciona una opción [ ]\n")
    if tecla == "1":
        return distribuir()
        
    elif tecla == "2":
        return reglas_juego()
        
    elif tecla == "3":
        return salir()
        
    else:
        return error_3tecla()

def solicitar_nombre(): #Función que guarda el nombre de la persona
    print("Gracias por aplicar al comité de gestión de áreas verdes.")
    name = input("Por favor, escribe tu nombre para registrarte: ")
    print()
    print("Presiona cualquier otra tecla [ ] para salir\n")
    namechoice = input("¿Estás segur@ de tu nombre? [1] Sí [2] No \n")

    if namechoice == "1":
        return menu_principal(name)
        
    elif namechoice == "2":
        return solicitar_nombre()
        
    else:
        return salir()

name = solicitar_nombre() #Esto inicia el juego