from __init__ import *


def main_prompts(*args):
    try:
        prompt = args[0].lower()
    except:
        print("Please Enter proper input")
    if (
        ("add" in prompt and "account" in prompt)
        or ("make" in prompt and "account" in prompt)
        or ("new" in prompt and "account" in prompt)
        or ("add" in prompt and "new" in prompt)
    ):
        pass

    elif (
        ("account" in prompt and "detail" in prompt)
        or ("view" in prompt and "account" in prompt)
        or ("check" in prompt and "account" in prompt)
    ):
        pass

    elif (
        ("add" in prompt and "salary" in prompt)
        or ("new" in prompt and "salary" in prompt)
        or ("add" in prompt and "income" in prompt)
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
        pass

    elif (
        ("change" in prompt and "account" in prompt)
        or ("renew" in prompt and "account" in prompt)
        or ("edit" in prompt and "account" in prompt)
        or ("edit" in prompt)
    ):
        pass

    elif "exit" in prompt or "out" in prompt:
        pass

    else:
        pass
