from typing import List


def find_biggest_name(names: List[str]) -> str:
    big = ""
    for name in names:
        if len(name) > len(big):
            big = name
    return big
