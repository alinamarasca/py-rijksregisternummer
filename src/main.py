import functions


def main():
    choice = input("what to calc? bis or rijk")
    print(choice)
    if choice == '1':
        print("We are calculating BIS")
        result = functions.calc_bis()
    elif choice == '2':
        print("We are calculating ISNZ")
        result = functions.calc_isnz()
    print(f"Rijkerigsternummer is: {result}")

if __name__ == '__main__':
    main()
