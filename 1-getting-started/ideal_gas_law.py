'''
Exercise: Ideal Gas Law

This script calculates the amount of gas in moles using the Ideal Gas Law.

Formula:
    PV = nRT --> n = PV / RT
where:
    - P is the pressure of the gas in Pascals
    - V is the volume of the gas in cubic meters
    - n is the amount of gas in moles.
    - R is the ideal gas constant (8.314 J/(mol·K)).
    - T is the temperature of the gas in Kelvin.

Usage:
    Call the function with the pressure, volume, and temperature.

Tags: arithmetic operations, physics, chemistry, ideal gas law
'''


def main():
    '''Main function to calculate the amount of gas in moles using the
    ideal gas law.'''
    pressure, volume, temperature = 101.3, 22.4, 273
    moles = ideal_gas_law(pressure, volume, temperature)
    print(f'The amount of gas is {moles:.4f} moles')


def ideal_gas_law(pressure, volume, temperature):
    '''
    Calculates the amount of gas in moles using the ideal gas law.

    Parameters:
        pressure (float): Pressure in kilopascals.
        volume (float): Volume in liters.
        temperature (float): Temperature in kelvin.

    Returns:
        float: Amount of gas in moles.
    '''
    R = 8.314  # Ideal gas constant in J/(mol·K)
    pressure_pa = pressure * 1000  # kPa to Pa
    volume_m3 = volume / 1000  # liters to cubic meters
    moles = (pressure_pa * volume_m3) / (R * temperature)
    return moles


if __name__ == '__main__':
    main()
