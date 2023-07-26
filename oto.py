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
    # This function compares the scores of the user and the computer and returns the result of the game.
    # The function takes two integers as parameters, representing the scores of the user and the computer.
    # The function returns a string, indicating whether the user wins, loses or draws.

    # If either score is 0, it means blackjack
    if user_score == 0 or computer_score == 0:
        if user_score == computer_score:
            return "Draw"
        elif user_score == 0:
            return "Win"
        else:
            return "Loss"

    # If either score is over 21, it means bust
    if user_score > 21 or computer_score > 21:
        if user_score > 21:
            return "Loss"
        elif computer_score > 21:
            return "Win"
        else:
            return "Draw"

    # If neither score is blackjack or bust, compare them normally
    if user_score > computer_score:
        return "Win"
    elif user_score < computer_score:
        return "Loss"
    else:
        return "Draw"


def suggest_action(user_score, computer_card, deck):
    if user_score > 21:
        return "PASS"

    # Soft hand (contains an Ace)
    if 11 in deck and user_score < 19:
        return "DRAW"

    # Hard hand (no Ace)
    if user_score <= 11:
        return "DRAW"
    elif user_score >= 17:
        return "PASS"
    elif 12 <= user_score <= 16:
        # Dealer's face-up card
        dealer_card = computer_card
        if 2 <= dealer_card <= 6:
            return "PASS"
        else:
            return "DRAW"
    else:
        return "DRAW"


def play_game():
    num_decks = 4
    deck = create_deck(num_decks)

    user = Player()
    total_games = 100
    wins = 0
    losses = 0
    draws = 0

    for game in range(total_games):
        user_cards = []
        computer_cards = []

        for _ in range(2):
            user_cards.append(deal_card(deck, num_decks))
            computer_cards.append(deal_card(deck, num_decks))

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Player's turn
        while True:
            print(f" Your cards: {user_cards}, current score: {user_score}")
            print(f" Computer's first card: {computer_cards[0]}")
            print(suggest_action(user_score, computer_cards[0], deck))  # Pass the entire deck

            # Automatically decide based on suggestion
            should_deal = suggest_action(user_score, computer_cards[0], deck)[0]  # Take the first character of the suggestion
            print(f"Computer chooses: {should_deal}")

            if should_deal == 'D':
                user_cards.append(deal_card(deck, num_decks))
                user_score = calculate_score(user_cards)
                if user_score > 21:
                    break
            else:
                break

        # Computer's turn
        while computer_score < 17 and user_score <= 21:
            computer_cards.append(deal_card(deck, num_decks))
            computer_score = calculate_score(computer_cards)

        print(f" Your final hand: {user_cards}, final score: {user_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")

        # Compare results and update stats
        result = compare(user_score, computer_score)
        if result == "Win":
            wins += 1
            user.win_chips(10)  # You can adjust the winning chips amount as desired
        elif result == "Loss":
            losses += 1
            user.lose_chips(10)  # You can adjust the losing chips amount as desired
        else:
            draws += 1
            user.draw_chips()

        print(f"Result: {result}\n")

    # Print overall results
    print("Overall Results:")
    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print(user)


if __name__ == "__main__":
    play_game()