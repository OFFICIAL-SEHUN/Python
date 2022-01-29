#손익분기점
import sys
a,b,c=map(int,sys.stdin.readline().split())
def sonic(a,b,c):
    if c<=b:
        print("-1")
        quit()
    res=a//(c-b)
    return res+1

print(sonic(a,b,c))
