def battery_is_ok(temperature, soc, charge_rate):
    if not (0 <= temperature <= 45):
        return False
    if not (20 <= soc <= 80):
        return False
    if charge_rate > 0.8:
        return False
    return True

def test_battery_is_ok():
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
    assert battery_is_ok(-1, 50, 0.5) is False
    assert battery_is_ok(25, 10, 0.7) is False
    assert battery_is_ok(25, 70, 0.9) is False
    print("All tests passed!")

if __name__ == '__main__':
    test_battery_is_ok()
