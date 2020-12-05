# exprecao for item in list
dobra_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobra_dos_pares)


# vesao "normal"
dobra_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobra_dos_pares.append(i*2)

print(dobra_dos_pares)