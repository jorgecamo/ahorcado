import random

"""
# Este programa es una ahorcado de toda la vida con 6 intentos de poner una letra mal.
"""


def DimeLetra(LetrasActuaales):
    """
    Este metodo sirve para comprobar si la letra que has puesto sirve para gastar un intento.
    Tambien puedes terminar el programa ponendo terminar.
    :param LetrasActuaales: **String de las letras que estan.**
    :return: Char Letra de intento
    """
    while True:
        print('Adivina una letra.')
        adivina = input('> ').upper()
        if adivina == 'TERMINAR':
            adivina = "1"
            return adivina
        elif len(adivina) != 1:
            print('Introduce una única letra.')
        elif adivina in LetrasActuaales:
            print('Esa letra ya la sabías. Elige otra vez.')
        elif not adivina.isalpha():
            print('Introduce una LETRA.')

        else:
            return adivina


def Intentos(intentos):
    """
    Este metodo sirve para descontar intentos
    :param intentos: Int intentos actuales
    :return: Int Intentos restantes
    """
    intentos -= 1
    return intentos


class JuegoAhorcado:
    """
    *En esta clase se crea la estructura del ahoracado y tambien estan definidas las categorias y las palabras
    disponibles para jugar.*
    """
    Estados = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    Salvado = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    Categoria = 'FRUTAS FUTBOLISTAS COCHES'.split()
    Frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
             'MANDARINA ' \
             'NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    Coches = 'LAMBO BMW MERCEDES TESLA'.split()
    Futbolistas = 'MESSI CRISTIANO NEYMAR KANTE'.split()

    def jugar(self):
        """
        En este metodo es cuando empieza el juego, y se ejecuta un bucle hasta que se el resultado correcto,
        o se gasten todos los intentos.
        :return: Resultado
        """
        LetrasIncorrectas = []
        LetrasCorrectas = []
        NumIntentos = 6
        nombre = input("Como te llamas?")
        cat = random.choice(self.Categoria)
        if cat == 'FRUTAS':
            secreto = random.choice(self.Frutas)
        elif cat == 'COCHES':
            secreto = random.choice(self.Coches)
        else:
            secreto = random.choice(self.Futbolistas)

        while True:
            self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto, NumIntentos, cat)
            Letra = DimeLetra(LetrasIncorrectas + LetrasCorrectas)

            if Letra in secreto:
                LetrasCorrectas.append(Letra)

                Resultado = True
                for LetrasSecreto in secreto:
                    if LetrasSecreto not in LetrasCorrectas:
                        Resultado = False
                        break
                if Resultado:
                    print(self.Salvado[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado! ' + nombre)
                    break

            else:
                LetrasIncorrectas.append(Letra)
                NumIntentos = Intentos(NumIntentos)
                if Letra == "1":
                    print(self.Estados[6])
                    print('La palabra era "{}"'.format(secreto))
                    break
                if len(LetrasIncorrectas) == len(self.Estados) - 1:
                    self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto, NumIntentos, cat)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, LetrasIncorrectas, LetrasCorrectas, secreto, NumIntentos, cat):
        """

        :param LetrasIncorrectas: Lista con las letras incorrectas que llevas.
        :param LetrasCorrectas: Lista con las letras correctas que llevas.
        :param secreto: String secreta.
        :param NumIntentos: Int de los intentos que llevas.
        :param cat: String de la categoria actual
        :return: Te muestra un dibujo actual de como vas y de los tintentoss que tienes, y las letras incorrectas
        y correctas.
        """
        print(self.Estados[len(LetrasIncorrectas)])
        print('La categoría es: ', cat)
        print()
        print("Te quedan :" + str(NumIntentos) + " intentos.")
        print('Letras incorrectas: ', end='')
        for LetraIncorrecta in LetrasIncorrectas:
            print(LetraIncorrecta, end=' ')
        if len(LetrasIncorrectas) == 0 and 0 == len(LetrasIncorrectas):
            print('No hay letras incorrectas.')
        print()

        EspaciosEnBlanco = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in LetrasCorrectas:
                EspaciosEnBlanco[i] = secreto[i]

        print(' '.join(EspaciosEnBlanco))


if __name__ == '__main__':
    juego1 = JuegoAhorcado()
    juego1.jugar()
