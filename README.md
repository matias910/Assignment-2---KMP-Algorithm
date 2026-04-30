# Assignment 2 - KMP Algorithm
### Samuel Valencia Montoya - Matias Zapata Rojas
School of Applied Sciences and Engineering – Eafit
Professor: Cesar Guerra Villa

## Versions

| Component            | Version / Details  |
|---------------------|--------------------|
| Operating System     | Windows 11         |
| Programming Language | Python 3.14.0      |
| Compiler / Runtime   | CPython 3.14.0     |

---

## How to Run

**1. Make sure Python 3 is installed:**
```bash
python3 --version
```
You should see `Python 3.14.0` or higher.

**2. Navigate to the `assignment2/` folder:**
```bash
cd assignment2
```

**3. Run the program:**
```bash
python3 kmp.py
```

The program will test whether the keyword `ababaa` is a substring of the following strings:

- `abababaab` — Exercise 3.4.6 a)
- `abababbaa` — Exercise 3.4.6 b)

**4. To use the functions in your own code:**
```python
from kmp import kmp, failure_function

# Compute the failure function for a keyword
f = failure_function("ababaa")
# f = [0, 0, 0, 1, 2, 3, 1]
# f[1]=0, f[2]=0, f[3]=1, f[4]=2, f[5]=3, f[6]=1

# Test whether a keyword appears in a text
result = kmp("abababaab", "ababaa")
# result = "yes"

print(result)
```

---

## Algorithm Explanation

The **KMP algorithm** is defined in  
**Figure 3.20 (page 138)** of:

> Aho, Lam, Sethi, Ullman. *Compilers: Principles, Techniques, and Tools*. 2nd ed. Pearson/Addison Wesley, 2007.

### What it does

Given a text `a[1] a[2] ... a[m]` and a keyword `b[1] b[2] ... b[n]`, the KMP algorithm
determines whether the keyword occurs as a substring of the text in **O(m + n)** time.

It relies on the **failure function** `f(s)` (computed in Assignment 1) to avoid redundant
comparisons. When a mismatch occurs after `s` characters have been matched, the algorithm
does not restart from scratch — instead it jumps to state `f(s)`, preserving the longest
valid partial match found so far.

For example, for the keyword `ababaa`:

| s    | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| b[s] | a | b | a | b | a | a |
| f(s) | 0 | 0 | 1 | 2 | 3 | 1 |

`f(5) = 3` means the longest proper suffix of `ababa` that is also a prefix is `aba` (length 3).  
So when a mismatch happens at position 5, the algorithm continues from state 3 instead of 0.

### Why it is used

During the lexical analysis phase of a compiler, the scanner must recognize tokens from
the source text as efficiently as possible. The KMP algorithm provides a linear-time
solution for this pattern-matching problem. By using the failure function to slide the
keyword intelligently on mismatches, the algorithm scans each character of the text
token recognition in compiler front-ends.````
