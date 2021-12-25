# Enter your code here. Read input from STDIN. Print output to STDOUT

happiness = 0
    
n, m = map(int, input().strip().split(' '))  # for input line - 1
arr = list(map(int, input().strip().split(' '))) # for input line - 2
A = set(map(int, input().strip().split(' '))) # for input line - 3
B = set(map(int, input().strip().split(' '))) # for input line - 4
    
for i in arr:
    if i in A:
        happiness = happiness + 1

    elif i in B :
        happiness = happiness - 1 
            
print (happiness)
