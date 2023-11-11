def diagonalSum(mat):
    elements = []
    length = len(mat)
    if length==1:
        return mat[0][0]
    for i in range(length):
        if i!=length-1-i:
            elements.append(mat[i][i])
            elements.append(mat[i][length-1-i])
    if length%2!=0:
        elements.append(mat[length//2][length//2])

    sumation = sum(elements)
    return sumation

result = diagonalSum([[1,2,3],
    [4,5,6],
    [7,8,9]])

print(result)