opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
games_ratings = []
non_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]

    if genre == 'Games':
        games_ratings.append(rating)

    if genre != 'Games':
        non_games_ratings.append(rating)

avg_rating_games = sum(games_ratings)/len(games_ratings)
avg_rating_non_games = sum(non_games_ratings)/len(non_games_ratings)
print(avg_rating_games)
print(avg_rating_non_games)

differences = avg_rating_games - avg_rating_non_games
print(differences)
