valor_compra=float(input("Ingrese el valor total de la compra: "))
bolita=input("Ingrese el color de la bolita: ")
bolita.upper()
if bolita=="BLANCA":
  descuento=0
elif bolita=="VERDE":
  descuento=10
elif bolita=="AMARILLA":
  descuento=25
elif bolita=="AZUL":
  descuento=50
else: descuento=100
valor_pagar=valor_compra-valor_compra*descuento/100
print(f"El ciente debe pagar: ${valor_pagar}")
