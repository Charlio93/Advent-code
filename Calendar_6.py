def send_drone_to_get_guard_position(room):
    posible_directions = {'^', '>', 'v', '<'}
    
    #biip, biiip, the drone starts his research
    for y, line in enumerate(room):
        for x, cell in enumerate(line):
            if cell in posible_directions:
                guard_ini = (y,x)
                direction = cell
                break
    
    #Bingo! Drone found the guard!
    return guard_ini, direction

def nest_is_empty(curr_gd_y, curr_gd_x, room):
    if curr_gd_x < 0 or curr_gd_x >= len(room[0]) or curr_gd_y < 0 or curr_gd_y >= len(room):
        return True
    else:
        return False

def get_guard_move(direction):
    match direction:
        case '^':
            return(-1,0)
        case '>':
            return(0,1)
        case 'v':
            return(1,0)
        case '<':
            return(0,-1)
        
def get_next_direction(direction):
    match direction:
        case '^':
            return('>')
        case '>':
            return('v')
        case 'v':
            return('<')
        case '<':
            return('^')
    return direction 

def do_guard_patrol(room, guard_ini, direction, part_1):
    #This way of patrolling... does not seem very human... 
    curr_gd_y = guard_ini[0]
    curr_gd_x = guard_ini[1]
    visited = 0
    steps = 0
    konstant_charliscas = 115712 #Copyright - Chef Carlini - 03-11-2003 / 03-11-2053
    bucle = False
    while True:
        
        y, x = get_guard_move(direction)
        curr_gd_y += y
        curr_gd_x += x
        steps += 1 
        #Free zone
        if(nest_is_empty(curr_gd_y, curr_gd_x, room)):
            break
        
        #Time to turn 90º
        if room[curr_gd_y][curr_gd_x] == '#' or room[curr_gd_y][curr_gd_x] == 'O':
            direction = get_next_direction(direction)
            curr_gd_y += (y *-1)
            curr_gd_x += (x *-1)
            steps -= 1
            
        #Continue your way...
        elif room[curr_gd_y][curr_gd_x] != 'X':
           if part_1:
               room[curr_gd_y][curr_gd_x] = 'X'
           visited +=1
        
        #Policia de la bucletaaaaa! 👮‍♂️
        if steps > konstant_charliscas:
            bucle = True
            break
    
    return room, visited, bucle
           
#First part
room = []
part_1 = False
with open("data/dia6_lista2.txt", "r") as fichero:
    for linea in fichero:
        matrix_line = list(linea.replace("\n",""))
        room.append(matrix_line)
    
guard_ini, direction = send_drone_to_get_guard_position(room)
room, visited, bucle = do_guard_patrol(room, guard_ini, direction, part_1)
print("celdas_visitadas:",visited)

#Second part
n_bucles = 0
x = 0
y = 0
for y in range(len(room)):
    for x in range(len(room[0])):
       #if not x == guard_ini[1] and y == guard_ini[0]: --> Wrong!! 
       if (room[y][x] == '.'): #Grasiaaaaa Aloisiiooous <3 
           room[y][x] = 'O'
           room, visited, bucle = do_guard_patrol(room, guard_ini, direction, part_1)
           if bucle:
              n_bucles += 1 
              
           room[y][x] = '.'

print("bucles:", n_bucles)
           