HELLO = "Hello, world!"
LYRICS = [
    "99 bottles of beer on the wall, 99 bottles of beer.",
    "Take one down and pass it around, 98 bottles of beer on the wall.",
    "98 bottles of beer on the wall, 98 bottles of beer.",
    "Take one down and pass it around, 97 bottles of beer on the wall.",
    "97 bottles of beer on the wall, 97 bottles of beer.",
    "Take one down and pass it around, 96 bottles of beer on the wall.",
]


def solve(N: int, X: list[str]):
    # process the text to find a predicted minimal program and predicted quine
    predicted_program = []
    predicted_quine = None
    i = 0
    while i < N:
        if X[i] == HELLO: # is it the output of an H?
            predicted_program.append('H')
            i += 1
        elif X[i:i + 6] == LYRICS: # is it the output of a 9?
            predicted_program.append('9')
            i += 6
        elif all(c in 'HQ9+' for c in X[i]): # if not H or 9, must be a Q
            predicted_program.append('Q')
            if predicted_quine == None: # if this is the first Q, record it
                predicted_quine = X[i]
            else: # otherwise, verify consistency with prior Qs
                if X[i] != predicted_quine:
                    return 'IMPOSSIBLE'
            i += 1
        else:
            return 'IMPOSSIBLE'
    predicted_program = ''.join(predicted_program)
    
    # if a quine was found, verify its correctness with the predicted program
    if predicted_quine != None:
        if predicted_quine.replace('+', '') != predicted_program:
            return 'IMPOSSIBLE'
        predicted_program = predicted_quine
    
    return predicted_program


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = [input() for _ in range(N)]
        print(solve(N, X))


if __name__ == '__main__':
    main()
