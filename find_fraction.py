#분수찾기
import sys
X = int(sys.stdin.readline())
sum = 0
cnt = 0
while X > sum:
    cnt+=1
    sum+=cnt
print("누적 합:",sum,"   ",cnt,"번째")
if cnt%2==0:  # 카운트가 짝수
    top=cnt-(sum-X)
    
else: #카운트가 홀수
    
        