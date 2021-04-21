def hotel_cost(nights):
    return 140 * nights


print(hotel_cost(4))


def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return


print(plane_ride_cost("Cape Town"))
print(plane_ride_cost("JHB"))
print(plane_ride_cost("Durban"))


def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days


print(rental_car_cost(7))


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


location = (input("where did you go: "))
days = int(input("How many days did you stay: "))
extras = float(input("How much was your spending money: "))

print(trip_cost(location, days, extras))
