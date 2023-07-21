def mat_pro(matrix,A):
    result=[]
    for i in range(r):
        lst = []
        for j in range(c):
            lst.append(matrix[i][j]*A)
        result.append(lst)
    return result

matrix=[]
A=int(input())
r,c=map(int,input().split())
for i in range(r):
    row=[]
    for j in range(c):
        element=int(input(f'{i},{j}:'))
        row.append(element)
    matrix.append(row)
print(mat_pro(matrix,A))