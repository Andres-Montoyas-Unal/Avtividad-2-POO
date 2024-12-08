pa=int(input("Ingrese el peso de la esfera A: "))
pb=int(input("Ingrese el peso de la esfera B: "))
pc=int(input("Ingrese el peso de la esfera C: "))
pd=int(input("Ingrese el peso de la esfera D: "))
if pa==pb and pa==pc:
  print("La esfera D es la diferente y ")
  if pd>pa:
    print("es de mayor peso")
  else: print("es de menor peso")
elif pa==pb and pa==pd:
  print("La esfera C es la diferente y ")
  if pc>pa:
    print("es de mayor peso")
  else: print("es de menor peso")
elif pa==pc and pa==pd:
  print("La esfera B es la diferente y ")
  if pb>pa: 
    print("es de mayor peso")
  else: print("es de menor peso")
else:
  print("La esfera A es la diferente y ")
  if pa>pb: print("es de mayor peso")
  else: print("es de menor peso")
