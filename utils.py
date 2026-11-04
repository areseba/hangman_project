#!/usr/bin/env python3
"""Módulo para leer e imprimir un archivo de texto."""
import random


def load_words(filename):
    """Carga las peliculas desde un archivo de texto."""
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words.append(line.strip())
        return words


def get_random_word(filename):
    """Elijo una pelicula al azar desde un archivo de texto."""
    movies = load_words(filename)
    movie = random.choice(movies)
    return movie
