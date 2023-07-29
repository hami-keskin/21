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