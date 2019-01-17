# code: utf-8

truth = {2, 3, 5}


def myguess(cands, guess):
    print(cands, guess)
    if guess == truth:
        return True
    return not len(guess) > len(truth) and (
        cands == {} or any(myguess(cands-{c}, guess.union({c})) for c in cands))


cands = {1, 2, 3, 4, 5}
guess = set()
print(myguess(cands, guess))
