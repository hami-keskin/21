def suggest_action(player_hand, computer_card, deck):
    player_score = sum(player_hand)

    # Öncelikle, oyuncunun kart toplamı 21'i geçmişse "PASS" önerilir.
    if player_score > 21:
        return "PASS"

    # Strateji tablosu tanımlama
    strategy_table = {
        (9, 2): "DOUBLE",
        (9, 3): "DOUBLE",
        (9, 4): "DOUBLE",
        (9, 5): "DOUBLE",
        (9, 6): "DOUBLE",
        (10, 2): "DOUBLE",
        (10, 3): "DOUBLE",
        (10, 4): "DOUBLE",
        (10, 5): "DOUBLE",
        (10, 6): "DOUBLE",
        (11, 2): "DOUBLE",
        (11, 3): "DOUBLE",
        (11, 4): "DOUBLE",
        (11, 5): "DOUBLE",
        (11, 6): "DOUBLE",
        (17, 2): "PASS",
        (17, 3): "PASS",
        (17, 4): "PASS",
        (17, 5): "PASS",
        (17, 6): "PASS",
    }

    # Oyuncunun eli ile bilgisayar kartını birleştirerek tablodan stratejiyi al
    if (player_score, computer_card) in strategy_table:
        return strategy_table[(player_score, computer_card)]

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
