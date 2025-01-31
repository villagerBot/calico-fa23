def solve(N: int, K: int) -> int:
    deck = list(range(1, N + 1))
    
    for i in range(N):
        card = deck.pop(i)
        deck.append(card)
    
    return deck.index(K) + 1


def main():
    T = int(input())
    for _ in range(T):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        print(solve(N, K))


if __name__ == '__main__':
    main()
