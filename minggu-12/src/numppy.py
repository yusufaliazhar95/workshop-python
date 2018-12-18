import numpy as np
#menghasilkan a 3 by 3 identity matrix
matrix_one = np.eye(3)
matrix_one
#menghasilkan 3 by 3 matrix lainya for perkalian
matrix_two = np.arange(1,10).reshape(3,3)
matrix_two
#mengkalikan dua array
matrix_multiply = np.dot(matrix_one, matrix_two)
matrix_multiply