ni=int(input("Ingrese el número de inscripción: "))
nom=input("Ingrese el nombre: ")
pat=float(input("Ingrese el patrimonio: "))
est=int(input("Ingrese el estrato: "))
pagmat=50000
if (pat>2000000)and(est>3):
  pagmat+=0.03*pat
print(f"El estudiante con número de inscripción {ni} y nombre {nombre} debe pagar {pagmat}")
