from math import log, ceil

def sq_mult(m, e, n):
    s = ceil(log(e, 2))
    t = 1
    for i in reversed(range(0, s)):
        t *= t
        t %= n
        print(f"step {i}: squaring")
        if e & (1 << i):
            t *= m
            t %= n
            print(f"step {i}: multiplying")
    return t

def main():
    m = 42
    print("m = {m}, key = (31, 35)")
    sq_mult(m, 31, 35)
    print("-------------")
    print("m = {m}, key = (33, 35)")
    sq_mult(m, 33, 35)

if __name__ == "__main__":
    main()
