import pytest

from Personal_money_handler import prompt


def test_delete_account_prompt_calls_delete_acc(monkeypatch):
    called = []
    monkeypatch.setattr(prompt.fnf, "delete_acc", lambda: called.append(True))

    prompt.main_prompts("delete my account")

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
