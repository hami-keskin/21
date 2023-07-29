def strategy(player_score, computer_card):
    if player_score == 9 and 2 <= computer_card <= 6:
        return "DOUBLE"
    elif player_score == 10 and 2 <= computer_card <= 9:
        return "DOUBLE"
    elif player_score == 11 and 2 <= computer_card <= 10:
        return "DOUBLE"
    elif player_score == 12 and 4 <= computer_card <= 6:
        return "DRAW"
    elif player_score in [13, 14, 15, 16] and 2 <= computer_card <= 6:
        return "DRAW"
    elif player_score >= 17:
        return "PASS"
    else:
        return None


def suggest_action(player_hand, computer_card, deck):
    player_score = sum(player_hand)

    # Öncelikle, oyuncunun kart toplamı 21'i geçmişse "PASS" önerilir.
    if player_score > 21:
        return "PASS"

    action = strategy(player_score, computer_card)
    if action is not None:
        return action

    # Yumuşak el (As içeren el)
    if player_score < 19 and any(card == 11 for card in player_hand):
        return 'DRAW'

    # Sert el
    if player_score <= 11:
        return 'DRAW'
    else:
        return 'PASS'


import random


def simulate_games(num_games):
    wins = 0
    total_games = num_games

    for _ in range(num_games):
        # Oyuncunun eli ve bilgisayarın açık kartını rastgele oluştur
        player_hand = [random.randint(2, 11), random.randint(2, 11)]
        computer_card = random.randint(2, 11)

        # Stratejiye göre oyuncunun hamlesini al
        action = suggest_action(player_hand, computer_card, [])

        # Oyuncunun elini tamamla
        while action == "DRAW":
            new_card = random.randint(2, 11)
            player_hand.append(new_card)
            player_score = sum(player_hand)

            # Yumuşak el (As içeren el) için As'ın değerini ayarla
            if 11 in player_hand and player_score > 21:
                player_hand[player_hand.index(11)] = 1
                player_score = sum(player_hand)

            if player_score > 21:
                break

            action = suggest_action(player_hand, computer_card, [])

        # Son durumda oyunu değerlendir
        player_score = sum(player_hand)
        if player_score <= 21 and (player_score > sum([computer_card]) or sum([computer_card]) > 21):
            wins += 1

    success_rate = wins / total_games
    return success_rate


# Başarı oranını 100,000 oyun için simüle et
success_rate = simulate_games(100000)
print("Başarı Oranı:", success_rate)
