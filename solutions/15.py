#   Lattice paths

'''
    Grid size = m x n
    Number of paths = (m+n)!/(m!*n!)
'''

fact = [1]*50
fact[0] = 1
for i in range(1,50):
    fact[i] = fact[i-1]*i

print(fact[40]//(fact[20]**2))