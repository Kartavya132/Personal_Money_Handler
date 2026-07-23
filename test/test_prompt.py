import pytest

from func import prompt


def test_delete_account_prompt_calls_delete_acc(monkeypatch):
    called = []
    monkeypatch.setattr(prompt.fnf, "delete_acc", lambda: called.append(True))

    prompt.main_prompts("delete my account")

    assert called == [True]


def test_delete_entry_prompt_calls_delete_entry(monkeypatch):
    called = []
    monkeypatch.setattr(prompt.fnf, "delete_entry", lambda: called.append(True))

    prompt.main_prompts("delete my entry")

    assert called == [True]


def test_edit_total_prompt_calls_edit_total_money(monkeypatch):
    called = []
    monkeypatch.setattr(prompt.fnf, "edit_total_money", lambda: called.append(True))

    prompt.main_prompts("edit total amount")

    assert called == [True]


def test_edit_prompt_calls_chan_acc(monkeypatch):
    called = []
    monkeypatch.setattr(prompt.fnf, "chan_acc", lambda: called.append(True))

    prompt.main_prompts("edit account")

    assert called == [True]


def test_exit_prompt_exits(capsys):
    with pytest.raises(SystemExit):
        prompt.main_prompts("exit")

    assert "Good Bye" in capsys.readouterr().out
