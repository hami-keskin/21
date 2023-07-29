import random
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
    elif 12 <= player_score <= 16:
        # Bilgisayarın açık kartı
        dealer_card = computer_card
        if 2 <= dealer_card <= 6:
            return "PASS"
        else:
            return "DRAW"
    else:
        return "DRAW"
def simulate_games(num_games):
    num_correct_moves = 0

    for _ in range(num_games):
        player_hand = []
        computer_card = random.randint(2, 11)
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        # İlk iki kartı dağıt
        player_hand.append(random.choice(deck))
        player_hand.append(random.choice(deck))

        while True:
            action = suggest_action(player_hand, computer_card, deck)
            if action == "DRAW":
                player_hand.append(random.choice(deck))
            elif action == "PASS":
                break

            player_score = sum(player_hand)
            if player_score > 21:
                break

        if player_score <= 21:
            num_correct_moves += 1

    return num_correct_moves / num_games

# 1000 oyunu simüle et ve başarı oranını hesapla
num_games = 1000
success_rate = simulate_games(num_games)

print(f"Stratejinin başarı oranı: {success_rate:.2f}")
