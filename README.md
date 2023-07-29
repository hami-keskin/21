# Blackjack Strategy Simulator

This program simulates multiple games of Blackjack and calculates the success rate of a given strategy.

## How it works

The program defines two functions: `strategy` and `suggest_action`.

The `strategy` function takes in the player's score and the computer's card as arguments and returns a recommended action based on a set of predefined rules.

The `suggest_action` function takes in the player's hand, the computer's card, and the deck as arguments. It calculates the player's score and recommends an action based on the strategy function. If the player's hand total has exceeded 21, it recommends "PASS". If the player has a soft hand (contains an Ace) and their score is less than 19, it recommends "DRAW". If the player has a hard hand and their score is less than or equal to 11, it recommends "DRAW". Otherwise, it recommends "PASS".

The program also defines a `simulate_games` function that takes in the number of games to simulate as an argument. It generates random player hands and computer cards, gets the player's action based on the strategy, completes the player's hand, and evaluates the game in its final state. It calculates the success rate as the number of wins divided by the total number of games.

## Usage

To use this program, simply run it with Python. It will simulate 100,000 games and print out the success rate.
