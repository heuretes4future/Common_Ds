import random 

def insertion(insertnumber, prim_list):
    #an easy insert type function
    if insertnumber in prim_list:
        next_pos = 0
        working_position = prim_list.index(insertnumber)
        for _ in prim_list:
            curr = prim_list[-1-next_pos]
            if curr == insertnumber:
                prim_list[working_position] = insertnumber
                return insertnumber
            prim_list.append(curr)
            next_pos +=1

#def deletion(deletenumber, prim_list):

#    return deletenumber


def main():
    list_size = random.randint(1, 100) 
    prim_list = [random.randint(1, 100) for _ in range(list_size)]
    print(f"Randomized list: {prim_list}")
    while True:
        UserInput = input("which position do you want to insert in > ")
        if UserInput.isdigit():
            UserInput = int(UserInput)
            try:
           #     removed = deletion(UserInput, prim_list)
                inserted = insertion(UserInput,prim_list)
           #     input(f"value that has been manipulated: {removed}")
            except ValueError:
                print("Add a valid number")

        else:
         print("Enter a valid number that exist in the list")


if __name__ == "__main__":
    main()