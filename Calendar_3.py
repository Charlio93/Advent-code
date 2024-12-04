#En una cadena de texto llena de simbolos raros tendre que responder con la suma de los productos
#de los fragmentos de cadena que respeten el siguiente formato "mul(n1,n2)"
import re

def clear_conditions(conditions_list):
    clear_list = []
    enable_append = True
    for fragment in conditions_list:
        if fragment == "do()":
            enable_append = True
        elif fragment == "don't()":
            enable_append = False
        
        if enable_append:
            clear_list.append(fragment)
        
    return clear_list

def get_conditions(linea):
    pattern = r"(do\(\)|don't\(\))"
    conditions = re.split(pattern,linea)
    return [condition for condition in conditions if condition]

def extract_data(linea):
    pattern = r"mul+\(\d+,\d+\)"
    matches = re.findall(pattern, linea)
    return matches

def calculate_value(valores):
    str_replaced = valores.replace("mul", "").strip("()")
    numbers = str_replaced.split(",")
    return int(numbers[0]) * int(numbers[1])

with open("data/dia3_lista2.txt", "r") as fichero: 
    conditions_list =[]
    clear_list = []
    for linea in fichero:
       conditions = get_conditions(linea)
       conditions_list.extend(conditions)
    
    clear_list = clear_conditions(conditions_list)
    
    data_list = []
    for linea in clear_list: 
       matches = extract_data(linea)
       data_list.extend(matches)
    
    final_resul = 0
    for valores in data_list:
       value = calculate_value(valores)
       final_resul += value
    
    print(final_resul)