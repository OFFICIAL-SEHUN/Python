import sys
n=int(sys.stdin.readline().rstrip()) #n번
group=0
for _ in range(n):
    s1=sys.stdin.readline().rstrip()
    non_group=0
    for index in range(len(s1)-1):
        if s1[index] != s1[index+1]: # index 와 index+1 이 다르다면
            s2 = s1[index+1:] # index+1 이후 새로운 단어
            if s1.count(s2[index]) > 0:
                non_group+=1
    
    if non_group == 0:
            group+=1

print(group)
