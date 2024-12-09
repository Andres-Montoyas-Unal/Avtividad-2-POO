nombre=input("Ingrese el nombre del empleado: ")
salario=float(input("Ingrese el salario básico por hora: "))
num_horas=int(input("Ingrese el número de horas trabjadas: "))
total=salario*num_horas
print(f"Empleado= {nombre}")
if total>450000: print(f"Tuvo un sueldo de ${total}")
  
