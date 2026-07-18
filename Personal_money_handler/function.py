import pandas as pd
from pathlib import Path
from main import *
import random

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
acc_data = pd.DataFrame(
    columns=["ID", "acc", "name", "password", "profession", "total_m"]
)
money_data = pd.DataFrame()
target_data = pd.DataFrame()


def load_data():
    global acc_data, money_data, target_data

    acc_path = DATA_DIR / "account.csv"
    money_path = DATA_DIR / "money.csv"
    target_path = DATA_DIR / "target.csv"

    if acc_path.exists() and acc_path.stat().st_size > 0:
        acc_data = pd.read_csv(acc_path)
    else:
        acc_data = pd.DataFrame(
            columns=["ID", "acc", "name", "password", "profession", "total_m"]
        )

    if money_path.exists() and money_path.stat().st_size > 0:
        money_data = pd.read_csv(money_path)
    else:
        money_data = pd.DataFrame()

    if target_path.exists() and target_path.stat().st_size > 0:
        target_data = pd.read_csv(target_path)
    else:
        target_data = pd.DataFrame()

    return acc_data, money_data, target_data


def add_acc():
    global acc_data

    if not isinstance(acc_data, pd.DataFrame):
        acc_data = pd.DataFrame(
            columns=["ID", "acc", "name", "password", "profession", "total_m"]
        )

    for column in ["acc", "name", "password", "profession", "total_m"]:
        if column not in acc_data.columns:
            acc_data[column] = pd.Series(dtype="object")

    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += characters.upper()
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
        prof = input("Enter your proffession : ")
        if prof:
            break
        else:
            print("Enter the valid value.")

    while True:
        try:
            total_ammount = int(input("Enter the total ammount of money : "))
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
    }
    acc_path = DATA_DIR / "account.csv"
    acc_data.to_csv(acc_path, index=False)
    print(acc)
    return acc_data


def chan_acc():
    pass


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
