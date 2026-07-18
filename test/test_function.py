import pandas as pd

import Personal_money_handler.function as fnf


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

    monkeypatch.setattr(fnf, "DATA_DIR", data_dir)
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

    acc_data, money_data, target_data = fnf.load_data()

    assert "acc" in acc_data.columns
    fnf.add_acc()

    saved_accounts = pd.read_csv(data_dir / "account.csv")
    assert len(saved_accounts) == 1
    assert saved_accounts.iloc[0]["name"] == "Alice"
