# rotating the matrix by 90 degree
# logic: if looked at the patterns, we can do by rotating squares and iterating thru each square

# catch: no of loops based on the square
# while rotating the inner decreases

def rotate(matrix):
    if matrix and len(matrix)>1:
        dim=len(matrix)
        # print(dim)
        loops = dim//2
        # print(loops)
        for i in range(loops):
            start_i= start_j = i # starting at the top corner left of the square
            print("i",i)
            for j in range(i,dim-(i+1)):
                print("j",j)
                top_i, top_j = i,j
                right_i, right_j= top_j, dim-1-top_i # as i doesnt change we will have the row/col respective doesn't change
                bottom_i, bottom_j= right_j, dim-1-right_i
                left_i, left_j= bottom_j, dim-1-bottom_i
                matrix[right_i][right_j], matrix[bottom_i][bottom_j], matrix[left_i][left_j], matrix[top_i][top_j] =matrix[top_i][top_j], matrix[right_i][right_j], matrix[bottom_i][bottom_j], matrix[left_i][left_j]
    return matrix

# print(rotate([1]))

# for i in range(0,5):
#     print(i)


# TIME: O(MN)

def rotate_matrix(A):
    A.reverse()
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]