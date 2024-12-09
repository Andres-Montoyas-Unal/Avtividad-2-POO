class departamento():
    def __init__(self, ventas, salario):
        self.ventas=ventas
        self.salario=salario
    def calcular_salario(self,porcentaje_ventas):
        if self.ventas>porcentaje_ventas:
            self.salario=salario+salario*0.2

ventas1=int(input("Ingrese las ventas de departamento 1: "))
ventas2=int(input("Ingrese las ventas de departamento 2: "))
ventas3=int(input("Ingrese las ventas de departamento 3: "))
salario=int(input("Ingrese el salario de los vendedores: "))
ventas_total=ventas1+ventas2+ventas3
porven=0.33*ventas_total
departamento1=departamento(ventas1,salario)
departamento2=departamento(ventas2,salario)
departamento3=departamento(ventas3,salario)
departamento1.calcular_salario(porven)
departamento2.calcular_salario(porven)
departamento3.calcular_salario(porven)
print(f"Salario vendedores Depto. 1 {departamento1.salario}, salario Depto.2 {departamento2.salario}, salario Depto.3 {departamento3.salario}")