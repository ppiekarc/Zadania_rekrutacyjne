
def missing_elements(elements: list(), scope: int) -> list():
    missing = list(range(1, scope + 1))
    for e in elements:
        missing.remove(e)

    return missing


if __name__ == "__main__":
    print(missing_elements([2, 3, 7, 4, 9], 10))
