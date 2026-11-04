#!/usr/bin/env python3
"""Módulo para importar la lista y la selecion de la parabra."""

from utils import get_random_word
from game import HangmanGame


word = get_random_word(filename="wordlist.txt")
print(word)
print(len(word))

game = HangmanGame(word)
game.display_progress()
print(game)