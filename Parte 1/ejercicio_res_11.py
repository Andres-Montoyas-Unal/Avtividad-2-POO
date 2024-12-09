n1=int(input("Ingrese el valor de n1: "))
n2=int(input("Ingrese el valor de n2: "))
n3=int(input("Ingrese el valor de n3: "))
if n1>n2 and n1>n3:
  mayor=n1
elif n2>n3:
  mayor=n2
else:mayor=n3
print(f"El valor mayor entre {n1}, {n2} y {n3} es: {mayor}")
