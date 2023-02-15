# from oop import Number
import oop
from test import test



def main():
    result = ""
    # choice = input("what to calc? bis or rijk")
    choice = "1"
    print(choice)
    if choice == '1':
        print("We are calculating BIS")
        oop.calc_bis()
    elif choice == '2':
        print("We are calculating ISNZ")
        oop.calc_isnz()

if __name__ == '__main__':
    main()
