import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

ACCOUNT_COLUMNS = [
    "ID",
    "acc",
    "name",
    "password",
    "profession",
    "total_m",
    "created_on",
    "steps",
]
MONEY_COLUMNS = ["ID", "acc", "type", "date", "steps", "ammount"]


def empty_frame(columns=None):
    return pd.DataFrame(columns=columns or [])


def load_csv(path, columns=None):
    if path.exists() and path.stat().st_size > 0:
        frame = pd.read_csv(path)
        if columns:
            for column in columns:
                if column not in frame.columns:
                    frame[column] = pd.Series(dtype="object")
        return frame
    return empty_frame(columns)


def load_data():
    return (
        load_csv(DATA_DIR / "account.csv", ACCOUNT_COLUMNS),
        load_csv(DATA_DIR / "money.csv", MONEY_COLUMNS),
        load_csv(DATA_DIR / "target.csv"),
    )


def save_csv(name, frame):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = DATA_DIR / f"{name}.csv"
    frame.to_csv(path, index=False)
    return path


def save_account(frame):
    return save_csv("account", frame)


def save_money(frame):
    return save_csv("money", frame)


def save_target(frame):
    return save_csv("target", frame)


if __name__ == "__main__":
    print("OOPS came in wrong place!!\nGo to main.py")
    exit()
