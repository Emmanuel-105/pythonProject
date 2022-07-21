
def solution(A):
    array = []
# create a register of all the available numbers
    for x in A:
        if x not in array:
            array.append(x)
# count the amount of times each number appears in the array
    for x in array:
        if A.count(x)% 2 == 1:
            return x

def solution2(A):
    if (len(A) > 1000000 or len(A) < 1) and len(A) % 2 == 0:
        return "INVALID"
    else:
        for x in A:
            if len(A) > 1000000000 or len(A) < 1:
                return
            if A.count(x) % 2 == 1:
                return x


print(solution2([4,8,9,7,8,9,4,9,7]))
