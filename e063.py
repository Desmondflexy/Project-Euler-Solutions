print(sum([10**(n-1) <= A**n < 10**n for n in range(1, 22) for A in range(1, 10)]))

"""
Notice that $S_{(A,n)} = A^n$ always has $n+k$ digits when $A \geq 10$, therefore we
set $A = \{1, 2,..., 9\}$. Setting $A=9$, I noticed that $S_{(9,n)}$ always has $n-k$
digits for $n \geq 22$,, where $k$ is any positive integer. So we set $n =\{1, 2,..., 21\}$.
We are simply looking for how many values of $S$ holds true for $10^{n-1} \leq S_{(A,n)} < 10^n$
This is my Python one-liner program.
"""