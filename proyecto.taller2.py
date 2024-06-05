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