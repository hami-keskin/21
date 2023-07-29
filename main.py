def suggest_action(player_hand, computer_card, deck):
    player_score = sum(player_hand)

    # Öncelikle, oyuncunun kart toplamı 21'i geçmişse "PASS" önerilir.
    if player_score > 21:
        return "PASS"

    # Yumuşak el (As içeren el)
    if 11 in player_hand and player_score < 19:
        return "DRAW"

    # Sert el (As içermeyen el)
    if player_score <= 11:
        return "DRAW"
    elif player_score >= 17:
        return "PASS"
    elif player_score == 9 or player_score == 10:
        dealer_card = computer_card
        if 2 <= dealer_card <= 9:
            return "DOUBLE"
        else:
            return "DRAW"
    elif 12 <= player_score <= 16:
        # Bilgisayarın açık kartı
        dealer_card = computer_card
        if dealer_card == 4 or dealer_card == 5 or dealer_card == 6:
            return "DRAW"
        else:
            return "PASS"
    else:
        return "DRAW"


import random

def simulate_game(strategy_func, num_games=10000):
    wins = 0
    losses = 0
    draws = 0

    for _ in range(num_games):
        # Yapay bir deste oluştur
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        # Oyuncunun başlangıç elini ve bilgisayarın açık kartını belirle
        player_hand = random.sample(deck, 2)
        computer_card = random.choice(deck)

        while True:
            action = strategy_func(player_hand, computer_card, deck)
            if action == "DRAW":
                drawn_card = random.choice(deck)
                player_hand.append(drawn_card)
                deck.remove(drawn_card)
            elif action == "DOUBLE":
                drawn_card = random.choice(deck)
                player_hand.append(drawn_card)
                deck.remove(drawn_card)
                break
            else:
                break

        player_score = sum(player_hand)
        if player_score > 21:
            losses += 1
        elif player_score == 21:
            wins += 1
        else:
            draws += 1

    return wins, losses, draws

if __name__ == "__main__":
    wins, losses, draws = simulate_game(suggest_action)
    total_games = wins + losses + draws

    print(f"Başarı Oranı: {wins / total_games:.2%}")
    print(f"Kayıp Oranı: {losses / total_games:.2%}")
    print(f"Beraberlik Oranı: {draws / total_games:.2%}")
