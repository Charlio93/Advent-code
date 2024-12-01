#Dos grupos de historiadores han ido añadiendo una serie de IDs de ubicaciones
#Tengo que comparar las listas de los dos grupos de historiadores ordenados de menor a mayor
#Luego acumulo la distancia entre los valores y los sumo para dar un resultado final

hist_1 = [] #3,4,2,1,3,3
hist_2 = [] #4,3,5,3,9,3
total_diff = 0
total_simi = 0

with open("dia1_lista1.txt", "r") as fichero: 
    for linea in fichero:
        val1, val2 = linea.split()
        hist_1.append(int(val1))
        hist_2.append(int(val2))
        
hist_1.sort()
hist_2.sort()

for a,b in zip(hist_1, hist_2):
    total_diff = total_diff + abs( a - b )
    
print('total diff', total_diff)


#Para la segunda parte he de mirar cuantas veces se repiten los valores de la columna izquierda en la derecha y multiplicar ese valor por el 
#número de veces que aparece 
for val1 in hist_1:
    counter = 0
    for val2 in hist_2:
        if val1 == val2:
            counter = counter + 1

    total_simi = total_simi + ( val1 * counter)
    
print('Total simi', total_simi)





