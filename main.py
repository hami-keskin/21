from st import suggest_action

import random


# Define a function to simulate multiple games and calculate success rate
def simulate_games(num_games):
    wins = 0
    total_games = num_games

    for _ in range(num_games):
        # Generate random player hand and computer's open card
        player_hand = [random.randint(2, 11), random.randint(2, 11)]
        computer_card = random.randint(2, 11)

        # Get the player's action based on the strategy
        action = suggest_action(player_hand, computer_card, [])

        # Complete the player's hand
        while action == "DRAW":
            new_card = random.randint(2, 11)
            player_hand.append(new_card)
            player_score = sum(player_hand)

            # Adjust the value of Ace for soft hand (if necessary)
            if 11 in player_hand and player_score > 21:
                player_hand[player_hand.index(11)] = 1
                player_score = sum(player_hand)

            if player_score > 21:
                break

            action = suggest_action(player_hand, computer_card, [])

        # Evaluate the game in the final state
        player_score = sum(player_hand)
        if player_score <= 21 and (player_score > sum([computer_card]) or sum([computer_card]) > 21):
            wins += 1

    success_rate = wins / total_games
    return success_rate


# Simulate success rate for 100,000 games
success_rate = simulate_games(100000)
print("Success Rate:", success_rate)
