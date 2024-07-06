'''
Exercise: Weather Classification

This script classifies weather conditions as sunny, rainy, cloudy, snowy,
etc., based on temperature, humidity, and precipitation.

Usage:
    Call the function with temperature, humidity, and precipitation values.

Tags: if-elif-else, weather, classification
'''


def main():
    '''Classify the weather conditions.'''
    temperature = float(input('Enter the temperature in degrees Celsius: '))
    humidity = float(input('Enter the humidity percentage: '))
    precipitation = float(input('Enter the precipitation in millimeters: '))
    classification = classify_weather(temperature, humidity, precipitation)
    print(f'The weather is classified as: {classification}')


def classify_weather(temperature, humidity, precipitation):
    '''
    Classify weather conditions.

    Parameters:
        temperature (float): The temperature in degrees Celsius.
        humidity (float): The humidity percentage.
        precipitation (float): The precipitation in millimeters.

    Returns:
        str: The weather classification (sunny, rainy, cloudy, snowy).
    '''
    if precipitation > 0:
        if temperature < 0:
            return 'Snowy'
        else:
            return 'Rainy'
    elif humidity > 70:
        return 'Cloudy'
    else:
        return 'Sunny'


if __name__ == '__main__':
    main()
