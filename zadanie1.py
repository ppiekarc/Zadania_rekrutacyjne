

def post_code_generator(start: str, end: str) -> list():
    numbers = range(int(start.replace('-', '')), int(end.replace('-', '')))
    codes = list(map(lambda x: str(x)[0:-3] + '-' + str(x)[-3:], numbers))
    return codes


if __name__ == '__main__':
    print(post_code_generator("79-900", "80-155"))
