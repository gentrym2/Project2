"""
The purpose of the project is to identify the best route possible through 5 Arizona cities,
with the requirements: the highest average temperature and a max hotel budget of $850.

author: Mackenna Gentry
email: gentrym2@my.erau.edu
version: 1.0
"""

from itertools import combinations_with_replacement, permutations

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriot": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

days = len(list(city_temps.keys()))
perms = list(permutations(city_temps.keys(), days))


def cost_route(routes):
    """
    :param routes: parameter of function requires a tuple; permutation of city names listed in routes
    :return: average temperature of each tuple
    """
    temps_of_route = [city_temps[routes[i]][i] for i in range(len(routes))]
    return sum(temps_of_route) / len(routes)


cities = max(perms, key=lambda m: cost_route(m))


HOTEL_BUDGET = 850
combinations = list(combinations_with_replacement(hotel_rates.keys(), days))


def cost_fun(t):
    """
    :param t: parameter of the function requires a tuple; names of hotels in cities
    :return: sum of hotel pricing for each tuple combination
    """
    return sum(hotel_rates[x] for x in t)


hotels = min(combinations, key=lambda t: HOTEL_BUDGET - cost_fun(t) if HOTEL_BUDGET >= cost_fun(t)
             else HOTEL_BUDGET)


if __name__ == "__main__":
    # final statement containing the route and highest average temperature for that route
    print(f'Here is your best route: {cities} the average of the daily max temp is {cost_route(cities)} degrees F')
    # final statement containing the hotel names and summed pricing
    print(f'To max out your hotel budget stay at these hotels: {hotels} with a sum of ${cost_fun(hotels)}')

