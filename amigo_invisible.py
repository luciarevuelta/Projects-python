import random
import unidecode
from random import randint
from typing import List


def conseguir_participantes() -> List[str]:
    """Función que genera una lista de
    participantes del sorteo.

    Returns:
        List: lista de nombres personales no
        duplicados.
    """
    participantes = []
    while True:
        nombre = input(
            f" Ingrese el nombre de los participantes."
            f" Pulse intro para finalizar:\n "
        )
        if nombre == "":
            if len(participantes) < 3:
                print(" Ingrese más de 2 participantes.\n")
            else:
                break
        elif nombre.isalpha(): 
            nombre_alfabetico = unidecode.unidecode(nombre.lower())
            if nombre_alfabetico in participantes:
                print(
                    f" Ese nombre ya fue ingresado anteriormente. "
                    f" Ingrese un nombre distinto.\n"
                )
            else:
                participantes.append(nombre_alfabetico)
        else:  
            print(
                f" ¡Escriba un nombre que tenga caracteres únicamente"
                f" alfabéticos!\n"
            )
    return participantes  # lista de participantes no duplicados


def generar_reciben(n: int) -> list:
    """Función que genera una lista aleatoria de índices.

    Args:
        n (int): Valor entero que será la longitud de la lista de los
        participantes.

    Returns:
        list: Lista aleatoria de índices.
    """
    lista_indices_aleatoria = [] 
    for i in range(n):
        j = random.randint(0, n - 1)
        while j == i or j in lista_indices_aleatoria:
            j = random.randint(0, n - 1)
        lista_indices_aleatoria.append(j)
        #Solo falta un valor por genera (i == n-2)
        #Y el que me falta por genera es el de la última posición (n-1) not in lista_indices_aleatoria
        if i == n-2 and (n-1) not in lista_indices_aleatoria:
            return generar_reciben(n)
    return lista_indices_aleatoria


def amigo_invisible():
    """ Devuelve las posibles combinaciones entre los que compran y reciben
    el regalo.
    """
    print(f" ¡¡Bienvenidos al sorteo del amigo invisible !!  \n")
    compran = conseguir_participantes()
    compran = [mayus.capitalize() for mayus in compran]
    indices_que_reciben = generar_reciben(len(compran))
    reciben = [compran[i] for i in indices_que_reciben]  
    print("EL RESULTADO DEL SORTEO ES EL SIGUIENTE: \n")
    for comprador, recibidor in zip(compran, reciben):
        print(f"{comprador} le regala a {recibidor}.\n")

AFIRMACION = "si"

def llamar_amigo_invisible():
    print(f"Bienvenido al juego del amigo invisible. ¡¡Buena suerte!!\n")
    decision = AFIRMACION
    while decision == AFIRMACION:
        amigo_invisible()
        decision = input(
            "Si quiere continuar jugando escriba 'si', si desea salir del" 
            "juego pulse otra tecla."
             
        )
