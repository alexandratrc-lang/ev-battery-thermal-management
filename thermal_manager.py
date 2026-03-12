def control_btms(temp_celsius):
    """
    Battery Thermal Management System Logic
    Based on REQ-01 to REQ-05
    """
    if temp_celsius > 60:
        return "CRITICAL_SHUTDOWN"
    elif temp_celsius > 45:
        return "COOLING_ACTIVE"
    elif temp_celsius < 10:
        return "HEATING_ACTIVE"
    else:
        return "IDLE"

# Testing the logic
if __name__ == "__main__":
    test_temps = [5, 25, 50, 65]
    for t in test_temps:
        status = control_btms(t)
        print(f"Temp: {t}°C -> System State: {status}")
