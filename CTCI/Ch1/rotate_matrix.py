"""
Given an image represented by an NxN matrix, where each pixel in the
image is 4 bytes, write a metgid ti ritate tge unage by 90 degrees, Can you
do this in place?
"""

def rotate(matrix):
    size = len(matrix)

    for i in range(int(size/2)):
        for j in range(i, size - i - 1):
            temp = matrix[i][j]

            matrix[i][j] = matrix[j][size - 1 - i] 
            matrix[j][size - 1 - i] = matrix[size - 1 - i][size - 1 - j]   
            matrix[size - 1 - j][size - 1 - j] = matrix[size - 1 - j][i]   
            matrix[size - 1 - j][i] = temp

    display(matrix) 

def display(matrix):
    size = len(matrix) 
    for i in range(0, size): 
        res = ""
        for j in range(0, size): 
            res += str(matrix[i][j]) + ", "
        print res

    print "---"

# Test case 1 
mat1 = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ] 
           
# Test case 2 
mat2 = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 

# Test case 3 
mat3 = [ [1, 2 ], 
        [4, 5 ] ] 
          

rotate(mat1) 
rotate(mat2)  
rotate(mat3)