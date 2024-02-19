# 2) Faça um programa em C ou python , que demonstre que se o quadrado de
# um número é ímpar, então o número também é ímpar.


numero = 0

while(numero % 2 == 0):
    numero = int(input("Digite um número ímpar: "))
print(f"Vamos demonstrar que o quadrado de um número ímpar é ímpar:")
print(f"1. Temos o número ímpar {numero}.")
print(f"2. Todo número ímpar pode ser representado da seguinte forma: 2 * k + 1")
print("3. Logo, o quadrado de um número ímpar pode ser dado por: (2k + 1)^2 ")
k = (numero - 1) // 2
print(f"4. Calculamos o valor de k: k = ({numero} - 1) // 2 = {k}")
print(f"5. Expandindo o quadrado da fórmula do passo 3, temos: 4 * K^2+ 4 * k + 1")
quadrado = 4 * k** 2 + 4 * k + 1
print(f"6. Calculando 4 * {k}^2 + 4 * {k} + 1 temos que o quadrado de {numero} é: {quadrado}")
print(f"7. Conclusão: O quadrado de {numero} é ({2 * k + 1})^2 = 4 * {k}^2 + 4 * {k} + 1 = {quadrado}, que é ímpar.")