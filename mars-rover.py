
# -------------- Functions --------------- #

def move_one(init_pos,instruction):
    """Calculate the updated the position of a robot based on an initial position and one instruction.

    :param init_pos: initial position in the form [x, y, orientation]
    :type init_pos: list of int, int, str
    :param instruction: movement command, either F, R or L
    :type instruction: str
    :return: updated position after movement completed
    :rtype: list of int, int, str
    """
    
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
    """Calculate the movement of a robot across a grid based on an initial position and a set of instructions.
    If robot moves off the grid the last valid position is recorded and the robot is marked as lost.

    :param m: size of grid in the x-direction
    :type m: int
    :param n: size of grid in the y-direction
    :type n: int
    :param init_pos: initial position of robot in the form [x, y, orientation]
    :type init_pos: list of int, int, str
    :param instructions: sequence of movement commands (combination of F,L,R)
    :type instructions: str
    :return: end position 
    :rtype: list of int, int, str
    """

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
    """Convert a user input to a valid list of int and str.

    :param user_input: user input
    :type user_input: str
    :return: valid list of int and str
    :rtype: list
    """
    output_list = []
    for x in user_input.split():
        try:
            x = int(x)
        except ValueError:
            pass
        output_list.append(x)
    return output_list

# ---------------- Deploy functions -------- #

# When the script is run the user is prompted for a set of inputs to complete the Mars Rover calculations.

input_grid = input("Input the grid size as two numbers separated by a space: ")
grid_size = convert_inputs(input_grid)

i = 1

while i < 10:
    user_input_pos = input("Input the initial position as two numbers and a letter each separated by a space: ")
    input_pos = convert_inputs(user_input_pos)
    
    input_instructions = input("Input the instructions as a sequence of F, L, R (e.g. FFRLF): ")
    
    output = moving_robots(grid_size[0],grid_size[1],input_pos,input_instructions)
    print(output)

    inputs_open = input("To enter another input press return, to end press x + return: ")
    if inputs_open =="x":
        break

    i += 1

