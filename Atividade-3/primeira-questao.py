# Para esta tarefa, desenvolva a solução de cada pergunta utilizando código(python
# ou c).
# 1) Suponha que A, B e C representam condições que serão verdadeiras e falsas
# quando um programa é executado. Suponha ainda que desejamos que este
# programa realize alguma tarefa somente quando A ou B forem verdadeiras (mas
# não ambas) e C for falsa.
# a) Usando A, B e C e os conectivos E, OU e NOT, escreva uma sentença que
# será verdadeira apenas nestas condições.

def condicao_a():
    print("Condição A")
    print("A".ljust(8, " ") + "B".ljust(8, " ") + "C".ljust(8, " ") + "Saída")
    valores = [(True, True, True), (True, False, True), (False, True, True), (True, False, False)]
    for A, B, C in valores:
        saida = (not C) and ((A and not B) or (not A and B))
        print(str(A).ljust(8, " ") + str(B).ljust(8, " ") + str(C).ljust(8, " ") + str(saida))

condicao_a()
print("#" * 40, end="\n\n")


# b) Usando A, B e C e os conectivos E, OU e NOT, escreva uma sentença que
# será falsa apenas nestas condições.

def condicao_b():
    print("Condição B")
    print("A".ljust(8, " ") + "B".ljust(8, " ") + "C".ljust(8, " ") + "Saída")
    valores = [(True, True, True), (True, False, True), (False, True, True), (True, False, False)]
    for A, B, C in valores:
        saida = not((not C) and ((A and not B) or (not A and B)))
        print(str(A).ljust(8, " ") + str(B).ljust(8, " ") + str(C).ljust(8, " ") + str(saida))

condicao_b()
print("#" * 40, end="\n\n")

