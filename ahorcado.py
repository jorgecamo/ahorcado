import random


def DimeLetra(LetrasActuaales):
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
    intentos -= 1
    return intentos


class JuegoAhorcado:
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

    Categoria = 'FRUTAS'
    PalabraJuego = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
                   'MANDARINA ' \
                   'NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):

        LetrasIncorrectas = []
        LetrasCorrectas = []
        NumIntentos = 6
        nombre = input("Como te llamas?")
        secreto = random.choice(self.PalabraJuego)

        while True:
            self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto, NumIntentos)
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
                    self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto, NumIntentos)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, LetrasIncorrectas, LetrasCorrectas, secreto, NumIntentos):
        print(self.Estados[len(LetrasIncorrectas)])
        print('La categoría es: ', self.Categoria)
        print()
        print("Te quedan :" + str(NumIntentos) + " intentos.")
        print('Letras incorrectas: ', end='')
        for LetraIncorrecta in LetrasIncorrectas:
            print(LetraIncorrecta, end=' ')
        if len(LetrasIncorrectas) == 0 and 0 == len(LetrasIncorrectas):
            print('No hay letras incorrectas.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 1:
            print('Letras diferentes.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 2:
            print('No coinciden.')

        print()

        EspaciosEnBlanco = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in LetrasCorrectas:
                EspaciosEnBlanco[i] = secreto[i]

        print(' '.join(EspaciosEnBlanco))


if __name__ == '__main__':
    juego1 = JuegoAhorcado()
    juego1.jugar()
