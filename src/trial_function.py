import re


def say_hi(name: str) -> str:
    if not isinstance(name, str):
        return "Uh-oh! I can only use strings."
    name = name.strip()
    if re.fullmatch(r"[-'’A-Za-z ]+", name):
        return f'Well, hi, {name}! Nice to meet you!'
    return "Sorry, seems like I can't understand you :("

