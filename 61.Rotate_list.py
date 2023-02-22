n,m=map(int, input().split())
cost=list(map(int, input().split()))
cost.sort()
toys=[]
for i in range(m):
    toys.append(input())
my_dict={}
for i in range(m):
    if toys[i] in my_dict:
        my_dict[toys[i]]+=1
    else:
        my_dict[toys[i]]=1
counter=list(my_dict.values())
counter.sort(reverse=True)
j=i=0
min_cost=0
max_cost=0
while j < m:
    min_cost+=(cost[i] * counter[i])
    max_cost+=(cost[n-1-i] * counter[i])
    j+=counter[i]
    i+=1
print(min_cost,max_cost)
