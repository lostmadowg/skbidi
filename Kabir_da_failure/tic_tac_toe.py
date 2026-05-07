from colorama import Fore, Back, Style, init
import random
import time
init(autoreset=True)
while True:
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
    while True:
        gamemode = input("What level would you like to play? (medium or hard): ").lower()
        if gamemode != "medium" and gamemode != "hard":
            print("Invalid gamemode")
            continue
        elif gamemode == "medium" or gamemode == "hard":
            break
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
        time.sleep(1)
        try:
            human_move = int(input("Where would you like to place your piece pick a number 1-9: "))
            valid = human_move >= 1 and human_move <= 9
            if valid == False:
                print("put a number 1-9 please")
                continue
        except ValueError:
            print("put a proper number please")
            continue
        if human_move not in game_numbers:
            print("That spot is taken")
            continue

        if human_move in game_numbers:
            game_numbers.remove(human_move)
            human_numbers.add(human_move)
            if 1 in human_numbers:
                one = Fore.RED + "X" + Style.RESET_ALL
            if 2 in human_numbers:
                two = Fore.RED + "X" + Style.RESET_ALL
            if 3 in human_numbers:
                three = Fore.RED + "X" + Style.RESET_ALL
            if 4 in human_numbers:
                four = Fore.RED + "X" + Style.RESET_ALL
            if 5 in human_numbers:
                five = Fore.RED + "X" + Style.RESET_ALL
            if 6 in human_numbers:
                six = Fore.RED + "X" + Style.RESET_ALL
            if 7 in human_numbers:
                seven = Fore.RED + "X" + Style.RESET_ALL
            if 8 in human_numbers:
                eight = Fore.RED + "X" + Style.RESET_ALL
            if 9 in human_numbers:
                nine = Fore.RED + "X" + Style.RESET_ALL
            if 1 in computer_numbers:
                one = Fore.BLUE + "O" + Style.RESET_ALL
            if 2 in computer_numbers:
                two = Fore.BLUE + "O" + Style.RESET_ALL
            if 3 in computer_numbers:
                three = Fore.BLUE + "O" + Style.RESET_ALL
            if 4 in computer_numbers:
                four = Fore.BLUE + "O" + Style.RESET_ALL
            if 5 in computer_numbers:
                five = Fore.BLUE + "O" + Style.RESET_ALL
            if 6 in computer_numbers:
                six = Fore.BLUE + "O" + Style.RESET_ALL
            if 7 in computer_numbers:
                seven = Fore.BLUE + "O" + Style.RESET_ALL
            if 8 in computer_numbers:
                eight = Fore.BLUE + "O" + Style.RESET_ALL
            if 9 in computer_numbers:
                nine = Fore.BLUE + "O" + Style.RESET_ALL
            time.sleep(1)
            print(f"""Here is the tic-tac-toe board now:

            
         |     |     
      {one}  |  {two}  |  {three}  
    _____|_____|_____
         |     |     
      {four}  |  {five}  |  {six} 
    _____|_____|_____
         |     |     
      {seven}  |  {eight}  |  {nine}  
         |     |     """)
        if 1 in human_numbers and 2 in human_numbers and 3 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 4 in human_numbers and 5 in human_numbers and 6 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 7 in human_numbers and 8 in human_numbers and 9 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 1 in human_numbers and 4 in human_numbers and 7 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 2 in human_numbers and 5 in human_numbers and 8 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 3 in human_numbers and 6 in human_numbers and 9 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 1 in human_numbers and 5 in human_numbers and 9 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 3 in human_numbers and 5 in human_numbers and 7 in human_numbers:
            print("Congratulations, you win!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif len(game_numbers) == 0:
            print("It's a tie!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        time.sleep(0.5)
        print(Fore.CYAN + "Computer is thinking...")
        time.sleep(1)
        
        target_numbers1 = {1, 2, 3}

        present1 = target_numbers1.intersection(human_numbers)

        missing1 = target_numbers1 - human_numbers

        amissing1 = target_numbers1 - human_numbers

        target_numbers2 = {4, 5, 6}

        present2 = target_numbers2.intersection(human_numbers)

        missing2 = target_numbers2 - human_numbers

        amissing2 = target_numbers2 - human_numbers

        target_numbers3 = {7, 8, 9}

        present3 = target_numbers3.intersection(human_numbers)

        missing3 = target_numbers3 - human_numbers

        amissing3 = target_numbers3 - human_numbers

        target_numbers4 = {1, 4, 7}

        present4 = target_numbers4.intersection(human_numbers)

        missing4 = target_numbers4 - human_numbers

        amissing4 = target_numbers4 - human_numbers

        target_numbers5 = {2, 5, 8}

        present5 = target_numbers5.intersection(human_numbers)

        missing5 = target_numbers5 - human_numbers

        amissing5 = target_numbers5 - human_numbers
        
        target_numbers6 = {3, 6, 9}

        present6 = target_numbers6.intersection(human_numbers)

        missing6 = target_numbers6 - human_numbers

        amissing6 = target_numbers6 - human_numbers

        target_numbers7 = {1, 5, 9}

        present7 = target_numbers7.intersection(human_numbers)

        missing7 = target_numbers7 - human_numbers

        amissing7 = target_numbers7 - human_numbers

        target_numbers8 = {3, 5, 7}

        present8 = target_numbers8.intersection(human_numbers)

        missing8 = target_numbers8 - human_numbers

        amissing8 = target_numbers8 - human_numbers

        target_numbers9 = {1, 2, 4}
        
        present9 = target_numbers9.intersection(human_numbers)
        
        missing9 = target_numbers9 - human_numbers

        amissing9 = target_numbers9 - human_numbers

        target_numbers10 = {3, 6, 2}

        present10 = target_numbers10.intersection(human_numbers)

        missing10 = target_numbers10 - human_numbers

        amissing10 = target_numbers10 - human_numbers

        target_numbers11 = {7, 8, 4}

        present11 = target_numbers11.intersection(human_numbers)

        missing11 = target_numbers11 - human_numbers

        amissing11 = target_numbers11 - human_numbers

        target_numbers12 = {9, 8, 6}

        present12 = target_numbers12.intersection(human_numbers)

        missing12 = target_numbers12 - human_numbers

        amissing12 = target_numbers12 - human_numbers

        target_numbers13 = {1, 3, 5}

        present13 = target_numbers13.intersection(human_numbers)

        missing13 = target_numbers13 - human_numbers

        amissing13 = target_numbers13 - human_numbers

        target_numbers14 = {3, 5, 9}

        present14 = target_numbers14.intersection(human_numbers)

        missing14 = target_numbers14 - human_numbers

        amissing14 = target_numbers14 - human_numbers

        target_numbers15 = {1, 5, 7}

        present15 = target_numbers15.intersection(human_numbers)

        missing15 = target_numbers15 - human_numbers

        amissing15 = target_numbers15 - human_numbers

        target_numbers16 = {7, 5, 9}

        present16 = target_numbers16.intersection(human_numbers)

        missing16 = target_numbers16 - human_numbers

        amissing16 = target_numbers16 - human_numbers

        amount1 = target_numbers1.intersection(computer_numbers)

        leftover1 = target_numbers1 - computer_numbers

        aleftover1 = target_numbers1 - computer_numbers

        amount2 = target_numbers2.intersection(computer_numbers)

        leftover2 = target_numbers2 - computer_numbers

        aleftover2 = target_numbers2 - computer_numbers

        amount3 = target_numbers3.intersection(computer_numbers)

        leftover3 = target_numbers3 - computer_numbers

        aleftover3 = target_numbers3 - computer_numbers

        amount4 = target_numbers4.intersection(computer_numbers)

        leftover4 = target_numbers4 - computer_numbers

        aleftover4 = target_numbers4 - computer_numbers

        amount5 = target_numbers5.intersection(computer_numbers)

        leftover5 = target_numbers5 - computer_numbers

        aleftover5 = target_numbers5 - computer_numbers

        amount6 = target_numbers6.intersection(computer_numbers)

        leftover6 = target_numbers6 - computer_numbers

        aleftover6 = target_numbers6 - computer_numbers

        amount7 = target_numbers7.intersection(computer_numbers)

        leftover7 = target_numbers7 - computer_numbers

        aleftover7 = target_numbers7 - computer_numbers

        amount8 = target_numbers8.intersection(computer_numbers)

        leftover8 = target_numbers8 - computer_numbers

        aleftover8 = target_numbers8 - computer_numbers

        computer_moved = False
        if 5 in human_numbers and len(human_numbers) == 2 and gamemode == "hard":
            computer_move = random.choice([1, 3, 7, 9])
            computer_numbers.add(computer_move)
            game_numbers.remove(computer_move)
            print("Computer played " + str(computer_move))
            time.sleep(1)
            computer_moved = True
        elif 5 not in human_numbers and len(human_numbers) == 2 and gamemode == "hard":
            computer_move = 5
            computer_numbers.add(computer_move)
            game_numbers.remove(computer_move)
            print("Computer played " + str(computer_move))
            time.sleep(1)
            computer_moved = True
        elif len(amount1) == 2 and aleftover1.pop() in game_numbers:
            computer_move = leftover1.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount2) == 2 and aleftover2.pop() in game_numbers:    
            computer_move = leftover2.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount3) == 2 and aleftover3.pop() in game_numbers:
            computer_move = leftover3.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount4) == 2 and aleftover4.pop() in game_numbers:
            computer_move = leftover4.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount5) == 2 and aleftover5.pop() in game_numbers: 
            computer_move = leftover5.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount6) == 2 and aleftover6.pop() in game_numbers:
            computer_move = leftover6.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount7) == 2 and aleftover7.pop() in game_numbers:    
            computer_move = leftover7.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(amount8) == 2 and aleftover8.pop() in game_numbers:
            computer_move = leftover8.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present1) == 2 and amissing1.pop() in game_numbers:
            computer_move = missing1.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present2) == 2 and amissing2.pop() in game_numbers:
            computer_move = missing2.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present3) == 2 and amissing3.pop() in game_numbers:
            computer_move = missing3.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present4) == 2 and amissing4.pop() in game_numbers:
            computer_move = missing4.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present5) == 2 and amissing5.pop() in game_numbers:
            computer_move = missing5.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present6) == 2 and amissing6.pop() in game_numbers:
            computer_move = missing6.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present7) == 2 and amissing7.pop() in game_numbers:
            computer_move = missing7.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present8) == 2 and amissing8.pop() in game_numbers:
            computer_move = missing8.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present9) == 2 and amissing9.pop() in game_numbers and gamemode == "hard":
            computer_move = missing9.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present10) == 2 and amissing10.pop() in game_numbers and gamemode == "hard":
            computer_move = missing10.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present11) == 2 and amissing11.pop() in game_numbers and gamemode == "hard":
            computer_move = missing11.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present12) == 2 and amissing12.pop() in game_numbers and gamemode == "hard":
            computer_move = missing12.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present13) == 2 and amissing13.pop() in game_numbers and gamemode == "hard":
            computer_move = missing13.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present14) == 2 and amissing14.pop() in game_numbers and gamemode == "hard":
            computer_move = missing14.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present15) == 2 and amissing15.pop() in game_numbers and gamemode == "hard":
            computer_move = missing15.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        elif len(present16) == 2 and amissing16.pop() in game_numbers and gamemode == "hard":
            computer_move = missing16.pop()
            if computer_move in game_numbers:
                computer_numbers.add(computer_move)
                game_numbers.remove(computer_move)
                print("Computer played " + str(computer_move))
                time.sleep(1)
                computer_moved = True
        else:
            computer_move = random.choice(list(game_numbers))
            game_numbers.remove(computer_move)
            computer_numbers.add(computer_move)
            time.sleep(1)
            print("Computer played " + str(computer_move))

        if 10 in computer_numbers:
            if 1 in human_numbers:
                one = Fore.RED + "X" + Style.RESET_ALL
            if 2 in human_numbers:
                two = Fore.RED + "X" + Style.RESET_ALL
            if 3 in human_numbers:
                three = Fore.RED + "X" + Style.RESET_ALL
            if 4 in human_numbers:
                four = Fore.RED + "X" + Style.RESET_ALL
            if 5 in human_numbers:
                five = Fore.RED + "X" + Style.RESET_ALL
            if 6 in human_numbers:
                six = Fore.RED + "X" + Style.RESET_ALL
            if 7 in human_numbers:
                seven = Fore.RED + "X" + Style.RESET_ALL
            if 8 in human_numbers:
                eight = Fore.RED + "X" + Style.RESET_ALL
            if 9 in human_numbers:
                nine = Fore.RED + "X" + Style.RESET_ALL
            if 1 in computer_numbers:
                one = Fore.BLUE + "O" + Style.RESET_ALL
            if 2 in computer_numbers:
                two = Fore.BLUE + "O" + Style.RESET_ALL
            if 3 in computer_numbers:
                three = Fore.BLUE + "O" + Style.RESET_ALL
            if 4 in computer_numbers:
                four = Fore.BLUE + "O" + Style.RESET_ALL
            if 5 in computer_numbers:
                five = Fore.BLUE + "O" + Style.RESET_ALL
            if 6 in computer_numbers:
                six = Fore.BLUE + "O" + Style.RESET_ALL
            if 7 in computer_numbers:
                seven = Fore.BLUE + "O" + Style.RESET_ALL
            if 8 in computer_numbers:
                eight = Fore.BLUE + "O" + Style.RESET_ALL
            if 9 in computer_numbers:
                nine = Fore.BLUE + "O" + Style.RESET_ALL
            time.sleep(1)
            print(f"""Here is the tic-tac-toe board after computer's move:

            
         |     |     
      {one}  |  {two}  |  {three}  
    _____|_____|_____
         |     |     
      {four}  |  {five}  |  {six} 
    _____|_____|_____
         |     |     
      {seven}  |  {eight}  |  {nine}  
         |     |     """)
        if 1 in computer_numbers and 2 in computer_numbers and 3 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 4 in computer_numbers and 5 in computer_numbers and 6 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 7 in computer_numbers and 8 in computer_numbers and 9 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 1 in computer_numbers and 4 in computer_numbers and 7 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 2 in computer_numbers and 5 in computer_numbers and 8 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 3 in computer_numbers and 6 in computer_numbers and 9 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 1 in computer_numbers and 5 in computer_numbers and 9 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
        elif 3 in computer_numbers and 5 in computer_numbers and 7 in computer_numbers:
            print("Computer wins, better luck next time!")
            playagain = input("Would you like to play again? (yes or no): ").lower()
            break
    if playagain == "yes":
        continue
    if playagain == "no":
        print("Thanks for playing!")
        break
        
                
    