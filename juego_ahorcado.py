import unidecode
import getpass


def generar_palabra_secreta() -> str:
    """Función que pide al jugador 1 ingresar una palabra secreta.

    Returns:
        str: Palabra secreta ingresada por jugador 1.
    """
    while True:
        palabra_secreta_jugador_1 = getpass.getpass(
                f"Elige una palabra secreta:\n "
            )
        if palabra_secreta_jugador_1.isalpha():
            palabra_secreta = unidecode.unidecode(
                        palabra_secreta_jugador_1.lower()
                    )
            return palabra_secreta
        else:
            print(
                        f"Caracteres no válidos. Ingrese una palabra con caracteres"
                        " alfabéticos:\n"
                    )


def palabra_secreta_espacios_blanco(palabra: str) -> list:
    """Devuelve una lista con tantos espacios en blanco como letras tiene la
    palabra.

    Args:
        palabra (str): Palabra secreta ingresada por el jugador 1 

    Returns:
        list: Lista de espacios en blanco de la
            palabra.
    """
    lista_espacios_blanco = []
    for _ in range(len(palabra)):
        lista_espacios_blanco += "_"  # lista con tantos espacios en blanco
        # como elementos tiene la palabra
    return lista_espacios_blanco

def jugar_ahorcado():
    """ Función que imprime por pantalla si el jugador 2 ha sido el ganador o
    perdedor de la partida.
    """
    palabra_secreta_2 = generar_palabra_secreta()
    lista = palabra_secreta_espacios_blanco(palabra_secreta_2)
    string_espacios_blanco = " ".join(str(elem) for elem in lista)
    print(
        "La palabra secreta tiene tantas letras como espacios en blanco:",
        string_espacios_blanco,
    )
    vidas = 7  
    contador_errores = 0  
    letras_correctas = []
    final_del_juego = False
    while not final_del_juego:  # mientras el juego no finalice
        letra_ingresada = input("Ingrese una letra: ")

        for posicion in range(len(palabra_secreta_2)):
            letra = palabra_secreta_2[posicion]
            if letra == letra_ingresada:
                lista[posicion] = letra

        if (
            (letra_ingresada not in palabra_secreta_2)
            or (letra_ingresada in letras_correctas)
            or (len(letra_ingresada) > 1)
        ):
            # por el jugador 1 o ya ha sido usada
            vidas -= 1  # hemos gastado una vida
            contador_errores += 1  # aumentamos el contador de errores
            # imprimir por pantalla número de errores cometidos no de vidas
            # restantes.
            print(
                f"La letra elegida no es la correcta o ya ha sido repetida."
                f" Le quedan {vidas} vidas."
            )
            print(f"Ha cometido {contador_errores} errores.")
        else:
            letras_correctas.append(letra_ingresada)

        print(" ".join(str(elemento) for elemento in lista))

        if vidas == 0:  # si gastamos todos los intentos
            final_del_juego = True  # finalizamos el juego
            print(
                f"Lo siento jugador 2, ha perdido la partida. El jugador 1 ha"
                f" ganado. Mejor suerte para la próxima. \n"
                f"La palabra secreta era {palabra_secreta_2} "
            )

        # si no hay espacios en blanco en la lista entonces significa que he
        #  ganado (ie, he acertado todas las letras)
        if "_" not in lista:  # si no hay elementos vacíos en la lista
            final_del_juego = True  # finalizamos el juego en el momento
            # que acertamos todas las letras, ie, cuando todos los espacios
            # en blanco han sido rellenados.
            print(f"Jugador 2: Ha sido el ganador de la partida ¡Enhorabuena!")

AFIRMACION = "si"
def llamar_ahorcado():
    print(f"Bienvenido al juego del ahorcado. ¡¡Buena suerte!!\n")
    decision = AFIRMACION
    while decision == AFIRMACION:
        jugar_ahorcado()
        decision = input(
            "Si quiere continuar jugando escriba 'si', si desea salir del" 
            "juego pulse otra tecla."
             
        )

llamar_ahorcado()
