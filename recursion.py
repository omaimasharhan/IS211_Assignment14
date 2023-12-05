# Part I: Implement the Fibonnaci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Part II: Implement Euclid’s GCD Algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Part III: String Comparison
def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])

def main():
    print("1. Fibonacci Sequence")
    n = int(input("Enter a number to get its Fibonacci sequence value: "))
    print(f"Fibonacci sequence at position {n}: {fibonacci(n)}")

    print("\n2. GCD Calculation")
    a = int(input("Enter first number for GCD calculation: "))
    b = int(input("Enter second number for GCD calculation: "))
    print(f"GCD of {a} and {b} is: {gcd(a, b)}")

    print("\n3. String Comparison")
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print(f"String comparison of '{s1}' and '{s2}': {compareTo(s1, s2)}")

if __name__ == "__main__":
    main()
