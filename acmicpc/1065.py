#1이상 99이하의 정수는 모두 한수라는 것을 생각하고 문제를 풀어보자

def han(n):
    if(n < 100):
        return n
    s = 99
    for i in range(100, n+1):
        if(int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0])):
            s += 1
    return s

a = int(input())
print(han(a))
