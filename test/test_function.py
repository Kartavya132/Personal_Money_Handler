import pandas as pd

import func.function as fnf
from func import data as dt


def test_load_data_uses_account_csv_and_add_acc_saves_new_account(
    tmp_path, monkeypatch
):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    (data_dir / "account.csv").write_text(
        "ID,acc,name,password,profession,total_m\n",
        encoding="utf-8",
    )
    (data_dir / "money.csv").write_text("name\nKartavya\n", encoding="utf-8")
    (data_dir / "target.csv").write_text("", encoding="utf-8")

    monkeypatch.setattr(dt, "DATA_DIR", data_dir)
    monkeypatch.setattr(
        fnf,
        "acc_data",
        pd.DataFrame(
            columns=["ID", "acc", "name", "password", "profession", "total_m"]
        ),
    )
    monkeypatch.setattr(fnf, "money_data", pd.DataFrame())
    monkeypatch.setattr(fnf, "target_data", pd.DataFrame())

    answers = iter(["Alice", "secret", "secret", "Engineer", "1000"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    acc_data, money_data, target_data = fnf.load()

    assert "acc" in acc_data.columns
    fnf.add_acc()

    saved_accounts = pd.read_csv(data_dir / "account.csv")
    assert len(saved_accounts) == 1
    assert saved_accounts.iloc[0]["name"] == "Alice"


def test_changing_total_updates_account_and_money_steps(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setattr(dt, "DATA_DIR", data_dir)
    fnf.acc_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "name": "Alice",
                "password": "secret",
                "profession": "Engineer",
                "total_m": 1000,
                "created_on": "2026-01-01",
                "steps": 1,
            }
        ]
    )
    fnf.money_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "type": "total",
                "date": "2026-01-01",
                "steps": 1,
                "ammount": 1000,
            }
        ]
    )
    fnf.current_acc = "A01"
    answers = iter(["total_m", "1500"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    fnf.chan_acc()

    saved_accounts = pd.read_csv(data_dir / "account.csv")
    saved_money = pd.read_csv(data_dir / "money.csv")
    assert saved_accounts.iloc[0]["total_m"] == 1500
    assert saved_accounts.iloc[0]["steps"] == 2
    assert saved_money.iloc[-1]["steps"] == 2
    assert saved_money.iloc[-1]["ammount"] == 1500


def test_edit_total_money_updates_account_and_history(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setattr(dt, "DATA_DIR", data_dir)
    fnf.acc_data = pd.DataFrame(
        [{"ID": 1, "acc": "A01", "name": "Alice", "password": "secret", "profession": "Engineer", "total_m": 1000, "created_on": "2026-01-01", "steps": 1}]
    )
    fnf.money_data = pd.DataFrame(
        [{"ID": 1, "acc": "A01", "type": "total", "date": "2026-01-01", "steps": 1, "ammount": 1000}]
    )
    fnf.current_acc = "A01"
    monkeypatch.setattr("builtins.input", lambda prompt="": "1500")

    fnf.edit_total_money()

    saved_accounts = pd.read_csv(data_dir / "account.csv")
    saved_money = pd.read_csv(data_dir / "money.csv")
    assert saved_accounts.iloc[0]["total_m"] == 1500
    assert saved_money.iloc[-1]["steps"] == 2


def test_changing_name_does_not_increase_steps(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setattr(dt, "DATA_DIR", data_dir)
    fnf.acc_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "name": "Alice",
                "password": "secret",
                "profession": "Engineer",
                "total_m": 1000,
                "created_on": "2026-01-01",
                "steps": 1,
            }
        ]
    )
    fnf.money_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "type": "total",
                "date": "2026-01-01",
                "steps": 1,
                "ammount": 1000,
            }
        ]
    )
    fnf.current_acc = "A01"
    answers = iter(["name", "Bob"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    fnf.chan_acc()

    saved_accounts = pd.read_csv(data_dir / "account.csv")
    assert saved_accounts.iloc[0]["name"] == "Bob"
    assert saved_accounts.iloc[0]["steps"] == 1


def test_delete_acc_removes_account_and_matching_money_rows(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setattr(dt, "DATA_DIR", data_dir)
    fnf.acc_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "name": "Alice",
                "password": "secret",
                "profession": "Engineer",
                "total_m": 1000,
                "created_on": "2026-01-01",
                "steps": 1,
            }
        ]
    )
    fnf.money_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "type": "total",
                "date": "2026-01-01",
                "steps": 1,
                "ammount": 1000,
            },
            {
                "ID": 2,
                "acc": "A02",
                "type": "total",
                "date": "2026-01-02",
                "steps": 1,
                "ammount": 2000,
            },
        ]
    )
    fnf.current_acc = "A01"
    answers = iter(["yes", "secret"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    fnf.delete_acc()

    saved_accounts = pd.read_csv(data_dir / "account.csv")
    saved_money = pd.read_csv(data_dir / "money.csv")
    assert saved_accounts.empty
    assert len(saved_money) == 1
    assert saved_money.iloc[0]["acc"] == "A02"


def test_delete_entry_removes_only_current_accounts_money_rows(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setattr(dt, "DATA_DIR", data_dir)
    fnf.acc_data = pd.DataFrame(
        [
            {
                "ID": 1,
                "acc": "A01",
                "name": "Alice",
                "password": "secret",
                "profession": "Engineer",
                "total_m": 1000,
                "created_on": "2026-01-01",
                "steps": 1,
            }
        ]
    )
    fnf.money_data = pd.DataFrame(
        [
            {"ID": 1, "acc": "A01", "type": "total", "date": "2026-01-01", "steps": 1, "ammount": 1000},
            {"ID": 2, "acc": "A02", "type": "total", "date": "2026-01-02", "steps": 1, "ammount": 2000},
        ]
    )
    fnf.current_acc = "A01"
    answers = iter(["yes", "secret"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    fnf.delete_entry()

    saved_money = pd.read_csv(data_dir / "money.csv")
    assert len(saved_money) == 1
    assert saved_money.iloc[0]["acc"] == "A02"
