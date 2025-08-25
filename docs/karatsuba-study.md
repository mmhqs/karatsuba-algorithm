## Karatsuba Study
In this file I tried to understand the math behind the Karatsuba algorithm before implementing it in Python or any other programming language.

[1. What's wrong with the traditional multiplying method?](#whats-wrong-with-the-traditional-multiplying-method)
[2. What does Karatsuba do to solve this problem?](#what-does-karatsuba-do-to-solve-this-problem)
[2.1. Step 1 - Breaking down the numbers](#step-1-breaking-down-the-numbers)
[2.2. Step 2 - Traditional (inefficient) multiplication](#step-2-traditional-inefficient-multiplication)
[2.3. Step 3 - Karatsuba's magic](#step-3-karatsubas-magic)
[2.4. Step 4 - Combine the results](#step-4-combine-the-results)
[3. Wait, wait! What happens if the numbers are not powers of 2?](#wait-wait-what-happens-if-the-numbers-are-not-powers-of-2)
[4. And what happens if the numbers are odd?](#and-what-happens-if-the-numbers-are-odd)
[5. Complexity and advantages](#complexity-and-advantages)
[6. Conclusion](#conclusion)

### What's wrong with the traditional multiplying method?
Imagine you want to multiply two large numbers, `x` and `y`, each with `n` digits. Using the traditional method, you would **multiply each digit** of `x` by each digit of `y`. This requires approximately n² multiplication operations. If the numbers have thousands or millions of digits, the computational cost becomes prohibitive.

For example, to multiply two 1024-digit numbers, the traditional method would require:
`1024² = 1048576 single-digit multiplications`

### What does Karatsuba do to solve this problem?
Karatsuba's central idea is to break down the multiplication of two large numbers into smaller multiplications, and instead of performing four smaller multiplications as would be expected, he achieves the result with only three.

Let's go through it step by step.

#### Step 1 - Breaking down the numbers
Suppose we want to multiply two numbers `x` and `y`, each with `n` digits (for simplicity, let's assume that `n` is a power of 2). We can divide each number into two halves:

- `x = a * 10^(n/2) + b`
- `y = c * 10^(n/2) + d`

Where `a` and `c` are the most significant halves (the first `n/2` digits) and `b` and `d` are the least significant halves (the last `n/2` digits).

**Practical example:**
Let's multiply `x` = 5678 and `y` = 1234.
Here, `n` = 4. Therefore, `n/2` = 2.

- `a` = 56 (first half of `x`)
- `b` = 78 (second half of `x`)
- `c` = 12 (first half of `y`)
- `d` = 34 (second half of `y`)

Thus, we can rewrite the numbers as:
`x = 56 * 10^2 + 78`
`y = 12 * 10^2 + 34`

#### Step 2 - Traditional (inefficient) multiplication
The multiplication `x * y` becomes:
`x * y = (a * 10^(n/2) + b) * (c * 10^(n/2) + d)`
`x * y = (a*c) * 10^n + (a*d + b*c) * 10^(n/2) + (b*d)`

Note that to calculate this, we would need four multiplications of smaller numbers:
- `a * c`
- `b * d`
- `a * d`
- `b * c`

**This does not improve efficiency!** We are still left with a complexity of O(n²).

#### Step 3 - Karatsuba's magic
Karatsuba realized that the middle term `(a*d + b*c)` could be calculated in a smarter way, **using only one additional multiplication instead of two**.

He defines three products instead of four:
- `z2 = a * c`
- `z0 = b * d`
- `z1 = (a + b) * (c + d)`

And now, the genius part. He calculates the middle term `(a*d + b*c)` as follows:
`a*d + b*c = z1 - z2 - z0`

**Why does this work?**
`(a + b) * (c + d) = a*c + a*d + b*c + b*d`
If we replace `a*c` with `z2` and `b*d` with `z0`, we get:
`z1 = z2 + a*d + b*c + z0`
Rearranging the equation, we get:
`a*d + b*c = z1 - z2 - z0`

We get the middle term with just one new multiplication (`z1`), reusing the results of `z2` and `z0`.

#### Step 4 - Combine the results
The final result of the multiplication `x * y` is obtained by combining `z2`, `z1`, and `z0` with the appropriate offsets (the powers of 10):

`x * y = z2 * 10^n + (z1 - z2 - z0) * 10^(n/2) + z0`

**Practical Example (Continued)**
Remember: `a` = 56, `b` = 78, `c` = 12, `d` = 34.

Calculate `z2`: 
`z2 = a * c` 
= 56 * 12 
= 672

Calculate `z0`: 
`z0 = b * d` 
= 78 * 34 
= 2652

Calculate `z1`:
`z1 = (a + b) * (c + d)` 
= (56 + 78) * (12 + 34)
= 134 * 46 
= 6164

(Note that these multiplications (56*12, 78*34, 134*46) could be solved recursively with Karatsuba's algorithm itself if the numbers were larger. For this example, we calculate directly).

Calculate the **middle term**:
`z1 - z2 - z0` = 6164 - 672 - 2652 = 2840

Combine everything:
Remember the formula: `result = z2 * 10^n + (middle term) * 10^(n/2) + z0`
With `n` = 4 and `n/2`= 2:
`result = 672 * 10^4 + 2840 * 10^2 + 2652`
= 6720000 + 284000 + 2652
= 7006652

It works perfectly!

### Wait, wait! What happens if the numbers are not powers of 2?

### And what happens if the numbers are odd?

### Complexity and advantages
- Traditional Method: The complexity is O(n²).
- Karatsuba Algorithm: The complexity is approximately O(n^log2(3)), which is about O(n^1.585).

It may not seem like a big difference, but for numbers with millions of digits, the reduction in computation time is enormous. The Karatsuba algorithm is one of the pillars that make modern cryptography (which depends on operations with very large numbers) feasible.

### Conclusion
The Karatsuba algorithm replaces one large multiplication with three smaller multiplications and some additions and subtractions. By applying this logic recursively, it drastically reduces the total number of multiplication operations, making it much more efficient than the school method for large numbers.

