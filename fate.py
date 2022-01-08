import random

ladder = {
    'legendary': 8,
    'epic': 7,
    'fantastic': 6,
    'superb': 5,
    'great': 4,
    'good': 3,
    'fair': 2,
    'average': 1,
    'mediocre': 0,
    'poor': -1,
    'terrible': -2,
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
