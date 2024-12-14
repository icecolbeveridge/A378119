$$\newcommand{\ds}[1]{\text{digsum}(\#1)}$$

***Note**: All numbers are positive integers unless otherwise stated.*

### Definition

$\ds{n}$ is the digit sum of $n$. For example, $\ds{789} = 7+8+9 = 24$.

### Lemma 1

If $k \mod{10} \ne 0$, then $\ds{k-1}= \ds{k}-1$.

#### Demonstration

Let $k = 10a + b$, where $0 < b \le 9$. Then $\ds{k} = \ds{a} + b$ and $\ds{k-1} = \ds{a}+b-1$, which is $\ds{k}-1$.

#### Lemma 2

If $k = a \cdot 10^b$, where $a \mod{10} \ne 0$, then $\ds{k-1} = \ds{k} + 9b - 1$.

#### Demonstration

* $\ds{k} = \ds{a}$ (because $k$ is $a$ followed by a $b$ zeroes.) 
* $\ds{k-1} = \ds{a-1} + \ds{10^b-1}$. The first term is $\ds{a}-1$ by Lemma 1, and the second term is $9b$ because $10^b-1$ is a string of $b$ nines.
* Hence $\ds{k-1} = \ds{k} + 9b -1$.

### Corollary

If $k \mod 10 \ne 0$, then $\gcd(\ds{k-1}, \ds{k}) = 1$ (by Lemma 1). 

## Proposition

For $n$ not divisible by 3, the smallest positive integer such that $n \mid \ds{k}$ and $n \mid \ds{k-1}$  is $a_0\cdot 10^{b_0}$, where $a_0$ is the smallest positive integer such that $\ds{a_0}=n$ and $b_0=9^{-1}\pmod{n}$.

### Proof

Suppose $\ds{k} = An$ and $\ds{k-1} = Bn$ for $n>1$ and $n \mod 3 \ne 0$. By the Corollary, since the digit sums are not co-prime, $k \mod 10 = 0$; $k$ can therefore be written as $k = a \cdot 10^b$, where $a \mod 10 \ne 0$.

We then have $An = \ds{a}$. Given this, $Bn = \ds{a} + 9b - 1$, which is a multiple of $n$ iff $9b-1$ is a multiple of $n$. Therefore $b = 9^{-1} \pmod{n} + nt$ for some non-negative integer $t$. 

**Remark**: If $n$ were a multiple of 3, 9 would have no multiplicative inverse. 

For $k = a\cdot 10^b$ to satisfy $\ds{k} = An$ and $\ds{k-1}=Bn$, it is necessary and sufficient that:

1. $\ds{a}=An$; and
2. $b = 9^{-1}\pmod{n} + nt$ (for some non-negative integer $t$)

In particular, $b_0 = 9^{-1} \pmod{n}$ is the smallest $b$ that satisfies condition 2 (so $k$ must end in at least $b_0$ zeros), and $a_0 = \text{A051885}(n)$ is the smallest $a$ that satisfies condition 1. 

Therefore $k = a_0 \cdot 10^{b_0}$ is the smallest $k$ that satisfies both $n \mid \ds{k}$ and $n \mid \ds{k-1}$.

### Consequence

Since $\text{A378119}(n)$ is the smallest positive integer $k$ satisfying $n \mid \ds{k}$ and $n \mid \ds{k+1}$, we have $\text{A378119}(n) = \text{A051885}(n) \cdot 10^{9^{-1} \pmod n}-1$.
