import random, time

board = [' '] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board():
    display = [str(i+1) if board[i] == ' ' else board[i] for i in range(9)]
    print(f"""
          
      |     |     
   {display[0]}  |  {display[1]}  |  {display[2]}  
 _____|_____|_____
      |     |     
   {display[3]}  |  {display[4]}  |  {display[5]} 
 _____|_____|_____
      |     |     
   {display[6]}  |  {display[7]}  |  {display[8]}
      |     |     """)

print_board()

while True:
    try:
        h = int(input("Where would you like to place your piece pick a number 1-9: ")) - 1
        if board[h] != ' ':
            print("Spot taken")
            continue
        board[h] = 'X'
        print_board()
        if any(all(board[i] == 'X' for i in w) for w in wins):
            print("You win!")
            break
    except (ValueError, IndexError):
        print("Invalid input")
        continue

    time.sleep(0.5)
    print("Computer thinking...")

    # AI logic
    available = [i for i in range(9) if board[i] == ' ']
    if not available:
        break

    # Check for win
    for w in wins:
        if sum(1 for i in w if board[i] == 'O') == 2 and any(board[i] == ' ' for i in w):
            move = next(i for i in w if board[i] == ' ')
            break
    else:
        # Check for block
        for w in wins:
            if sum(1 for i in w if board[i] == 'X') == 2 and any(board[i] == ' ' for i in w):
                move = next(i for i in w if board[i] == ' ')
                break
        else:
            # Center if available
            if 4 in available:
                move = 4
            else:
                # Corner
                corners = [i for i in [0,2,6,8] if i in available]
                if corners:
                    move = random.choice(corners)
                else:
                    move = random.choice(available)

    board[move] = 'O'
    print(f"Computer played {move+1}")
    print_board()
    if any(all(board[i] == 'O' for i in w) for w in wins):
        print("Computer wins!")
        break
        