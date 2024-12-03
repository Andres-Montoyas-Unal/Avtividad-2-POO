codigo=input("Ingrese el codigo del Empleado")
nombres=input("Ingrese el nombre del Empleado")
horas_trbajadas=input("Ingrese las horas trabajadas por el empleado")
valor_hora=input("Ingrese el valor de la hora")
porcentaje=input("Ingrese el porcentaje de retemcion en la fuente")

salario_bruto=horas_trbajadas*valor_hora
salario_neto=salario_bruto-(salario_bruto*(porcentaje/100))

print(f"Codigo={codigo}--Empleado={nombres}\nSu salario bruto es: {salario_bruto} y su salario neto es: {salario_neto}")
