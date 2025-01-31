def solve() -> None:
    feed(1)
    feed(3)
    feed(2)
    
    num = poop()
    if num == 1: 
        guess("queueon")
    elif num == 3: 
        guess("heapeon")
    else:
        guess("stackeon")


def feed(i: int) -> str:
    print('feed', i, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return response


def poop() -> int:
    print('poop', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return int(response)


def guess(s: str) -> str:
    print('guess', s, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return response


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()
