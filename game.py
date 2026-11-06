#!/usr/bin/env python3
"""Módulo que contiene la lógica y las reglas del juego Ahorcado."""


def normalize_letter(letter):
    """Normalizamos las vocales acentuadas para facilitar las comparaciones.
    Convierte las vocales acentuadas en vocales sin tilde.
    Pasamos como argumento:
        letter (es un string): Letra que se desea normalizar.
    Retornamos:
        string: Letra normalizada.
    """
    return letter.translate(
        str.maketrans("áéíóú", "aeiou")
    )


class HangmanGame:
    """Gestionamods el estado y el funcionamiento de una partida de Ahorcado."""

    def __init__(self, word):
        """Inicializamos una nueva partida.
        Pasamos como argumento:
            word (string): Película que debe adivinar el jugador.
        """
        # Guardamos la película en minúsculas.
        self.word = word.lower()

        # Almacenamos las letras adivinadas correctamente.
        self.guessed_letters = []

        # Almacenamos todas las letras ingresadas.
        self.attempted_letters = []

        # Definimos la cantidad máxima de errores permitidos.
        self.max_errors = 6

        # Inicializamos el contador de errores.
        self.errors = 0

    def display_progress(self):
        """Mostramos las letras adivinadas y ocultamos las restantes.
        Las iniciales de cada palabra las mostramos en mayúsculas
        cuando son descubiertas.
        """
        progress = ""

        # Recorremos el título obteniendo la posición y cada carácter.
        for posicion, letter in enumerate(self.word):

            # Normalizamos la letra para comparar sin tildes.
            normalized = normalize_letter(letter)

            # Conservamos los espacios entre las palabras.
            if letter == " ":
                progress += " "

            # Comprobamos si es la primera letra de una palabra.
            elif posicion == 0 or self.word[posicion - 1] == " ":

                # Mostramos la inicial en mayúscula si fue adivinada.
                if normalized in self.guessed_letters:
                    progress += letter.upper()
                else:
                    progress += "_"

            # Mostramos las demás letras si fueron adivinadas.
            elif normalized in self.guessed_letters:
                progress += letter

            # Ocultamos las letras que todavía no fueron adivinadas.
            else:
                progress += "_"

        # Imprimimos el progreso actual de la película.
        print(progress)

    def process_guess(self, letter):
        """Procesamos una letra y actualizamos el estado de la partida.
        Pasamos como argumento:
            letter (es un string): Letra ingresada por el jugador.
        Retornamos:
            booleano: True si la letra está en la película; False en caso contrario.
        """
        # Normalizamos la letra ingresada.
        normalized_letter = normalize_letter(letter)

        # Normalizamos el título completo para comparar sin tildes.
        normalized_word = normalize_letter(self.word)

        # Guardamos todas las letras ingresadas por el jugador.
        self.attempted_letters.append(normalized_letter)

        # Comprobamos si la letra aparece en el título.
        if normalized_letter in normalized_word:

            # Guardamos la letra correcta.
            self.guessed_letters.append(normalized_letter)

            return True

        else:
            # Incrementamos el contador cuando la letra es incorrecta.
            self.errors += 1

            return False

    def is_lost(self):
        """Comprobamos si el jugador agotó sus intentos.
        Retornamos:
            booleano: True si alcanzó el máximo de errores; False en caso contrario.
        """
        return self.errors == self.max_errors

    def is_won(self):
        """Comprobamos si el jugador descubrió todas las letras del título.
        Retornamos:
            booleano: True si todas las letras fueron descubiertas; False si falta alguna.
        """
        # Recorremos todos los caracteres del título.
        for letter in self.word:

            # Ignoramos espacios y otros caracteres que no sean letras.
            if (letter.isalpha() and normalize_letter(letter) not in self.guessed_letters):
                return False

        # Si no quedan letras pendientes, el jugador ganó la partida.
        return True

    def display_guessed_letters(self):
        """Muostramos todas las letras ingresadas por el jugador."""
        print("Letras ingresadas:", ", ".join(self.attempted_letters))

    def display_attempts(self):
        """Mostramos la cantidad de intentos restantes."""
        attempts_left = self.max_errors - self.errors
        print("Intentos restantes:", attempts_left)
