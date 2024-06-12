#Probabilidad y estadistica
## facilitador: Jose Gabriel Rodriguez Rivas
## Alumno:Victor Seturino

from statistics import *;
# tiempos de corredores 100 metros

tiempos = [15.10,17.20,14.69,13.27,22.15,18.71,19.15,20.65,15.10,17.20];

print(f"los tiempos son:{tiempos}");

print("El tiempo promedio de los correros es de ", mean(tiempos));

mediana = median(tiempos);
print("la media de los tiempos de los corredores es ", mediana );

# muestra los numeros ordenados de forma ascendente
print(sorted(tiempos));

print(reversed(tiempos)); #muestra los numeros en reversa

modas = multimode(tiempos);
print("las modas de los tiempos es ", modas);

moda = mode(tiempos);
print("la moda de los tiempos es ", moda);

