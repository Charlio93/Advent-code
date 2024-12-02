
#Comprobar si la lista aumenta(1) o disminuye(2)
def check_order_list( ld_anterior, ld_int_valor ):

    if ld_int_valor > ld_anterior:
        ld_aumento = 1
    else:
        ld_aumento = 2
    
    return ld_aumento

def check_errors(numeros):
    
    ld_anterior = 0 
    error = False
    ld_aumento = 0
    
    for valor in numeros: 
       ld_int_valor = int(valor)

       #Revisar si los valores crecen o decrecen
       if ld_anterior != 0 and ld_aumento == 0:
           ld_aumento = check_order_list( ld_anterior, ld_int_valor )
              
       #Mirar que realmente estemos aumentando o disminuyendo y que no se supere en 3 el aumento/disminución
       if ld_aumento != 0: 
           if abs(ld_int_valor - ld_anterior) > 3 or ( ld_int_valor == ld_anterior and ld_anterior != 0 ): 
                error = True
                return error
           else:
              match ld_aumento:
                case 1: 
                    if ld_int_valor < ld_anterior: 
                        return True
                case 2:
                    if ld_int_valor > ld_anterior:
                        return True
                    
       ld_anterior = ld_int_valor 
    
    return error
    
ld_informes_ok = 0
ld_informes_semiok = 0

with open("data/dia2_lista2.txt", "r") as fichero: 
    for linea in fichero:
        numeros = linea.split()
        #Primera comprobación con todos los valoresa
        error = check_errors(numeros)
        if not (error):
           ld_informes_ok += 1
           ld_informes_semiok += 1
        else:
           #Segunda llamada para ver los semi_ok, obviando cualquier numero que pueda generar error
           for ind, valor in enumerate(numeros):
               numeros_aux = numeros.copy()
               del numeros_aux[ind]
               error = check_errors(numeros_aux)
               if not (error):
                  ld_informes_semiok += 1
                  break
    
    print( 'Informes correctos:', ld_informes_ok )
    print( 'Informes semi correctos:', ld_informes_semiok )
               