import math 

def insertion(insertnumber, prim_list):

    if insertnumber in prim_list:
        next_pos = 0
        working_position = prim_list.index(insertnumber)
        for current_position in prim_list[:working_position]:
            next_pos +=1
            prim_list.append(prim_list[-1-next_pos])
        prim_list.insert(working_position,insertnumber)

    [prim_list[len(prim_list) - position].append(prim_list[len(prim_list)]) for position in range(len(prim_list)) if prim_list[position] == insertnumber]
    return insertnumber

def deletion(deletenumber, prim_list):

    return deletenumber


def main():
    prim_list = [math.random(i) for i in range(math.random)]
    print(f"Randomized list: {prim_list}")
    input("Chose by typing either insert, delete" )
    while True:
        UserInput = input("input the number you want to manipulate > ")
        if UserInput.isdigit and UserInput in UserInput:
            UserInput = int(UserInput)
            try:
                removed = deletion(UserInput, prim_list)
                inserted = insertion(UserInput,prim_list)
                input(f"value that has been manipulated: {removed}")
            except ValueError:
                print("Add a valid number")

        else:
         print("Enter a valid number that exist in the list")


