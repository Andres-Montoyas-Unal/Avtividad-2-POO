nombre=input("Ingrese el nombre del trabajador: ")
num_horas=int(input("Ingrese el numero de horas trabajadas: "))
valor_hora=float(input("Ingrese el valor por hora trabajada: "))
if num_horas>40:
  horas_extras=num_horas-40
  if horas_extras>8:
    horas_excedentes=horas_extras-8
    pago_horas_extras=valor_hora*2*8+valor_hora*3*horas_excedentes
  else: pago_horas_extras=valor_hora*2*horas_extras
  salario= valor_hora*40+pago_horas_extras
else: salario=valor_hora*num_horas
print(f"El trabajador {nombre} devengo: ${salario}")
