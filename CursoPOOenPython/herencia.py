class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado) #Se debe volver a inicializar  la clase superior y esto se hace con la función super() Si uno cambia una función de la clase sperior, se convierte en         polimorfismo       


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())