num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("Ta achando que eu sou idiota,é?")
else:
    while num >= 0:
        print(num)
        num -= 1
    print("Lançamento! Fim da contagem!... oh meu Deus acho que eu esqueci de por um prego no foguete...")
