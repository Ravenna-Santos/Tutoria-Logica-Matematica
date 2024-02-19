# Dados os valores-verdade A verdadeiro, B falso e C verdadeiro, qual o
# valor-verdade de cada uma das seguintes sentenças?
# a. A ^(B v C)
# b. (A ^ B) v C
# c. (A ^ B)’ v C
# d. A’ v ( B’ ^ C)’
# e. A v ( B v C)’

A = True
B = False
C = True

print("A ^(B v C)")
print(A and (B or C))
print("#" * 10, end="\n\n")

print("(A ^ B) v C")
print((A and B) or C)
print("#" * 10, end="\n\n")

print("(A ^ B)’ v C")
print((not (A and B)) or C)
print("#" * 10, end="\n\n")

print("A’ v ( B’ ^ C)’")
print((not A) or ((not B) and (not C)))
print("#" * 10, end="\n\n")

print("A v ( B v C)’")
print(A or (not (B or C)))
print("#" * 10, end="\n\n")