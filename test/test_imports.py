from abc import ABC

from Personal_money_handler.class_ob import Account, mains


def test_abstract_base_class_imports_cleanly():
    assert issubclass(mains, ABC)
    assert issubclass(Account, mains)
    assert mains.__abstractmethods__ == frozenset(
        {"add_acc", "acc_detail", "add_d", "predict", "plots_build"}
    )
