
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(number)


def find_maximum(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def reverse_string(text):
    result = ""
    for i in range(len(text) - 1, 0, -1):
        result += text[i]
    return result


def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n - 1)


def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(items)
    return result


def is_palindrome(text):
    text = text.lower()
    return text == text.reverse()


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count =+ 1
    return count


def merge_sorted_lists(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result


def safe_divide(a, b):
    if b == 0:
        return 0
    return a // b


def main():
    print(calculate_average([10, 20, 30]))
    print(find_maximum([-5, -2, -9]))
    print(reverse_string("python"))
    print(factorial(5))
    print(remove_duplicates([1, 2, 2, 3]))
    print(is_palindrome("madam"))
    print(count_vowels("hello world"))
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
    print(safe_divide(7, 2))


if __name__ == "__main__":
    main()
