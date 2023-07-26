import random


def create_deck(num_decks):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = cards * num_decks
    random.shuffle(deck)
    return deck


def deal_card(deck):
    return deck.pop()


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    num_decks = 4  # 4 desteyi temsil eden 208 kartlık bir destemiz var
    deck = create_deck(num_decks)

    user_cards = []
    computer_cards = []
    is_game_over = False
    is_double_down = False

    for _ in range(2):
        user_cards.append(deal_card(deck))
        computer_cards.append(deal_card(deck))

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not is_game_over:
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or is_double_down:
            is_game_over = True
        else:
            should_deal = input("Type 'y' to get another card, 'd' to double down, or 'n' to pass: ")

            if should_deal == 'y':
                user_cards.append(deal_card(deck))
                user_score = calculate_score(user_cards)
            elif should_deal == 'd':
                user_cards.append(deal_card(deck))
                user_score = calculate_score(user_cards)
                is_double_down = True
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(deck))
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
