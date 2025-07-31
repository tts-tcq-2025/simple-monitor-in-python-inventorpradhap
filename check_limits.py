def check_limit(value, low, high, name):
    if value < low or value > high:
        print(f'{name} is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    for value, low, high, name in [
        (temperature, 0, 45, 'Temperature'),
        (soc, 20, 80, 'State of Charge'),
        (charge_rate, 0, 0.8, 'Charge rate')
    ]:
        if not check_limit(value, low, high, name):
            return False
            break
    return True

if __name__ == '__main__':
    assert(battery_is_ok(4, 21, 1.0) is False)
    assert(battery_is_ok(50, 85, 0) is False)
