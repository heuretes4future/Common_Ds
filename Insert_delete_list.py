import math 


def insertion(insertnumber):
    return insertnumber

def deletion(deletenumber):
    return deletenumber


def main():
    prim_list = [math.random(i) for i in range(math.random)]
    print(f"Randomized list: {prim_list}")
    while True:
        UserInput = input("try deleting an element in the list >")
        if UserInput.isdigit and UserInput in UserInput:
            UserInput = int(UserInput)
            try:
                removed = deletion(UserInput)
                print(f"value that has been removed: {removed}")
                break
            except ValueError:
                print("Add a valid number")

        else:
         print("Enter a valid number that exist in the list")


