def check_plural(s):
    if s.endswith('es'):
        return 'plural'
    else:
        return 'not plural'


if __name__ == "__main__":
    # Example usage:
    s1 = "apples"
    s2 = "banana"
    result1 = check_plural(s1)
    result2 = check_plural(s2)
    print(f"'{s1}' is {result1}")
    print(f"'{s2}' is {result2}")