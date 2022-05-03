def any_lowercase1(s):
    for c in s:
       if c.islower():
           return True
       else:
           return False
# it only checks the first letter


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# this is always true because the letter c is alwayas lowercase.


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# checks only last letter


# WORKING
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    for c in s:
        if not c.islower():
               return False
    return True


print(any_lowercase1("D"))

