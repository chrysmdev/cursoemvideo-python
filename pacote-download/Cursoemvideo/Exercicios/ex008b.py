# DESAFIO 008 extra
# Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, m, dm, cm e mm.

m = float(input('Escolha um valor em metros para ser convertido: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'{m} metros é equivalente a: \n {km}km \n {hm}hm \n {dam}dam \n {dm}dm \n {cm}cm \n {mm}mm')