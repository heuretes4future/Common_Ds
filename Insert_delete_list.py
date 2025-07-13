import random 


def insertion(insertnumber, prim_list, positionnumber):
    front_pos = 3
    current_pos = 2
    working_number = prim_list.index(positionnumber)
    prim_list.append(prim_list[-1])

    for index in range(len(prim_list[working_number:])):
        if prim_list[-index-1] == positionnumber:
            prim_list[-index-current_pos] = insertnumber
            return prim_list
        prim_list[-index-current_pos] = prim_list[-index-front_pos]
    return 0

def deletion(prim_list,position):
    working_number = prim_list.index(position)
    removed_index = prim_list.pop(prim_list[working_number])
    for index in prim_list[removed_index:]:
        prim_list[index] = prim_list[index+1]
    


def main():
    list_size = random.randint(5, 20) 
    prim_list = [random.randint(1, 100) for _ in range(list_size)]
    print(f"Randomized list: {prim_list}")

    while True:
        user_input = input("Choose a number to insert > ")
        position_input = input("Which position to insert > ")
        deletion = input("Remove a number >")
        try:
            user_input = int(user_input)
            position_input = int(position_input)

            new_list = insertion(user_input, prim_list, position_input)
            deleted_list = deletion(new_list, deletion)
            print(f"New list: {deleted_list} (new item inserted at position {position_input})")

        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()