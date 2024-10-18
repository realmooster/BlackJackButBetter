import random

def dealerHands():
    global dealer_total
    dealer_total = 0
    dealer = random.randint(1, 10)
    print("Dealer pulled a", dealer, "card")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    dealer_total += dealer
    
    while dealer_total < 17:
        new_card = random.randint(1, 10)
        dealer_total += new_card
        print(f"Dealer draws {new_card}. Dealer's total is now {dealer_total}.")
        
        # Check if dealer busts
        if dealer_total > 21:
            print("The dealer has busted. You win!")
            print("---------------------------------------")
            return True  # Return True indicating dealer busted
    
    # Check if dealer got a Blackjack (exactly 21)
    if dealer_total == 21:
        print("Dealer Wins with a Black Jack.")
        print("---------------------------------------")
        return True  # Return True indicating dealer got a Black Jack
    
    return False  # Return False indicating dealer did not bust or get Black Jack

def playersHand():
    global player_total
    player_total = 0
    first = random.randint(1, 10)
    second = random.randint(1, 10)
    player_total = first + second
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Player starts with a {first} card and a {second} card, resulting in a total of {player_total}.")
    
    while True:
        choice = input("Hit or Stand: ").lower()
        if choice == "hit":
            hit = random.randint(1, 10)
            print(f"Player pulled a {hit} card.")
            player_total += hit
            print(f"You now have {player_total}.")
            
            if player_total > 21:
                print("Player has busted! The Dealer has won.")
                return
        elif choice == "stand":
            break  # Player stands, break out of loop
        else:
            print("Invalid input! Please choose 'hit' or 'stand'.")
    
    # After standing, compare player's hand with dealer's hand
    if dealer_total > player_total:
        print("You lose. Dealer has a higher count hand.")
    elif dealer_total < player_total:
        print("You won! Your hand was bigger than the Dealer's hand.")
    elif player_total == 21:
        print("Player has Black Jack!")

# Main game loop
def playGame():
    dealer_busted_or_blackjack = dealerHands()
    if dealer_busted_or_blackjack:
        return  # Exit the game if dealer busted or got a Black Jack
    
    playersHand()

    # Check for both player and dealer Black Jack
    if player_total == dealer_total:
        print("You lose! The Dealer wins.")

# Function to repeat the game
def startGame():
    while True:
        playGame()  # Play the game

        #Repeats the game
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break  # Exit the loop if the player doesn't want to play again

startGame()