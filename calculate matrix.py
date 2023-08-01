matrix = [[1, 2, 3],
          [4, 5, 6]]
matrix1 = [[1, 2, 3],
          [4, 5, 6]]
matrix2 = []

if len(matrix) == len(matrix1) and len(matrix[0]) == len(matrix1[0]) and len(matrix[1]) == len(matrix1[1]) :
     
    for i in range(2):
        for j in range(3):
           matrix2.append(matrix[i][j]+matrix1[i][j])
else:
    print("error")
print(matrix2)
           
           
      
        
        
        