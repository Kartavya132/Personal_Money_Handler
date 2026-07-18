import Personal_money_handler.prompt as pt
import Personal_money_handler.function as fnf
from sys import exit


def main():
    fnf.load_data()
    while True:
        pro = input("Do you have account : ").lower().strip()
        if ("yes" in pro) or ("yaah" in pro) or ("have" in pro and not "not" in pro):
            while True:
                print("\n===============================")
                print("---Welcomce to money handler---")
                print("===============================\n")
                ch = input("What do you want : ")
                pt.main_prompts(ch)
        elif (
            ("no" in pro)
            or ("na" in pro)
            or ("not" in pro and "have" in pro)
            or ("never" in pro)
        ):
            print("\n===============================")
            print("---Welcomce to money handler---")
            print("===============================\n")
            fnf.add_acc()
        elif "exit" in pro or "out" in pro:
            print("Thank you for using us!!\nGood Bye!!")
            exit()
        else:
            print("Enter the proper prompt!!")


if __name__ == "__main__":
    main()
