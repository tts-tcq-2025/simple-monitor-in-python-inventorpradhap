
def battery_is_ok(temperature, soc, charge_rate):
if temperature < 0 or temperature > 45:
        return False, 'Temperature is out of range!'
    if soc < 20 or soc > 80:
        return False, 'State of Charge is out of range!'
    if charge_rate > 0.8:
        return False, 'Charge rate is out of range!'

    return True, 'Battery is okay.'

if __name__ == '__main__':
    # Test cases
    test_cases = [
        (25, 70, 0.7),  # Expected: (True, 'Battery is okay.')
        (50, 85, 0),    # Expected: (False, 'Temperature is out of range!')
        (25, 10, 0.7),  # Expected: (False, 'State of Charge is out of range!')
        (25, 70, 0.9),   # Expected: (False, 'Charge rate is out of range!')
    ]

    for temp, soc, rate in test_cases:
        result, message = battery_is_ok(temp, soc, rate)
        print('Testing with Temp: {temp}, SOC: {soc}, Charge Rate: {rate} -> Result: {result}, Message: "{message}"')
