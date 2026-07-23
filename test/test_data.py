import pandas as pd

from Personal_money_handler import data


def test_load_csv_returns_requested_columns_for_missing_file(tmp_path):
    frame = data.load_csv(tmp_path / "missing.csv", ["ID", "name"])

    assert frame.empty
    assert frame.columns.tolist() == ["ID", "name"]


def test_save_csv_writes_frame_to_data_directory(tmp_path, monkeypatch):
    monkeypatch.setattr(data, "DATA_DIR", tmp_path)
    frame = pd.DataFrame({"ID": [1], "name": ["Alice"]})

    path = data.save_account(frame)

    assert path == tmp_path / "account.csv"
    assert pd.read_csv(path).to_dict("list") == {"ID": [1], "name": ["Alice"]}
