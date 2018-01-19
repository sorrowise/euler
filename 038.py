# ans = 932718654, time cost = 968 µs
# see link: http://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/

def is_pandgit(x):
    pandgit_set = {int(x) for x in str(x)}
    if pandgit_set == set(range(1,len(str(x))+1)):
        return True
    return False

def main():
    for p in range(9487,9233,-1):
        con = int(str(p) + str(p*2))
        if is_pandgit(con):
            return con
