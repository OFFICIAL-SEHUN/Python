#벌집 
import sys
N=int(sys.stdin.readline())

honey_comb = 1
cnt = 1
while N > honey_comb:
    honey_comb+=6*cnt
    cnt+=1
print(cnt)