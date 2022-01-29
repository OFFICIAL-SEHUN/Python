#호텔 방 배정
import sys
import math
T=int(sys.stdin.readline().rstrip()) # 테스트케이스 개수
room_floor = 0
room_num = 0
for _ in range(T):
    H,W,N = map(int,sys.stdin.readline().split()) #각각 호텔 높이, 방의개수, N번째 손님
    room_floor = (N % H)*100 #300
    if room_floor == 0: room_floor = H*100
    room_num = math.ceil(N / H)#math.ceil(N // H) #25//6 + 1 = 5호
    print(room_floor + room_num)