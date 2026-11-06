#!/usr/bin/env python3
"""Módulo principal que inicia y controla una partida de Ahorcado."""

# Importamos la función que selecciona una película aleatoria.
from utils import get_random_word

# Importamos la clase que contiene la lógica del juego.
from game import HangmanGame


# Seleccionamos una película aleatoriamente desde el archivo wordlist.txt.
word = get_random_word(filename="wordlist.txt")

# Creamos una instancia de la clase HangmanGame.
# La película seleccionada será la palabra que debe adivinar el jugador.
game = HangmanGame(word)

# Mostramos el progreso inicial de la película oculta.
game.display_progress()
game.display_guessed_letters()
game.display_attempts()

# Bucle: continúa mientras la partida no termine.
while True:

    # Solicitamos una letra y la convvertimos a minúscula.
    letter = input("Ingresa una letra: ").lower()

    # Comprobamos que el jugador haya ingresado un solo carácter.
    if len(letter) != 1:
        print("Debes ingresar una sola letra.")
        continue

    # Comprobamos que el carácter ingresado sea una letra.
    if not letter.isalpha():
        print("Debes ingresar una letra.")
        continue

    # Evitamos que el jugador ingrese una letra que ya utilizó.
    if letter in game.guessed_letters:
        print("Ya ingresaste esa letra.")
        continue

    # Procesamos la letra y actualizamos el estado de la partida.
    result = game.process_guess(letter)

    # Informamos si la letra está presente en la película.
    if result:
        print("¡Correcto!")
    else:
        print("Letra incorrecta.")

    # Mostramos las letras descubiertas y las que permanecen ocultas.
    game.display_progress()

    # Mostramos las letras ingresadas.
    game.display_guessed_letters()

    # Mostramos los intentos restantes.
    game.display_attempts()

    # Comprobamos si el jugador descubrió todas las letras.
    if game.is_won():
        print("¡Ganaste!")
        break

    # Comprobamos si el jugador agotó todos sus intentos.
    if game.is_lost():
        print("¡Perdiste!")
        print("La película era:", word)
        break
