import sys
sum_people = 0
def cal_people(K,N):
    sum = 0
    for i in range(N):
        sum += i
    if K == 0 : print('')
    else:
        cal_people(K-1,N)
    return sum

for _ in range(int(sys.stdin.readline().rstrip())): # Test_case
    K = int(sys.stdin.readline().rstrip()) # K층
    N = int(sys.stdin.readline().rstrip()) # N호
    print(cal_people(K,N))
    #if K == 0 : # 0층이면 sum_people = N (호) ex) 0층 7호 sum_people = 7
    #   sum_people = N
    