from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)


# average ratings finder
ratings = []
for each_row in apps_data[1:]:
    rating = float(each_row[7])
    ratings.append(rating)

avg_ratings = sum(ratings)/len(ratings)
print(avg_ratings)


# opened_file = open('AppleStore.csv')
# from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    price = float(row[4])

    if price == 0.0:
        free_apps_ratings.append(rating)


avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)
