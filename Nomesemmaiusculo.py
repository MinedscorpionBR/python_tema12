nomes = []

for i in range(5):
    nome = input(f"Bota o {i+1}º nome: ")
    nomes.append(nome)

print("\nNomes em letra maiúsculas:")

for nome in nomes:
    print(nome.upper())
