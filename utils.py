#!/usr/bin/env python3
"""Módulo para cargar películas desde un archivo de texto y elegir una al azar."""

import random


def load_words(filename):
    """Carga las películas almacenadas en un archivo de texto.
    Abre el archivo indicado, lee todas sus líneas y elimina los
    espacios y saltos de línea sobrantes.
    Pasamos como argumento:
        filename (es un string): Nombre del archivo que contiene las películas.
    Retornamos:
        list: Lista de películas disponibles.
    """
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words.append(line.strip())
        return words


def get_random_word(filename):
    """Selecciona una película aleatoria de la lista.
    Pasamos como argumento:
        filename (es un string): Nombre del archivo de películas.
    Retornamos:
        string: Título de la película seleccionada.
    """
    movies = load_words(filename)
    movie = random.choice(movies)
    return movie
