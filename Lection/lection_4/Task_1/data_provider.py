from random import randint


def get_temperature(sensor):
    return randint(0, 20) if sensor else randint(-20, 0)


def get_preassure(sensor):
    return randint(720, 750) if sensor else randint(750, 770)


def get_wind_speed(sensor):
    return randint(0, 10) if sensor else randint(10, 30)
