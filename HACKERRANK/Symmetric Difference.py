# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input()) # for line - 1 input
M = list(map(int,input().strip().split(' '))) # for input line-2
n = int(input()) # for input line-3
N= list(map(int,input().strip().split(' '))) # for input line -4

x = list()

for i in (M):
    if i not in N :
        x.append(i)
 

for j in N :
    if j not in M :
        x.append(j)

sort = set(x)
     
new_sort = sorted(sort)


for k in new_sort:
    print(k)
