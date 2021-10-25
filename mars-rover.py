
def move_one(init_pos,instruction):
    
    x_init = init_pos[0]
    y_init = init_pos[1]
    orient_init = init_pos[2]

    moveF_dict = {"N":[0,1],"E":[1,0],"S":[0,-1],"W":[-1,0]}
    moveR_dict = {"N":"E","E":"S","S":"W","W":"N"}
    moveL_dict = {"N":"W","W":"S","S":"E","E":"N"}

    if orient_init not in moveF_dict.keys():
        print("Position invalid, should be one of N, E, S, W")
        return

    if instruction == "F":
        orient = orient_init
        x = x_init + moveF_dict[orient][0]
        y = y_init + moveF_dict[orient][1]
    elif instruction == "R":
        x = x_init
        y = y_init
        orient = moveR_dict[orient_init]
    elif instruction == "L":
        x = x_init
        y = y_init
        orient = moveL_dict[orient_init]
    else:
        print("Instruction invalid, should be one of F, R, L")
        return
    
    return [x,y,orient]


def moving_robots(m,n,init_pos,instructions):

    for instruction in instructions:
        end_pos = move_one(init_pos,instruction)
        if end_pos is None:
            return
        elif end_pos[0] > m:
            end_pos[0] = m
            end_pos.append('LOST')
            break
        elif end_pos[1] > n:
            end_pos[0] = m
            end_pos.append('LOST')
            break
        elif end_pos[0] < 0:
            end_pos[0] = 0
            end_pos.append('LOST')
            break
        elif end_pos[1] < 0:
            end_pos[1] = 0
            end_pos.append('LOST')
            break
        else:
            init_pos = end_pos

    return end_pos

def convert_inputs(user_input):
    output_list = []
    for x in user_input.split():
        try:
            x = int(x)
        except ValueError:
            pass
        output_list.append(x)
    return output_list


input_1 = input("Input the grid size as two numbers separated by a space: ")
grid_size = convert_inputs(input_1)

input_2 = input("Input the first initial position as two numbers and a letter each separated by a space: ")
init_pos = convert_inputs(input_2)

input_3 = input("Input the instructions as a sequence of F, L, R: ")

output_1 = moving_robots(grid_size[0],grid_size[1],init_pos,input_3)
print(output_1)

input_4 = input("Input the second initial position as two numbers and a letter each separated by a space: ")
init_pos = convert_inputs(input_4)

input_5 = input("Input the instructions as a sequence of F, L, R: ")

output_2 = moving_robots(grid_size[0],grid_size[1],init_pos,input_5)
print(output_2)

