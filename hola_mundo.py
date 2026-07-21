# mi_primer_script.py
print("hola, elige tus números deseados de ver")
numeros = list(range(int(input("Introduzca sus rango de números: "))))

print("Números elegidos por el usuario: ")
for n in numeros:
    print(n)

suma_total = sum(numeros)
print("\nsuma de los números elegidos: ", suma_total)
