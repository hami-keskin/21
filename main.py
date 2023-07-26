import random


class Player:
    def __init__(self):
        self.chips = 100  # Initial chips
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def win_chips(self, amount):
        self.chips += amount
        self.wins += 1

    def lose_chips(self, amount):
        self.chips -= amount
        self.losses += 1

    def draw_chips(self):
        self.draws += 1

    def __str__(self):
        return f"Chips: {self.chips}, Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}"


def create_deck(num_decks):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = cards * num_decks
    random.shuffle(deck)
    return deck


def deal_card(deck, num_decks):
    if not deck:
        print("Deck is empty. Reshuffling...")
        deck = create_deck(num_decks)  # Reshuffle the deck if empty
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
        return "Draw"
    elif computer_score == 21:
        return "Loss"
    elif user_score == 21:
        return "Win"
    elif user_score > 21:
        return "Loss"
    elif computer_score > 21:
        return "Win"
    elif user_score > computer_score:
        return "Win"
    else:
        return "Loss"


def suggest_action(user_score, computer_card, deck):
    if user_score > 21:
        return "You should pass."

    # Soft hand (contains an Ace)
    if 11 in deck and user_score < 19:
        return "You should draw a card."

    # Hard hand (no Ace)
    if user_score <= 11:
        return "You should draw a card."
    elif user_score >= 17:
        return "You should pass."
    elif 12 <= user_score <= 16:
        # Dealer's face-up card
        dealer_card = computer_card
        if 2 <= dealer_card <= 6:
            return "You should pass."
        else:
            return "You should draw a card."
    else:
        return "You should draw a card."


def play_game():
    num_decks = 4
    deck = create_deck(num_decks)

    user = Player()

    while True:
        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card(deck, num_decks))
            computer_cards.append(deal_card(deck, num_decks))

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        print(suggest_action(user_score, computer_cards[0], deck))  # Pass the entire deck

        while not is_game_over:
            should_deal = input("Type 'y' to get another card, or 'n' to pass: ").lower()

            if should_deal == 'y':
                user_cards.append(deal_card(deck, num_decks))
                user_score = calculate_score(user_cards)
                print(f" Your cards: {user_cards}, current score: {user_score}")
                print(suggest_action(user_score, computer_cards[0], deck))  # Pass the entire deck
                if user_score > 21:
                    is_game_over = True
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card(deck, num_decks))
            computer_score = calculate_score(computer_cards)

        print(f" Your final hand: {user_cards}, final score: {user_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")

        result = compare(user_score, computer_score)
        if result == "Win":
            user.win_chips(10)  # You can adjust the winning chips amount as desired
        elif result == "Loss":
            user.lose_chips(10)  # You can adjust the losing chips amount as desired
        else:
            user.draw_chips()

        print(f"Result: {result}")
        print(user)

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
