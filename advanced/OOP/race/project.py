from OOP.race.car import Car
from OOP.race.motorcycle import Motorcycle


def race(competitor_1, competitor_2):

    # Important announcements
    print(f"Hello folks! Today, we have a {competitor_1.colour} "
          f"{competitor_1.year} {competitor_1.make} {competitor_1.model} versus a "
          f"{competitor_2.colour} {competitor_2.year} {competitor_2.make} {competitor_2.model}!")

    print('Let the race begin!\n')

    # Assigning each vehicle with their top speed to easily know which vehicle won.
    new_dict = {
        competitor_1: competitor_1.top_speed,
        competitor_2: competitor_2.top_speed
    }

    # Fancy business
    winner_speed = max(new_dict.get(competitor_1), new_dict.get(competitor_2))  # grabs the fastest speed from both vehicles
    winner = list(new_dict.keys())[list(new_dict.values()).index(winner_speed)]  # grabs the object from the value obtained
    loser_speed = min(new_dict.get(competitor_1), new_dict.get(competitor_2))
    loser = list(new_dict.keys())[list(new_dict.values()).index(loser_speed)]  # finding which vehicle loses cuz I need their wheels

    # Results!
    print(f"The winner is..... {winner.make}!\n"
          f"Top speed: {winner_speed} kph\n\n"
          f"It seems {winner.wheels} wheels is better than {loser.wheels}!")


# Creating the vehicles
created_car = Car('Subaru', 'Forester', 2022, 'Army Green', 204)
created_motorcycle = Motorcycle('Harley Davidson', 'Road Glide', 2020, 'Black', 205)

# Race!
race(created_car, created_motorcycle)
