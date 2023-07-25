# v1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

r = 5 # row number
c = 3 # col number
element = pascalTriangle(r, c)
print(f"The element at position (r,c) is: {element}")