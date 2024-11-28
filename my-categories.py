# Libraries
import mysql.connector
import sqlite3
import random


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Your MySQL server host
            user='root',  # Your MySQL username
            password='toor',  # Your MySQL password
            port='3306',
            database='final_categories'  # The database you want to connect to
        )
        print("Connection to MySQL DB successful")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    return connection


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

def play_round(category, num_players):
    print(f"\nPlaying round in category: {category}")
    scores = [random.randint(0, 10) for _ in range(num_players)]

    for i in range(num_players):
        print(f"Player {i + 1} Score: {scores[i]}")

    max_score = max(scores)
    winners = [f"Player {i + 1}" for i, score in enumerate(scores) if score == max_score]

    return winners, scores

def play_game(connection, num_rounds, num_players):
    total_scores = [0] * num_players
    categories = get_categories(connection)

    if not categories:  # Handle the case where no categories are returned
        print("No categories available in the database.")
        return

    for round_number in range(1, num_rounds + 1):
        category = random.choice(categories)  # Randomly select a category for the round
        print(f"\n--- Round {round_number} ---")
        winners, round_scores = play_round(category, num_players)

        for i in range(num_players):
            total_scores[i] += round_scores[i]

        for winner in winners:
            print(f"{winner} wins this round!")

    # Output final results
    print("\nGame Over!")
    for i in range(num_players):
        print(f"Player {i + 1} Total Score: {total_scores[i]}")

    max_total_score = max(total_scores)
    overall_winners = [f"Player {i + 1}" for i, score in enumerate(total_scores) if score == max_total_score]

    if len(overall_winners) > 1:
        print("Overall Result: It's a tie between " + ", ".join(overall_winners) + "!")
    else:
        print(f"Overall Winner: {overall_winners[0]}!")

# Main game function with input handling
try:
    rounds = int(input("Enter the number of rounds you wish to play: "))
    db_connection = create_connection()
    play_game(db_connection, rounds, 6)  # Set number of players to 6
except ValueError:
    print("Please enter a valid number.")
finally:
    if db_connection:
        db_connection.close()



#Distinguish who plays and win
#Distinguish who should be eliminated to the game
#Distinguish who is using the same word or answer





# Task Done:
# Already connected the database connection to python with pycharm
# We will start the game logic #2

# 2nd Game Instructions:
# Before starting the game, players can set the number of rounds they wish to play. For example, if set to 4 rounds, players will compete for 4 rounds before a final winner is declared.
# At the start of each round, a random category (e.g., Animals, Countries, Colors) is displayed on the screen.
# Each round ends with a "last man standing," who earns points for winning that round. The player with the most points at the end of all rounds is the game winner.
# Players have 10 seconds to submit a word that fits the category. Failure to provide a word within the set time results in elimination from that round.
# Once a player submits a word, it is temporarily hidden from other players until they submit their own words, ensuring no one can see which words have already been used.
# After each submission, the server checks if the word has already been used. Players should avoid submitting words from the set of used words.
# If a player submits a word that has already been used, they are eliminated from the round.
# Elimination continues until only one player remains, who is declared the winner of that round.
# Scoring:
# Players earn points based on how many rounds they survive. The longer you stay in the game, the more points you accumulate.


#Distinguish who wins and who plays
