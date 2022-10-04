import random


def preguntar_rondas_partidas() -> (int, int):
    """Pregunta al usuario el número de rondas y partidas que quiere jugar.
    Returns:
        int: Devuelve el número de partidas que va a jugar el
        usuario.

        int: Devuelve el número de rondas que va a jugar el
        usuario.
    """
    partidas, rondas = None, None
    try:
        partidas = int(input("¿Cuántas partidas quiere jugar?: "))
    except ValueError:
        print(f"El valor debe ser entero")
    try:
        rondas = int(input(f"¿Y cuántas rondas quiere que tenga cada juego?:"))
    except ValueError:
        print(f"El valor debe ser entero")
    return partidas, rondas


PIEDRA = "r"
PAPEL = "p"
TIJERA = "t"


def ha_ganado(jugador: str, oponente: str) -> bool:
    """Devuelve un booleano. True si el jugador gana al oponente y falso en
     caso contrario.

    Args:
        jugador (str): el jugador ingresa piedra, papel o tijera.
        oponente (str): el oponente ingresa piedra, papel o tijera.

    Returns:
        bool: True si el jugador gana al oponente, False si pierde contra el
        oponente.
    """

    # condiciones para ganar una jugada: r > t, t > p, p > r
    if (
        (jugador == PIEDRA and oponente == TIJERA)
        or (jugador == TIJERA and oponente == PIEDRA)
        or (jugador == PAPEL and oponente == PIEDRA)
    ):
        return True  
    return False  

GANA = 1
EMPATA = 0
PIERDE = -1

def juego() -> (int, str, str):
    """ Me devuelve quien gana, pierde o empatada en una tirada.  
    Returns:
        int: devuelve un entero ya sea 0, 1 o -1.
        str: devuelve lo que ha elegido el usuario (r, p o t).
        str: devuelve lo que ha elegido la computadora (r, p o t).
    """

    while True:
        usuario = input(
            f" ¿Cuál es tu elección? 'r' para piedra, 'p' "
            "para papel, 't' para tijera\n"
        )
        if usuario != PIEDRA and usuario != TIJERA and usuario != PAPEL:
            print(
                f" La opción elegida no es válida. Inténtelo de nuevo y esta"
                "vez ingrese los caracteres válidos "
            )
        else:
            computadora = random.choice([PIEDRA, PAPEL, TIJERA])
            if usuario == computadora:
                return (EMPATA, usuario, computadora)

            if ha_ganado(usuario, computadora):
                # si el usuario gana a la computadora (llamado a la función
                # creada abajo)
                return (GANA, usuario, computadora)

            return (
                PIERDE,
                usuario,
                computadora,
            )  # los casos que no son ni ganancia
            # ni empate son pérdidas para el usuario


def jugar_al_mejor_de(n: int) -> int:
    """Función que nos permite jugar al mejor de n rondas.

    Args:
        n (int): Número de rondas que jugamos

    Returns:
        int: 1 si el jugador ha ganado n rondas, -1 si la computadora ha 
        ganado n rondas, 0 si la computadora ha empatado n rondas.
    """
    print(f"------ Nuevo juego -------")
    jugador_gana = 0
    ordenador_gana = 0  
    jugadas_necesarias = n / 2
    for _ in range(n):
        resultado, usuario, computadora = juego()
        # EMPATAS
        if resultado == EMPATA:
            print(
                f" Usted y la computadora han elegido {usuario}. "
                "Ha empatado. \n"
            )
        # GANAS
        elif resultado == GANA:
            jugador_gana += 1  # incrementa el número de veces que ha ganado
            # el jugador
            print(
                f" Ha elegido {usuario} y la computadora ha elegido"
                f" {computadora}. Usted gana!\n"
            )
        # PIERDES
        else:
            ordenador_gana += 1  # incrementa el número de veces que ha perdido
            # el jugador
            print(
                f" Ha elegido {usuario} y la computadora ha elegido"
                f" {computadora}. Usted pierde. \n "
            )

        if (jugador_gana > jugadas_necesarias) or (
            ordenador_gana > jugadas_necesarias
        ):
            break

    if jugador_gana > ordenador_gana:
        print(f" ¡Usted ha ganado un juego de {n} rondas!\n")
        return GANA
    elif jugador_gana < ordenador_gana:
        print(f" ¡La computadora ha ganado un juego de {n} rondas!\n")
        return PIERDE
    else:
        print(f" Usted ha empatado un juego de {n} rondas!\n")
        return EMPATA


def mejor_m_partidas():
    """Jugar al mejor de m partidas

    Args:
        m (int): Número de partidas que vamos a jugar
    """
    jugador_gana_partida = 0
    ordenador_gana_partida = 0
    partidas, rondas = preguntar_rondas_partidas()
    partidas_necesarias = partidas/2
    if partidas and rondas:
        for _ in range(partidas):
            resultado = jugar_al_mejor_de(rondas)

            if resultado == GANA:
                jugador_gana_partida += 1

            elif resultado == PIERDE:
                ordenador_gana_partida += 1

            if (jugador_gana_partida > partidas_necesarias) or (
            ordenador_gana_partida > partidas_necesarias
            ):
                break

        if jugador_gana_partida > ordenador_gana_partida:
            print(f" ¡Usted ha ganado al mejor de {partidas} partidas!\n")
        elif jugador_gana_partida < ordenador_gana_partida:
            print(
                f" ¡La computadora ha ganado al mejor de {partidas} partidas!"
                f"\n"
            )
        else:
            print(
                f" Usted ha empatado el juego contra la computadora al mejor\n"
                f" de {partidas} partidas."
            )
    else:
        print("Ha introducido caracteres inválidos")

AFIRMACION = "si"
def llamar_piedra_papel_tijera():
    
    print(f"Bienvenido al juego de piedra, papel o tijera ¡¡Buena suerte!!\n")
    decision = AFIRMACION
    while decision == AFIRMACION:
        mejor_m_partidas()
        decision = input(
        "Si quiere continuar jugando escriba 'si', si desea salir del juego"
        " pulse otra tecla. "
        )
