from collections import Counter
from collections import defaultdict
import unittest
import time


def is_unique_chars_algorithm(string):
    # Longer than standard - ASCII 128 characters
    if len(string) > 128:
        return False
    char_set = [False] * 128
    for char in string:
        ascii_val = ord(char)
        if char_set[ascii_val]:
            return False
        char_set[ascii_val] = True
    return True


def is_unique_chars_python_lib(string):
    return len(set(string)) == len(string)


def is_unique_chars_set(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True


def is_unique_chars_dictionary(string):
    count = Counter(string)
    for val in count.values():
        if val > 1:
            return False
    return True


def is_unique_chars_bitvector(string):
    if len(string) > 128:
        return False
    checker = 0
    for char in string:
        val = ord(char)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


def is_unique_chars_sorting(string):
    sorted_str = sorted(string)
    last = None
    for char in sorted_str:
        if char == last:
            return False
        last = char
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars_sorting,
        is_unique_chars_bitvector,
        is_unique_chars_set,
        is_unique_chars_dictionary,
        is_unique_chars_algorithm,
        is_unique_chars_python_lib,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                            is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                                                                           time.perf_counter() - start
                                                                   ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
