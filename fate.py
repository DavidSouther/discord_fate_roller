import random

ladder = {
    'terrible': -2, 'ter': -2, 't': -2,
    'poor': -1, 'p': -1,
    'mediocre': 0, 'med': 0, 'm': 0,
    'average': 1, 'avg': 1, 'av': 1, 'a': 1,
    'fair': 2, 'f': 2,
    'good': 3, 'go': 3, 'g': 3,
    'great': 4, 'gr': 4,
    'superb': 5, 's': 5,
    'fantastic': 6, 'fan': 6,
    'epic': 7, 'ep': 7, 'e': 7,
    'legendary': 8, 'legend': 8, 'leg': 8, 'l': 8,
}

faces = {
    -1: "-",
    0: "□",
    1: "+",
}


def die():
    return random.choice([-1, 0, 1])


def roll(modifier=0):
    choices = [die(), die(), die(), die()]
    if modifier in ladder:
        modifier = ladder[modifier]
    elif not isinstance(modifier, int):
        modifier = 0
    roll = sum(choices) + modifier
    return (roll, modifier, choices)


def to_str(roll, modifier, choices):
    return f"""[{" ".join([faces[f] for f in choices])}] ({modifier}): {roll}"""

def command(modifier=0):
    if isinstance(modifier, str):
        modifier = modifier.lower().strip()
    if not modifier in ladder:
        try:
            modifier = int(modifier)
        except:
            modifier = 0
    return to_str(*roll(modifier))
