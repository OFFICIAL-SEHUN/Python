import sys
n=sys.stdin.readline().upper().rstrip() #str
tmp=list(set(n)) # 중복제거 ['Q','R','S']
num_lst=[]
for i in tmp:
    num_lst.append(n.count(i)) #append를 써야하는이유 (리스트에 숫자를 넣어도 list 자료형유지
if num_lst.count(max(num_lst))>1: # >  count는 문자열써야함
    print("?")
else:
    print(n[num_lst.index(max(num_lst))])
