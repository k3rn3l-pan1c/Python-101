def hotel_cost(nights):
    cost = 140
    return cost * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return None

def rental_car_cost(days):
    cost = 40
    if days >= 7:
        return cost*days - 50
    elif days >= 3:
        return cost*days - 20
    else:
        return cost*days

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Los Angeles", 5, 600)
