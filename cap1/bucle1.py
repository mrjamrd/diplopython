###Bucle

contador = 0

for contador in range(0,10):
    print(f"El contador va: {contador}")


##///////////////////////////////////////////////////////////

numero_user = int(input("Digite un numero: "))
if numero_user < 1:
    numero_user = 1
contador = 0

for contador in range(1,11):
    if numero_user == 45:
        print("Prohibido este numero...")
        break

    print(f"{numero_user} X {contador} = {numero_user * contador}")
