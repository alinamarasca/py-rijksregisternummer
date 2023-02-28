import calc_functions as c
from landline import landline_generate


def main():
    print(list(range(2, 4)) + list(range(9, 16)) + list(range(19, 20)), list(range(50, 71)), list(range(80, 90)))
    choice = input('''
    1. BIS
    2. ISNZ
    3. Phone number
        
    ''')

    if choice == '1':
        print("We are generating BIS")
        result = c.bis_generate()
        print(f"BIS nummer is: {result}")
    elif choice == '2':
        print("We are generating ISNZ")
        result = c.isnz_generate()
        print(f"Rijkerigsternummer is: {result}")

    elif choice == '3':
        print("We are generating a phone number")

        result = landline_generate()
        print(f"Phone number is: {result}")


if __name__ == '__main__':
    main()
