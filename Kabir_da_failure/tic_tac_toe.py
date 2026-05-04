import random
human_numbers = {10}
computer_numbers = {10}
game_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6 
seven = 7
eight = 8
nine = 9
print(f"""Here is a tic-tac-toe board:

          
      |     |     
   {one}  |  {two}  |  {three}  
 _____|_____|_____
      |     |     
   {four}  |  {five}  |  {six} 
 _____|_____|_____
      |     |     
   {seven}  |  {eight}  |  {nine}  
      |     |     """)
while True:
    human_move = int(input("Where would you like to place your piece pick a number 1-9: "))
    if human_move == ValueError:
        print("put a proper number please")
    
    elif human_move in game_numbers:
        print("Valid number")
        game_numbers.remove(human_move)
        human_numbers.add(human_move)
        if 1 in human_numbers:
            one = "X"
        if 2 in human_numbers:
            two = "X"
        if 3 in human_numbers:
            three = "X"
        if 4 in human_numbers:
            four = "X"
        if 5 in human_numbers:
            five = "X"
        if 6 in human_numbers:
            six = "X"
        if 7 in human_numbers:
            seven = "X"
        if 8 in human_numbers:
            eight = "X"
        if 9 in human_numbers:
            nine = "X"
        if 1 in computer_numbers:
            one = "O"
        if 2 in computer_numbers:
            two = "O"
        if 3 in computer_numbers:
            three = "O"
        if 4 in computer_numbers:
            four = "O"
        if 5 in computer_numbers:
            five = "O"
        if 6 in computer_numbers:
            six = "O"
        if 7 in computer_numbers:
            seven = "O"
        if 8 in computer_numbers:
            eight = "O"
        if 9 in computer_numbers:
            nine = "O"
        print(f"""Here is a tic-tac-toe board:

          
      |     |     
   {one}  |  {two}  |  {three}  
 _____|_____|_____
      |     |     
   {four}  |  {five}  |  {six} 
 _____|_____|_____
      |     |     
   {seven}  |  {eight}  |  {nine}  
      |     |     """)
    
    target_numbers1 = {1, 2, 3}

    present = target_numbers1.intersection(human_numbers)

    missing = target_numbers - check_set

    if len(present) == 2:
    computer_numbers.add(missing)
    game_numbers.remove(missing)
    computer_move = (list(missing))
    

    print(f"The missing number(s) are: {list(missing)}")

        computer_move = random.choice(list(game_numbers))
        game_numbers.remove(computer_move)
        computer_numbers.add(computer_move)
        print("Computer played " + str(computer_move))
        if 10 in computer_numbers:
            if 1 in human_numbers:
                one = "X"
            if 2 in human_numbers:
                two = "X"
            if 3 in human_numbers:
                three = "X"
            if 4 in human_numbers:
                four = "X"
            if 5 in human_numbers:
                five = "X"
            if 6 in human_numbers:
                six = "X"
            if 7 in human_numbers:
                seven = "X"
            if 8 in human_numbers:
                eight = "X"
            if 9 in human_numbers:
                nine = "X"
            if 1 in computer_numbers:
                one = "O"
            if 2 in computer_numbers:
                two = "O"
            if 3 in computer_numbers:
                three = "O"
            if 4 in computer_numbers:
                four = "O"
            if 5 in computer_numbers:
                five = "O"
            if 6 in computer_numbers:
                six = "O"
            if 7 in computer_numbers:
                seven = "O"
            if 8 in computer_numbers:
                eight = "O"
            if 9 in computer_numbers:
                nine = "O"
            print(f"""Here is a tic-tac-toe board:

            
        |     |     
    {one}  |  {two}  |  {three}  
    _____|_____|_____
        |     |     
    {four}  |  {five}  |  {six} 
    _____|_____|_____
        |     |     
    {seven}  |  {eight}  |  {nine}  
        |     |     """)
            
        print(computer_numbers)
        print(str(human_numbers))
        print(str(game_numbers))
        