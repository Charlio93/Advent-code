def search_rules(numero, rules_list):
    valores = []
    aplicable_rules = []
    for rules in rules_list:
        valores = rules.split("|")
        for valor in valores:
            if valor == numero:
                aplicable_rules.append(rules)
    
    return aplicable_rules

def check_if_correct(numero, rules, list_updates):
    rules_check_before = []
    rules_check_after = []
    
    for rule in rules:
        if rule.startswith(f"{numero}"):
            rules_check_before.append(rule[3:5]) #Me quedarér con los numeros que no pueden estar antes del NUMERO
        else:
            rules_check_after.append(rule[:2]) #Me quedaré con los numeros que no pueden estar despues del NUMERO 

    x_number = 0
    for x in range(len(list_updates)):
        if list_updates[x] == numero:
            x_number = x 
            break
    
    
    #Buscamos las de despues
    for i in range(x_number, len(list_updates), +1): 
        if list_updates[i] in rules_check_after and numero != list_updates[i]:
            return False
    
    for i in range(x_number, -1, -1): 
        if list_updates[i] in rules_check_before and numero != list_updates[i]:
            return False
    
    return True

def reparadortresmil(numero, rules, list_updates):
    rules_check_before = []
    rules_check_after = []
    
    for rule in rules:
        if rule.startswith(f"{numero}"):
            rules_check_before.append(rule[3:5]) #Me quedarér con los numeros que no pueden estar antes del NUMERO
        else:
            rules_check_after.append(rule[:2]) #Me quedaré con los numeros que no pueden estar despues del NUMERO 

    x_number = 0
    for x in range(len(list_updates)):
        if list_updates[x] == numero:
            x_number = x 
            break
    
    #Buscamos las de despues
    for i in range(x_number, len(list_updates), +1): 
        if list_updates[i] in rules_check_after and numero != list_updates[i]:
            list_updates[x_number], list_updates[i] = list_updates[i], list_updates[x_number]
            return True, list_updates
    
    for i in range(x_number, -1, -1): 
        if list_updates[i] in rules_check_before and numero != list_updates[i]:
           list_updates[i], list_updates[x_number] = list_updates[x_number], list_updates[i]
           return True, list_updates 
    
    return False, list_updates

updates_list = []
rules_list = []
lf_next_list = False
with open("data/dia5_lista1.txt", "r") as fichero:
    for linea in fichero:
        if linea.strip() == "":
            lf_next_list = True
            continue
        if lf_next_list:
            updates_list.append(linea.strip())
        else:
            rules_list.append(linea.strip())

aplicable_rules = []
correct_updates = []
error_updates = []
for update in updates_list:
    numeros = update.split(",")
    correct_update = True
    rules = []
    for numero in numeros:
        rules = search_rules(numero, rules_list)
        correct_update = check_if_correct(numero, rules, numeros)
        if not correct_update:
            error_updates.append(numeros)
            break
    
    if correct_update:
       correct_updates.append(numeros) 
    else:
        continue

for update in error_updates:
    lf_exit = True
    while lf_exit:         
        if lf_exit:
            lf_reparado = False
            for numero in update:
               rules = search_rules(numero, rules_list)
               lf_reparado, update = reparadortresmil(numero, rules, update) 
               if lf_reparado:
                  break
              
        correct_update = True   
        for numero in update:
           rules = search_rules(numero, rules_list)
           correct_update = check_if_correct(numero, rules, update)
        if correct_update:
            lf_exit = False
               
valor = 0
for correct_update in correct_updates:
    valor += int(correct_update[len(correct_update)//2])
print("Correctos",valor)

print(error_updates)
valor = 0
for error_update in error_updates:
    valor += int(error_update[len(error_update)//2])
print("Arreglados",valor)