def fatorial (num, show=False):
    if show:
        if num == 1:
            print(f"{num}", end=" = ")
            return num
        print(f"{num}", end=" x ")
        return num * fatorial(num-1, show)

    if num == 1:
        return num
    return num * fatorial(num-1, show)

print(fatorial(5, True))