import numpy as np

def lu_decomposition(A):
    """
    Fungsi untuk melakukan dekomposisi LU pada matriks A
    Parameters:
        A: Matriks input (numpy array)
    Returns:
        L: Matriks segitiga bawah
        U: Matriks segitiga atas
    """
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Mengisi diagonal L dengan 1
    for i in range(n):
        L[i][i] = 1
    
    # Melakukan dekomposisi
    for i in range(n):
        # Menghitung elemen U
        for k in range(i, n):
            sum_u = 0
            for j in range(i):
                sum_u += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - sum_u
        
        # Menghitung elemen L
        for k in range(i+1, n):
            sum_l = 0
            for j in range(i):
                sum_l += L[k][j] * U[j][i]
            L[k][i] = (A[k][i] - sum_l) / U[i][i]
    
    return L, U

def solve_lu(L, U, b):
    """
    Menyelesaikan sistem persamaan linear menggunakan hasil dekomposisi LU
    Parameters:
        L: Matriks segitiga bawah
        U: Matriks segitiga atas
        b: Vektor hasil
    Returns:
        x: Solusi sistem persamaan
    """
    n = len(L)
    # Menyelesaikan Ly = b
    y = np.zeros(n)
    for i in range(n):
        sum_y = 0
        for j in range(i):
            sum_y += L[i][j] * y[j]
        y[i] = b[i] - sum_y
    
    # Menyelesaikan Ux = y
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sum_x = 0
        for j in range(i+1, n):
            sum_x += U[i][j] * x[j]
        x[i] = (y[i] - sum_x) / U[i][i]
    
    return x

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh sistem persamaan:
    # 2x + y - z = 8
    # -3x - y + 2z = -11
    # -2x + y + 2z = -3
    
    # Matriks A
    A = np.array([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ])
    
    # Vektor b
    b = np.array([8, -11, -3])
    
    print("Matriks A:")
    print(A)
    print("\nVektor b:")
    print(b)
    
    # Melakukan dekomposisi LU
    L, U = lu_decomposition(A)
    
    print("\nMatriks L (Lower):")
    print(L)
    print("\nMatriks U (Upper):")
    print(U)
    
    # Verifikasi bahwa L × U = A
    print("\nVerifikasi L x U:")
    print(np.dot(L, U))
    
    # Menyelesaikan sistem persamaan
    x = solve_lu(L, U, b)
    
    print("\nSolusi sistem persamaan (X):")
    print(x)
    
    # Verifikasi solusi
    print("\nVerifikasi A x X = b:")
    print(np.dot(A, x))