import random

NUM_ROUNDS = 5

while True:
    score = 0  
    round_num = 1  

    while round_num <= NUM_ROUNDS:

        computer_num = random.randint(0, 100)
        user_num = random.randint(0, 100)
        
        print(f"\n=== Round {round_num} ===")
        print(f"Your number is {user_num}.")
        
        prompt = input("Guess if it is higher or lower than the computer number (type 'higher' or 'lower'):\t")
        
        if prompt == "higher":
            if user_num > computer_num:
                score += 1
                print(f"You were right! The computer's number was {computer_num}. Your score: {score}")
            else:
                score = max(0, score - 1)  # Prevent negative scores
                print(f"You were wrong! The computer's number was {computer_num}. Your score: {score}")
            round_num += 1  

        elif prompt == "lower":
            
            if user_num < computer_num:
                score += 1
                print(f"You were right! The computer's number was {computer_num}. Your score: {score}")
            else:
                score = max(0, score - 1)  # Prevent negative scores
                print(f"You were wrong! The computer's number was {computer_num}. Your score: {score}")
            round_num += 1  # Move to the next round

        else:
           
            print("Invalid input! The game will restart from Round 1.")
            break  

        print("\n-------------------------")

   
    if round_num > NUM_ROUNDS:
        print(f"\nGame Over! Your final score after {NUM_ROUNDS} rounds is: {score}")
        print("""
        Thanks for playing!
        Good job, you played really well!
        """)
        break 
