def is_palindromic(n): n=str(n); return n==n[::-1]
L = 10000
def is_lychrel(n, m=49):
 for _ in range(m):
   n+= int(str(n)[::-1])
   if is_palindromic(n): return 0
   return 1
print (sum(is_lychrel(n) for n in range(10, L)))
