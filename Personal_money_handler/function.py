import datetime
import random
import pandas as pd
from . import data as dt

acc_data = dt.empty_frame(dt.ACCOUNT_COLUMNS)
money_data = dt.empty_frame(dt.MONEY_COLUMNS)
target_data = dt.empty_frame()


def load():
    global acc_data, money_data, target_data
    acc_data, money_data, target_data = dt.load_data()
    return acc_data, money_data, target_data


def check_acc():
    global acc_data, current_acc
    if acc_data.empty:
        print("There is no account add one")
        return False
    while True:
        acc = input("Enter your account name : ").strip()
        if not acc in {str(value) for value in acc_data["acc"].astype(str).tolist()}:
            print("There is such account")
            return False
        for _ in range(0, 3):
            password = input("Enter the password : ")
            if password == acc_data.loc[acc_data["acc"] == acc, "password"].values[0]:
                current_acc = acc
                return True
            print("Invalid password")
        print("You tried many times")
        return False


def add_acc():
    global acc_data, money_data
    if not isinstance(acc_data, pd.DataFrame):
        acc_data = dt.empty_frame(dt.ACCOUNT_COLUMNS)

    for column in [
        "acc",
        "name",
        "password",
        "profession",
        "total_m",
        "created_on",
        "steps",
    ]:
        if column not in acc_data.columns:
            acc_data[column] = pd.Series(dtype="object")

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc = (
        random.choice(characters)
        + str(random.randint(0, 9))
        + str(random.randint(0, 9))
    )
    existing_accounts = {str(value) for value in acc_data["acc"].astype(str).tolist()}
    while acc in existing_accounts:
        acc = (
            random.choice(characters)
            + str(random.randint(0, 9))
            + str(random.randint(0, 9))
        )

    name = input("Enter your name : ").strip()
    while not name:
        name = input("Enter your proper name : ").strip()

    while True:
        password = input("Enter what password you want : ")
        confirm_password = input("Retype the password : ")
        if password == confirm_password:
            break
        print("Incorrect password")

    while True:
        prof = input("Enter your profession : ")
        if prof:
            break
        print("Enter the valid value.")

    while True:
        try:
            total_ammount = int(input("Enter the total ammount of money : "))
            if not total_ammount:
                total_ammount = 100
            break
        except ValueError:
            print("Enter the integer")

    acc_data.loc[len(acc_data)] = {
        "ID": len(acc_data) + 1,
        "acc": acc,
        "name": name,
        "password": password,
        "profession": prof,
        "total_m": total_ammount,
        "created_on": datetime.datetime.now(),
        "steps": 1,
    }
    dt.save_account(acc_data)
    money_data.loc[len(money_data)] = {
        "ID": len(money_data) + 1,
        "acc": acc,
        "type": "total",
        "date": datetime.datetime.now(),
        "steps": 1,
        "ammount": total_ammount,
    }
    dt.save_money(money_data)
    print(f"Your account no. ::- {acc}")
    return acc_data


def chan_acc():
    global acc_data
    pass


def delete_acc():
    pass


if __name__ == "__main__":
    print("OOPS came in wrong file!!\nGo to main.py to run the program")
    exit()
