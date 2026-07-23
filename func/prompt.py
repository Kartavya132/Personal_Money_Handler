import sys
from . import function as fnf


def main_prompts(prompt):
    prompt = prompt.lower()
    if "exit" in prompt or "out" in prompt:
        print("Thank you for using us!!\nGood Bye!!")
        sys.exit()

    elif (
        ("account" in prompt and "detail" in prompt)
        or ("see" in prompt and "account" in prompt)
        or ("view" in prompt and "account" in prompt)
        or ("check" in prompt and "account" in prompt)
    ):
        pass

    elif (
        ("add" in prompt and "salary" in prompt)
        or ("new" in prompt and "salary" in prompt)
        or ("add" in prompt and "income" in prompt)
        or ("save" in prompt and "salary" in prompt)
        or ("save" in prompt and "income" in prompt)
        or ("renew" in prompt and "income" in prompt)
        or ("renew" in prompt and "salary" in prompt)
    ):
        pass

    elif (
        ("graph" in prompt)
        or ("plot" in prompt)
        or ("chart" in prompt)
        or ("view" in prompt and "salary" in prompt)
        or ("visualization" in prompt)
    ):
        pass

    elif (
        ("delete" in prompt and "account" in prompt)
        or ("remove" in prompt and "account" in prompt)
        or ("vanish" in prompt and "account" in prompt)
    ):
        fnf.delete_acc()
    elif (
        ("delete" in prompt and "entry" in prompt)
        or ("remove" in prompt and "entry" in prompt)
        or ("vanish" in prompt and "entry" in prompt)
        or ("delete" in prompt and "saves" in prompt)
        or ("remove" in prompt and "saves" in prompt)
        or ("vanish" in prompt and "saves" in prompt)
    ):
        fnf.delete_entry()
    elif (
        (
            "total" in prompt
            and ("amount" in prompt or "ammount" in prompt or "amt" in prompt)
            and "add" in prompt
        )
        or (
            "save" in prompt
            and "total" in prompt
            and ("amount" in prompt or "amt" in prompt)
        )
        or (
            "edit" in prompt
            and "total" in prompt
            and ("amount" in prompt or "ammount" in prompt)
        )
        or ("renew" in prompt and "total" in prompt and "value" in prompt)
        or ("add" in prompt and "total" in prompt and "value" in prompt)
    ):
        fnf.edit_total_money()

    elif (
        ("change" in prompt and "account" in prompt)
        or ("renew" in prompt and "account" in prompt)
        or ("edit" in prompt and "account" in prompt)
        or ("edit" in prompt)
    ):
        fnf.chan_acc()

    elif "goal" in prompt or "target" in prompt:
        pass

    else:
        pass


if __name__ == "__main__":
    print("OOPS came in wrong place!!\nGo to main.py")
    exit()
