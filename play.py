from math import *
def pattern(n):
    k = 1
    for i in range(1,n+1):
        for j in range(n,n-i+1,-1):
            print(j,end="")
        for j in range(k,2*n):
            print(n-i+1,end="")
        k+=2
        for j in range(n-i+2,n+1):
            print(j,end="")
        print("\n")
    l = 2*n-3
    for i in range(1,n+1):
        for j in range(n,i,-1):
            print(j,end="")
        if l==-1:
            break
        for j in range(l,2*n-2):
            print(i+1,end="")
        l-=2
        for j in range(i+1,n+1):
            print(j,end="")
        print("\n")
def pattern2(n):
    digit = int(log10(n))+1
    for i in range(digit):
        print(n,end="")
        n = floor(n/10)
        print("\n")
def print_board(n):
    board = [[0 for i in range(n)] for j in range(n)]
    left = 0
    top = n-1
    N = 1
    for i in range(int(n/2)):
        for j in range(left,top+1):
            board[left][j] = N
            N=N+1
        for j in range(left+1,top+1):
            board[j][top] = N
            N+=1
        for j in range(top-1,left-1,-1):
            board[top][j] = N
            N+=1
        for j in range(top-1,left,-1):
            board[j][left] = N
            N+=1
        left+=1
        top-=1
    for i in range(n):
        for j in range(n):
            print("{:<5}".format(board[i][j]),end="")
        print("\n")
def pattern3(n):
    k = 1
    for i in range(1,2*n):
        for j in range(1,2*n):
            if j == i or j == 2*n - i:
                print(k,end="")
            else:
                print(" ",end="")
        if i < n:
            k+=1
        else:
            k-=1
        print("\n")
pattern(5)
pattern2(345234)
print_board(5)
pattern3(5)




