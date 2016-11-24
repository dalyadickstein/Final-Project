from move import move_list

if __name__ == "__main__":
    validElement = False
    while not validElement:
        print("Choose your main element: Fire, Water, Earth, or Wind: ", end="")
        elementChoice = raw_input()
        element = elementChoice.lower()
        if (
            element == "fire" || 
            element == "water" || 
            element == "earth" ||
            element == "wind"
        ):
            validElement = True
    print("An excellent choice.\nYou will be able to choose three different \
        moves. Type (move).info to read about a move.\nPick your first move:")
    print_movelist(element)


    



