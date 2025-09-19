###################### Our Blackjack House Rules ######################
## The deck is of unllimited size
## There are no jokers
## The Jack/Queen/King all count as 10
## The Ace can count as 11 or 1
## Each has an equal probability of being drawn
## A card is not removed from the deck as they are drawn 

import random
from clear import clear  
from logo import logo  

# Deck (Ace=11, face cards=10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Return a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Take a list of cards and return the score."""
    score = sum(hand)

    # Blackjack: Ace + 10 in 2 cards
    if score == 21 and len(hand) == 2:
        return 0  

    # Adjust Aces: convert 11 -> 1 if over 21
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
        
    return score

def compare(user_score, comp_score):
    """Compare user and computer scores and return result string."""
    if user_score == comp_score:
        return "It's a draw 😐"
    elif comp_score == 0:
        return "Computer has Blackjack! You lose 😭"
    elif user_score == 0:
        return "Blackjack! You win 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Computer went over. You win 😎"
    elif user_score > comp_score:
        return "You win 😎"
    else:
        return "You lose 😭"

def play_game():
    """ starts the game and continues dealing cards"""
    print(logo)
    print("Welcome to Blackjack!\n")

    user_hand = [deal_card(), deal_card()]
    comp_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        comp_score = calculate_score(comp_hand)

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {comp_hand[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == "y":
                user_hand.append(deal_card())
            else:
                game_over = True

    # Computer keeps drawing until 17+
    while comp_score != 0 and comp_score < 17:
        comp_hand.append(deal_card())
        comp_score = calculate_score(comp_hand)

    print(f"\nYour final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {comp_hand}, final score: {comp_score}")
    print(compare(user_score, comp_score))
    
    #play another round
    continue_playing = input("Do you want to play another round? Type 'y' or 'n': ")
    if continue_playing == 'y':
        clear()
        play_game()
    else:
        print('Thank you for playing😁')

#start game
start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    play_game()
else:
    print('ok maybe next time🥲')


