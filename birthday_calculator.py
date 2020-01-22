from functools import wraps
from math import factorial


def convert_to_percent(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        probability = f(*args, **kwargs)
        return f'{round(probability * 100, 3)}%'

    return decorated


@convert_to_percent
def birthday_probability(people: int, days_range=0, year_days=365) -> float:
    if year_days < people:
        return 1
    numerator = factorial(year_days - people * days_range - 1)
    denominator = year_days ** (people - 1) * factorial(
        year_days - people * (days_range + 1)
    )
    probability = 1 - numerator / denominator
    return probability


if __name__ == "__main__":
    print(
        '\n', birthday_probability(23),
        '\n', birthday_probability(14, days_range=1),
        '\n', birthday_probability(11, days_range=2),
        '\n', birthday_probability(9, days_range=3),
        '\n', birthday_probability(8, days_range=4),
    )
