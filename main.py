def distance_from_zero(distance):
    if type(distance) == int or distance == float:
        return abs(distance)
    else:
        return "Nope"


print(distance_from_zero(-6.8))
