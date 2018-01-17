from sympy import sieve

def is_pandgit(x):
    pandgit_set = {int(x) for x in str(x)}
    if pandgit_set == set(range(1,len(str(x))+1)):
        return True
    return False

max([x for x in list(sieve.primerange(1,7654321)) if is_pandgit(x)])
