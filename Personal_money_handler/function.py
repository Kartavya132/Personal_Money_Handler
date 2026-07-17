import json
import pandas as pd
from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_data():
    global acc_data, money_data, target_data

    acc_path = DATA_DIR / "account.json"
    money_path = DATA_DIR / "money.csv"
    target_path = DATA_DIR / "target.csv"

    if acc_path.exists() and acc_path.stat().st_size > 0:
        acc_data = pd.read_csv(money_path)
    else:
        acc_data = pd.DataFrame()
    if money_path.exists() and money_path.stat().st_size > 0:
        money_data = pd.read_csv(money_path)
    else:
        money_data = pd.DataFrame()
    if target_path.exists() and target_path.stat().st_size > 0:
        target_data = pd.read_csv(target_path)
    else:
        target_data = pd.DataFrame()


def add_acc():
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars += chars.upper()
    acc = random.choices(chars, 2) + random.randint(0, 9)
    while not acc in acc_data["acc"]:
        acc = random.choices(chars, 2) + random.randint(0, 9)
    name = input("Enter your name : ").strip()
    while not name:
        name = input("Enter your proper name : ").strip()
    while True:
        password = input("Enter what password you want : ")
        if password == input("Retype the password : "):
            break
        else:
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
