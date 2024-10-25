import keyboard as kb

# Function to convert decimal to hectares
def decimal_to_hectares(dec: float) -> float:
    '''
    # land measurement
    Convert an area from decimal to hectares.
    # The function convert the decimal into hactares.
    This function accepts a int or float value representing an area in decimal
    and returns the equivalent area in hectares.
    # Examples:
    >>> decimal_to_hectares(247.1280)
    >>> 1.0000915339548673
    '''
    if isinstance(dec, int|float):
        return '%.4f' % (dec * 0.0040468564224)
    else:
        print("The function wants int or str but", type(dec), 'is given')
        return -1
    

# User input
def user_input() -> float:
    while True:
        try:
            dec: float = float(input("Enter Decimal = "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            if isinstance(dec, int|float):
                return dec
            else:
                continue

def main() -> None:
    dec: float = user_input()
    
    print("\nHectares =", decimal_to_hectares(dec))

    # Wait unit the user pass the esc key on keybord
    print("\n\tThe program is still runiing until you press the 'Esc' button")
    kb.wait('esc')

# Main function
if __name__ == "__main__":
    main()
