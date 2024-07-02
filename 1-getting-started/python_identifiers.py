'''
Exercise: Python Identifiers

This script demonstrates Python identifiers and naming conventions.

Usage:
    Call the main function to demonstrate the usage of identifiers.

Tags: identifiers, variable naming, Python basics
'''


def main():
    '''Demonstrate various uses of Python identifiers.'''
    # Variable assignment using a valid identifier
    my_variable = 42
    print(my_variable)  # Utilize the variable to avoid F841

    # Function definition using a valid identifier
    def my_function(x):
        return x ** 2

    # Call the function to avoid F841
    result = my_function(5)
    print(result)

    # Class definition using a valid identifier
    MyClass = type('MyClass', (), {})
    print(MyClass)  # Utilize the class to avoid F841


if __name__ == '__main__':
    main()
