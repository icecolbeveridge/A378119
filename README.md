# [OEIS sequence A378119](https://oeis.org/A378119)

My esteemed friend Barney Maunder-Taylor put a new sequence in the OEIS: $A(n)$ is the smallest number $k$ such that the digit sum of $k$ and the digit sum of $k+1$ are both multiples of $k$.

I hypothesise that $A(n) = D \times 10^p - 1$, where $D$ is the smallest positive integer with digit sum $n$ and $p$ is $9^{-1}\pmod{n}$ (if it exists).
