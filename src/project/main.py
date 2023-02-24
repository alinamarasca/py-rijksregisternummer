import calc_functions as c
from landline import gen_landline


def main():
    choice = input('''
    1. BIS
    2. ISNZ
    3. Phone number
    
    ''')
    print
    if choice == '1':
        print("We are generating BIS")
        result = c.calc_bis()
        print(f"Rijkerigsternummer is: {result}")
    elif choice == '2':
        print("We are generating ISNZ")
        result = c.calc_isnz()
        print(f"Rijkerigsternummer is: {result}")
    elif choice == '3':
        print("We are generating Belgian mobile phone number")
        result = gen_landline()
        print(f"Phone number is: {result}")


if __name__ == '__main__':
    main()
