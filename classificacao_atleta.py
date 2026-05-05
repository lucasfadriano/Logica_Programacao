idade = int (input("Digite sua idade: "))
if idade >=5 and idade <=10:
    print("Categoria infantil")
elif idade >=11 and idade <=17:
    print("Categoria juventil")
elif idade >=18:
    print("Categoria Adulto")
else:
    print("Muito jovem para competir!")