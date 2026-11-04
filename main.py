#!/usr/bin/env python3
"""Módulo para importar la lista y la selecion de la parabra."""

from utils import get_random_word


words= get_random_word(filename="wordlist.txt")
print(words)
print(len(words))

