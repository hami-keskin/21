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


def count_high_cards(deck):
    high_cards = [10, 11]
    remaining_cards = deck.count(high_cards[0]) + deck.count(high_cards[1])
    total_cards = len(deck)
    return remaining_cards / (total_cards / 52)  # Divide by total cards in a single deck


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


def suggest_action(user_score, computer_card, remaining_cards, deck):  # Pass the deck variable
    if user_score > 21:
        return "You should pass."

    if user_score <= 11:
        return "You should draw a card."

    if computer_card == 11:
        return "You should be cautious and consider passing."

    if remaining_cards > 0:
        high_card_ratio = count_high_cards(deck)  # Pass the entire deck
        if high_card_ratio > 0.5:
            return "You may consider drawing a card to increase your chances of a higher score."
        else:
            return "It's better to be cautious and pass."
    else:
        return "There are no more cards in the deck. You should pass."


def play_game():
    num_decks = 4
    deck = create_deck(num_decks)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card(deck))
        computer_cards.append(deal_card(deck))

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    print(suggest_action(user_score, computer_cards[0], len(deck), deck))  # Pass the entire deck

    while not is_game_over:
        should_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()

        if should_deal == 'y':
            user_cards.append(deal_card(deck))
            user_score = calculate_score(user_cards)
            print(f" Your cards: {user_cards}, current score: {user_score}")
            print(suggest_action(user_score, computer_cards[0], len(deck), deck))  # Pass the entire deck
            if user_score > 21:
                is_game_over = True
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
