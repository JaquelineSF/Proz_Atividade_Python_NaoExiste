def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        opcao = input("Digite o número para a operação correspondente: ")
        
        if opcao == "0":
            print("Encerrando a calculadora.")
            break
        
        if opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe.")
            continue
        
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        
        if opcao == "1":
            print("Resultado:", soma(num1, num2))
        elif opcao == "2":
            print("Resultado:", subtracao(num1, num2))
        elif opcao == "3":
            print("Resultado:", multiplicacao(num1, num2))
        elif opcao == "4":
            print("Resultado:", divisao(num1, num2))

calculadora()

