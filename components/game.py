import mysql.connector
import random
from components.round import play_round

def get_categories(connection):
    """
    Fetches column names (categories) from the 'the_categories' table in MySQL.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = 'the_categories'
            AND TABLE_SCHEMA = 'final_categories';  # Replace with your actual database name
        """)
        columns = cursor.fetchall()  # Fetch all rows
        categories = [column[0] for column in columns]  # Extract column names
        return categories
    except mysql.connector.Error as e:
        print(f"Error fetching categories: {e}")
        return []  # Return an empty list in case of error


def play_game(connection, num_rounds, num_players):
    total_scores = [0] * num_players
    categories = get_categories(connection)

    if not categories:  # Handle the case where no categories are returned
        print("No categories available in the database.")
        return

    eliminated_players = set()  # Set of eliminated players
    for round_number in range(1, num_rounds + 1):
        category = random.choice(categories)  # Randomly select a category for the round
        print(f"\n--- Round {round_number} ---")
        valid_players, round_scores = play_round(category, num_players, eliminated_players)

        # Update total scores for players who are still in the game
        for i in range(num_players):
            if i + 1 in valid_players:  # Only add score for valid players
                total_scores[i] += round_scores[i] if round_scores[i] is not None else 0

        # Eliminate players who didn't give a valid and unique answer
        eliminated_players.update([i for i in range(num_players) if round_scores[i] is None])

        print(f"Players remaining after round {round_number}: {', '.join(map(str, valid_players))}")

        # If only two players remain, end the game and play the final round
        if len(valid_players) == 2:
            print("\nOnly two players remain. Starting the final round!")
            winner, final_scores = (category, [valid_players[0] - 1, valid_players[1] - 1])
            total_scores[valid_players[0] - 1] += final_scores[0] if winner[0] == valid_players[0] else 0
            total_scores[valid_players[1] - 1] += final_scores[1] if winner[0] == valid_players[1] else 0
            break

    # Output final results
    print("\nGame Over!")
    for i in range(num_players):
        if i + 1 in eliminated_players:
            continue  # Don't show eliminated players
        print(f"Player {i + 1} Total Score: {total_scores[i]}")

    # Find the overall winner based on total score
    max_total_score = max(total_scores)
    overall_winners = [f"Player {i + 1}" for i, score in enumerate(total_scores) if score == max_total_score]

    if len(overall_winners) > 1:
        print("Overall Result: It's a tie between " + ", ".join(overall_winners) + "!")
    else:
        print(f"Overall Winner: {overall_winners[0]}!")

    # Determine the Player of the Game based on highest total score
    player_of_the_game = f"Player {total_scores.index(max_total_score) + 1}"
    print(f"\nThe Player of the Game is: {player_of_the_game}")
