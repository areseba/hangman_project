#!/usr/bin/env python3
"""Módulo para importar la lista y la selecion de la parabra."""

from utils import get_random_word
from game import HangmanGame


# Selecciona una película aleatoriamente.
word = get_random_word(filename="wordlist.txt")

# Crea una instancia del juego.
game = HangmanGame(word)
game.display_progress()

# Solicita y valida la letra ingresada por el jugador.
while True:
    letter = input("Ingresa una letra: ")

    if len(letter) != 1:
        print("Debes ingresar una sola letra.")
        continue
    if not letter.isalpha():
        print("Debes ingresar una letra.")
        continue
    if letter in game.guessed_letters:
        print("Ya ingresaste esa letra.")
        continue
    game.guessed_letters.append(letter)
    break