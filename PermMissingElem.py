def solution(A):
    A.sort()
    count = 0
    if A == []:
        return 1
    for x in A:
        count += 1
        if x > count:
            return count
        elif x < count:
            return x



print(solution([4,5,3,6,7,8,2,1,9,10,3]))




