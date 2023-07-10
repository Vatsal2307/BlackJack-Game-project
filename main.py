############### Blackjack Project #####################
import random
from replit import clear 
from art import logo
print(logo)


card = 0
def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for i in range(2):
    user_cards.append(deal_cards()) 
    computer_cards.append(deal_cards())
  
  
  def calc_score(cards): 
    if sum(cards)== 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)   
    return sum(cards)
  
  def compare(user_score, comp_score):
    if user_score == comp_score:
      return "draw 😶‍🌫️"
    elif comp_score == 0:
      return"Computer has blackjack, you lose 😒"
    elif user_score == 0:
      return "You have a blackjack, you win! 🤩"
    elif user_score > 21:
      return "You lose! 😖"
    elif comp_score > 21:
      return "You win! 🥳"
    elif user_score > comp_score:
      return " You win! 🥳"
    else:
      return "Computer wins, you lose! 😖"
    
  
  while not is_game_over: 
    user_score = calc_score(cards = user_cards)
    comp_score = calc_score(cards = computer_cards)
    print(f"Your hand : {user_cards}, Your score is {user_score} ")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or comp_score == 0 or user_score > 21:
      is_game_over = True  
  
    else:
      next_move =  input("Do you wish to draw another card? Type 'y' for yes and 'n' for no: ")
      if next_move == 'y': 
        user_cards.append(deal_cards())
        user_score = calc_score(cards = user_cards)   
      else: 
        is_game_over = True
  
  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_cards())
    comp_score = calc_score(computer_cards)
  
  print(f"Computer's final hand {computer_cards}, and Computer's final score is: {comp_score}")
  print(compare(user_score, comp_score))
  
while input("Do you want to play a new game? Type 'y'for yes and 'n' for no: ") == "y":
  clear()
  play_game()




  

