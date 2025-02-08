import re

regex_integer_in_range = (
    r"^[1-9][0-9]{5}$"  # Ensures a 6-digit number in the range 100000-999999
)
regex_alternating_repetitive_digit_pair = (
    r"(\d)(?=\d\1)"  # Detects alternating repetitive digit pairs
)

P = input()
print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
