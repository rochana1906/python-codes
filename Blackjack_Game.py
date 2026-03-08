import random
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card(cards):
  return random.choice(cards)

def calculate_score(hand):
  score=sum(hand)

  if 11 in hand and score>21:
    hand.remove(11)
    hand.append(1)
    score=sum(hand)

  return score

def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose 😢"
    elif computer_score > 21:
        return "Computer went over. You win 🎉"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_blackjack():
    print("🃏 Welcome to Blackjack!\n")

    user_cards = []
    computer_cards = []

    # Deal first two cards
    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score > 21:
            game_over = True
            break
        choice = input("Type 'y' to get another card, 'n' to pass: ").lower()

        if choice == 'y':
            user_cards.append(deal_card(cards))
        else:
            game_over = True

    # Computer turn
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card(cards))

    # Final scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("\n--- Final Results ---")
    print(f"Your cards: {user_cards}, Final score: {user_score}")
    print(f"Computer's cards: {computer_cards}, Final score: {computer_score}")

    print(compare(user_score, computer_score))


# Run the game
play_blackjack()
