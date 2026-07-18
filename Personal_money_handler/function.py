import datetime
import random

import pandas as pd

from . import data as dt

acc_data = dt.empty_frame(dt.ACCOUNT_COLUMNS)
money_data = dt.empty_frame()
target_data = dt.empty_frame()


def load():
    global acc_data, money_data, target_data
    acc_data, money_data, target_data = dt.load_data()
    return acc_data, money_data, target_data


def add_acc():
    global acc_data
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
        "steps": 0,
    }
    dt.save_account(acc_data)
    print(f"Your account no. ::- {acc}")
    return acc_data


def chan_acc():
    global acc_data
    if acc_data.empty:
        print("No account found")
        return acc_data

    target_acc = input("Enter account no. to change : ").strip()
    row = acc_data[acc_data["acc"].astype(str) == target_acc]
    if row.empty:
        print("Account not found")
        return acc_data

    field = (
        input("Enter field to change (name/password/profession/total_m) : ")
        .strip()
        .lower()
    )
    mapping = {
        "name": "name",
        "password": "password",
        "profession": "profession",
        "total_m": "total_m",
    }
    if field not in mapping:
        print("Wrong field")
        return acc_data

    value = input(f"Enter new {field} : ")
    if field == "total_m":
        try:
            value = int(value)
        except ValueError:
            print("Enter the integer")
            return acc_data

    acc_data.loc[row.index[0], mapping[field]] = value
    dt.save_account(acc_data)
    print("Account updated")
    return acc_data


def inp_salary():
    pass


def salary_track():
    pass


def show_sal_plot():
    pass


def inp_ex():
    pass


def ex_track():
    pass


def show_ex_plot():
    pass


def give_saving():
    pass


def advice():
    pass


def show_combine_plot():
    pass


def total_ammount():
    pass


def total_track():
    pass


def show_total_plot():
    pass


if __name__ == "__main__":
    print("OOPS came in wrong file!!\nGo to main.py to run the program")
    exit()
