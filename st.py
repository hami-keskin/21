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
