"""Cuarta tarea de APA 2026: Generación de números aleatorios.

Alumno: Pau Pont Camp

Este módulo implementa un generador lineal congruente de números
pseudoaleatorios mediante una clase iterable, Aleat, y una función
generadora, aleat.
"""


class Aleat:
    """Generador lineal congruente iterable.

    La clase genera números pseudoaleatorios mediante la fórmula:

        x = (a * x + c) % m

    Atributos:
        m: módulo del generador.
        a: multiplicador.
        c: incremento.
        x: estado actual de la secuencia.

    Métodos:
        __next__(): devuelve el siguiente número de la secuencia.
        __iter__(): devuelve el propio iterador.
        __call__(x0): reinicia la secuencia con la semilla indicada.

    Comprobación del funcionamiento de Aleat:

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    Comprobación del reinicio de Aleat:

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(
        self,
        *,
        m=2**48,
        a=25214903917,
        c=11,
        x0=1212121,
    ):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """Generador lineal congruente.

    Genera números pseudoaleatorios mediante la fórmula:

        x = (a * x + c) % m

    Args:
        m: módulo del generador.
        a: multiplicador.
        c: incremento.
        x0: semilla inicial.

    Yields:
        El siguiente número pseudoaleatorio de la secuencia.

    Si se envía un valor con send(), la secuencia se reinicia usando
    ese valor como nueva semilla.

    Comprobación del funcionamiento de aleat():

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    Comprobación del reinicio de aleat():

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """

    x = x0

    while True:
        x = (a * x + c) % m
        nueva_semilla = yield x

        if nueva_semilla is not None:
            x = nueva_semilla


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
