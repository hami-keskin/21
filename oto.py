import random


class Player:
    def __init__(self):
        self.chips = 100
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


def deal_card(deck):
    if not deck:
        print("Deck is empty. Reshuffling...")
        return create_deck(4)
    return deck.pop(0)


def calculate_score(cards):
    total_score = 0
    aces = 0

    for card in cards:
        if card == 11:
            aces += 1
        total_score += card

    while total_score > 21 and aces > 0:
        total_score -= 10
        aces -= 1

    return total_score


def count_high_cards(deck):
    high_cards = [10, 11]
    remaining_cards = deck.count(high_cards[0]) + deck.count(high_cards[1])
    total_cards = len(deck)
    return remaining_cards / (total_cards / 52)


def compare(user_score, computer_score):
    if user_score == 0 or computer_score == 0:
        if user_score == computer_score:
            return "Draw"
        elif user_score == 0:
            return "Win"
        else:
            return "Loss"

    if user_score > 21 or computer_score > 21:
        if user_score > 21:
            return "Loss"
        elif computer_score > 21:
            return "Win"
        else:
            return "Draw"

    if user_score > computer_score:
        return "Win"
    elif user_score < computer_score:
        return "Loss"
    else:
        return "Draw"


def suggest_action(user_score, computer_card, deck):
    if user_score > 21:
        return "PASS"

    if 11 in deck and user_score < 19:
        return "DRAW"

    if user_score <= 11:
        return "DRAW"
    elif user_score >= 17:
        return "PASS"
    elif 12 <= user_score <= 16:
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
    total_games = 10000
    wins = 0
    losses = 0
    draws = 0

    for game in range(total_games):
        user_cards = []
        computer_cards = []

        for _ in range(2):
            user_cards.append(deal_card(deck))
            computer_cards.append(deal_card(deck))

        while True:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            print(f" Your cards: {user_cards}, current score: {user_score}")
            print(f" Computer's first card: {computer_cards[0]}")
            print(suggest_action(user_score, computer_cards[0], deck))

            should_deal = suggest_action(user_score, computer_cards[0], deck)

            if should_deal == "DRAW":
                user_cards.append(deal_card(deck))
                user_score = calculate_score(user_cards)
                if user_score > 21:
                    break
            else:
                break

        while computer_score < 17 and user_score <= 21:
            computer_cards.append(deal_card(deck))
            computer_score = calculate_score(computer_cards)

        print(f" Your final hand: {user_cards}, final score: {user_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")

        result = compare(user_score, computer_score)
        if result == "Win":
            wins += 1
            user.win_chips(10)
        elif result == "Loss":
            losses += 1
            user.lose_chips(10)
        else:
            draws += 1
            user.draw_chips()

        print(f"Result: {result}\n")

    print("Overall Results:")
    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print(user)


if __name__ == "__main__":
    play_game()
