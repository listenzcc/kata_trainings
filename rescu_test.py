# code: utf-8


def myguess(cands, guess):
    print(cands, guess)
    if guess == truth:
        return True
    return any(myguess(cands-{c}, guess.union({c})) for c in cands)


def rescu1(lst, allsubset):
    print(lst)
    allsubset.add(tuple(lst))
    return any(rescu1(lst_, allsubset) for lst_ in list(
        lst[0:j]+lst[j+1:] for j in range(len(lst))))


def rescu2(lst):
    print(lst)
    return max(lst) < 3 and any(rescu2(lst_) for lst_ in list(
        plus(lst, j) for j in range(len(lst))))


def plus(lst, j):
    lstj = lst.copy()
    lstj[j] += 1
    return lstj


truth = {2, 3, 5}
cands = {1, 2, 5, 3, 4}
guess = set()
print(myguess(cands, guess))

lst = list(range(5))
allsubset = set()
rescu1(lst, allsubset)

lst = [0, 0, 0]
rescu2(lst)
