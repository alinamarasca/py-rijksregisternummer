from oop import Number
from test import test



def main():
    result = ""
    choice = input("what to calc? bis or rijk")
    print(choice)
    if choice == '1':
        print("We are calculating BIS")
        Number.calc_bis()
    elif choice == '2':
        print("We are calculating ISNZ")
        Number.calc_isnz()

if __name__ == '__main__':
    main()
