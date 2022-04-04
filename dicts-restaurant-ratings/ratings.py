"""Restaurant rating lister."""
input_file = open("scores.txt")

def read_input():
    restaurant_ratings = {}
    for line in input_file:
        line = line.split(":")
        line[1] = int(line[1])
        restaurant_ratings[line[0]] = line[1]

    return restaurant_ratings

def print_output(restaurant_ratings):
    restaurant_ratings = dict(sorted(restaurant_ratings.items()))

    for key, value in restaurant_ratings.items():
        print (f"{key} is rated at {value}")

def rate_new_restaurant(restaurant_ratings):
    print (" ***** Restaurant ratings *****")
    restaurant_name = input("Please enter the name of the restaurant to rate: ")
    restaurant_name = restaurant_name[0].upper() + restaurant_name[1:]
    restaurant_ratings[restaurant_name] = input(f"Please enter {restaurant_name}'s score: ")


restaurant_ratings = read_input()
print_output(restaurant_ratings)
rate_new_restaurant(restaurant_ratings)
print_output(restaurant_ratings)



