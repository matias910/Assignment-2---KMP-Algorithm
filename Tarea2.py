
def failure_function(b: str) -> list[int]:
    n = len(b)
    f = [0] * (n + 1)
    t = 0
    for s in range(2, n + 1):
        while t > 0 and b[t] != b[s - 1]:
            t = f[t]
        if b[t] == b[s - 1]:
            t += 1
        f[s] = t
    return f


def kmp(a: str, b: str) -> str:
   
    f = failure_function(b)
    n = len(b)
    m = len(a)

    s = 0
    for i in range(1, m + 1):
        while s > 0 and a[i - 1] != b[s]:
            s = f[s]
        if a[i - 1] == b[s]:
            s = s + 1
        if s == n:
            return "yes"

    return "no"


def kmp_verbose(a: str, b: str) -> str:
    f = failure_function(b)
    n = len(b)
    m = len(a)

    print(f"\n  Keyword : {b}")
    print(f"  Text    : {a}")
    print(f"  f(s)    : {f[1:]}")
    print(f"  {'i':>4}  {'a[i]':>6}  {'b[s+1]':>8}  {'s before':>10}  {'s after':>9}  action")
    print("  " + "-" * 65)

    s = 0
    for i in range(1, m + 1):
        while s > 0 and a[i - 1] != b[s]:
            print(f"  {i:>4}  {a[i-1]:>6}  {b[s]:>8}  {s:>10}  {f[s]:>9}  slide: s = f({s}) = {f[s]}")
            s = f[s]
        before = s
        if a[i - 1] == b[s]:
            s += 1
            print(f"  {i:>4}  {a[i-1]:>6}  {b[s-1]:>8}  {before:>10}  {s:>9}  match")
        else:
            print(f"  {i:>4}  {a[i-1]:>6}  {b[s] if s < n else '-':>8}  {before:>10}  {s:>9}  mismatch")
        if s == n:
            print(f"\n  → Found at position {i - n + 1} (1-based). Returning 'yes'.\n")
            return "yes"

    print(f"\n  → End of text reached. Returning 'no'.\n")
    return "no"


if __name__ == "__main__":
    keyword = "ababaa"

    print("=" * 60)
    print("  KMP Algorithm — Exercise 3.4.6")
    print("=" * 60)

    f = failure_function(keyword)
    print(f"\nKeyword : {keyword}")
    print(f"f(s)    : {f[1:]}  (indexed 1 to {len(keyword)})\n")

    print("-" * 60)
    print("Exercise a)  Text: abababaab  |  Keyword: ababaa")
    result_a = kmp_verbose("abababaab", keyword)
    print(f"  kmp('abababaab', 'ababaa') → '{result_a}'")

    print("-" * 60)
    print("Exercise b)  Text: abababbaa  |  Keyword: ababaa")
    result_b = kmp_verbose("abababbaa", keyword)
    print(f"  kmp('abababbaa', 'ababaa') → '{result_b}'")