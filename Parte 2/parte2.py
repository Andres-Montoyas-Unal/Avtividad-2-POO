import math as mt
class figuras():
    def __init__(self):
        pass
    def CalcularPerimetro():
        pass
    def CalcularArea():
        pass

class TrianguloRectangulo(figuras):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcularHipotenusa(self):
        return ((self.base)**2 + (self.altura)**2)**0.5
    def calcularArea(self):
        return (self.base*self.altura)/2
    def calcularPerimetro(self,hipotenusa):
        return self.base+self.altura+hipotenusa
    def determinarTipoTriangulo(self,hipotenusa):
        if self.base==self.altura and self.base==hipotenusa:
            print("Es un triángulo equilatero")
        elif self.base!=self.altura and self.base!=hipotenusa:
            print("Es un triángulo escaleno")
        else: print("Es un triángulo isoceles")
class Circulo(figuras):
    def __init__(self,radio):
        self.radio=radio
    def calcularArea(self):
        return mt.pi*self.radio**2
    def calcularPerimetro(self):
        return 2*mt.pi*self.radio
    

class Cuadrado(figuras):
    def __init__(self,lado):
        self.lado=lado
    def calcularArea(self):
        return self.lado*self.lado
    def calcularPerimetro(self):
        return 4*self.lado

class Rectangulo(figuras):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return self.base*self.altura
    def calcularPerimetro(self):
        return (2*self.base)+(2*self.altura)

figura1= Circulo(2)
figura2= Rectangulo(1,2)
figura3=Cuadrado(3)
figura4= TrianguloRectangulo(3,5)

print(f"El área del ciculo es {figura1.calcularArea()} y su perimetro es {figura1.calcularPerimetro()}/n")
print(f"El área del Rectángulo es {figura2.calcularArea()} y su perimetro es {figura2.calcularPerimetro()}/n")
print(f"El área del Cuadrado es {figura3.calcularArea()} y su perimetro es {figura3.calcularPerimetro()}/n")
print(f"El área del Triángulo es {figura4.calcularArea()} y su perimetro es {figura4.calcularPerimetro(figura4.calcularHipotenusa())}")
figura4.determinarTipoTriangulo(figura4.calcularHipotenusa())