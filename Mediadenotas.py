num_notas = 0
while True:
    try:
        num_notas = int(input("Quantas notas você quer digitar? "))
        if num_notas > 0:
            break
        else:
            print("Por favor, não tenta me enganar com um numero inferior a 0.")
    except ValueError:
        print("Por favor, coloque numeros.")

soma_notas = 0

for i in range(num_notas):
    while True:
        try:
            nota = float(input(f"Coloca a {i+1}ª nota (entre 0 e 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Por favor, não tenta me enganar,você não tirou inferior a 0 ou superior a 10 numa escola onde o minimo é 0 e o maximo é 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um NUMERO.")
    soma_notas += nota


if num_notas > 0:
    media = soma_notas / num_notas
else:
    media = 0


print(f"\nA média final é: {media:.2f}")


if media >= 7:
    print("Situação: APROVADO, nos vemos ano que vem😒")
else:
    print("Situação: REPROVADO, nos vemos em dezembro 😊")
