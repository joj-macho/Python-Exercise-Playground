'''
Exercise: Ideal Gas Law

This script computes the amount of gas in moles when the user supplies
the pressure, volume, and temperature.

Formula Used:
Ideal Gas Law: PV = nRT
where P is the pressure in pascals, V is the volume in cubic meters,
n is the amount of gas in moles, R is the ideal gas constant (8.314 J/(mol·K))
, and T is the temperature in kelvin.

Usage:
    Call the function with the pressure, volume, and temperature.

Tags: arithmetic operations, pressure conversion, volume conversion, moles
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
