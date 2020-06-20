START = 2.0
END = 5.0
JUMP = 0.5


def gen_numbers() -> list():
    i = START
    numbers = list()
    while i <= END:
        numbers.append(i)
        i += 0.5

    return numbers


if __name__ == "__main__":
    print(gen_numbers())
