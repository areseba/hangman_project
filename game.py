#!/usr/bin/env python3
"""Módulo que contiene la lógica del juego."""


class HangmanGame:
    """Gestiona el estado de una partida del ahorcado."""
    def __init__(self, word):
        """Inicializa los atributos de una nueva partida."""
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra las letras adivinadas y oculta las restantes."""
        progress = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                progress += letter
            elif letter == " ":
                progress +=  " "
            else:
                progress += "_"
        print(progress)
