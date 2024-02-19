# 3) Faça um programa em C, que demonstra a prova de que o produto de dois
# pares, resulta em um número par.
a = 1
b = 1

while(a % 2 != 0):
    a = int(input("Digite o primeiro número par (a): "))
while(b % 2 != 0):
    b = int(input("Digite o segundo número par (b): "))


print("Vamos demonstrar matematicamente que o produto de dois números pares é par:")
print(f"1. Temos dois números pares: a = {a} e b = {b}")
print(" onde a e b podem ser escritos como: a = 2m e b = 2n.")

m = a // 2
n = b // 2

print(f"2. Assim, temos que a = 2 * {m} e b = 2 * {n}.")
print("3. a * b = (2m) * (2n)= 4mn")
produto = 4 * m * n
print(f"4. 4 * {m} * {n} = {produto}")
print(f"5. O produto de {a} e {b} é {a} * {b} = 4 * {m} * {n} = {produto}.")
print("6. Conclusão: O produto de dois números pares é par.")
