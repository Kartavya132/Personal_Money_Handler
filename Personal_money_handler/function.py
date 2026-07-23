import datetime
import random
import pandas as pd
from . import data as dt

acc_data = dt.empty_frame(dt.ACCOUNT_COLUMNS)
money_data = dt.empty_frame(dt.MONEY_COLUMNS)
target_data = dt.empty_frame()
current_acc = None


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
    if not isinstance(money_data, pd.DataFrame):
        money_data = dt.empty_frame(dt.MONEY_COLUMNS)

    for column in dt.ACCOUNT_COLUMNS:
        if column not in acc_data.columns:
            acc_data[column] = pd.Series(dtype="object")
    for column in dt.MONEY_COLUMNS:
        if column not in money_data.columns:
            money_data[column] = pd.Series(dtype="object")

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
    global acc_data, money_data, current_acc
    if current_acc is None:
        print("Sign in to an account before changing it")
        return acc_data

    account_mask = acc_data["acc"].astype(str) == str(current_acc)
    if not account_mask.any():
        print("Account not found")
        return acc_data

    checks = (
        input("Enter what you want to change (name/password/profession/total_m) :- ")
        .strip()
        .lower()
    )

    if checks == "name":
        name = input("Enter other name : ").strip()
        while not name:
            name = input("Enter your proper name : ").strip()
        column, value = "name", name
    elif checks == "password":
        while True:
            password = input("Enter what new password you want : ")
            confirm_password = input("Retype the new password : ")
            if password == confirm_password:
                break
            print("Incorrect password")
        column, value = "password", password
    elif checks == "profession":
        while True:
            prof = input("Enter your profession : ")
            if prof:
                break
            print("Enter the valid value.")
        column, value = "profession", prof
    elif checks in {"total_m", "total", "amount", "ammount"}:
        while True:
            try:
                total_ammount = int(input("Enter the total ammount of money : "))
                if not total_ammount:
                    total_ammount = 100
                break
            except ValueError:
                print("Enter the integer")
        column, value = "total_m", total_ammount
    else:
        print("Enter name, password, profession, or total_m")
        return acc_data

    row_index = acc_data.index[account_mask][0]
    acc_data.loc[row_index, column] = value

    if column == "total_m":
        current_step = pd.to_numeric(acc_data.loc[row_index, "steps"], errors="coerce")
        next_step = int(current_step) + 1 if pd.notna(current_step) else 1
        acc_data.loc[row_index, "steps"] = next_step
        dt.save_account(acc_data)
        for money_column in dt.MONEY_COLUMNS:
            if money_column not in money_data.columns:
                money_data[money_column] = pd.Series(dtype="object")
        money_data.loc[len(money_data)] = {
            "ID": len(money_data) + 1,
            "acc": current_acc,
            "type": "total",
            "date": datetime.datetime.now(),
            "steps": next_step,
            "ammount": value,
        }
        dt.save_money(money_data)
    else:
        dt.save_account(acc_data)

    print("Account updated")
    return acc_data


def delete_acc():
    global current_acc, acc_data, money_data
    if current_acc is None:
        print("Sign in to an account before changing it")
        return acc_data

    if "acc" not in acc_data.columns:
        print("Account not found")
        return acc_data

    account_mask = acc_data["acc"].astype(str) == str(current_acc)
    if not account_mask.any():
        print("Account not found")
        return acc_data

    choice = input("Do you want to Delete : ")

    if "yes" in choice or "yaah" in choice or "probably" in choice:
        ch_pass = input("Enter your password : ")
        saved_password = acc_data.loc[account_mask, "password"].values[0]
        if ch_pass == saved_password:
            acc_data = acc_data.loc[~account_mask].reset_index(drop=True)
            if "acc" in money_data.columns:
                money_mask = money_data["acc"].astype(str) == str(current_acc)
                money_data = money_data.loc[~money_mask].reset_index(drop=True)
            dt.save_account(acc_data)
            dt.save_money(money_data)
            current_acc = None
            print("Account entry both are deleted deleted")
        else:
            print("Incorrect password")
    else:
        print("Account not deleted")

    return acc_data


if __name__ == "__main__":
    print("OOPS came in wrong file!!\nGo to main.py to run the program")
    exit()
