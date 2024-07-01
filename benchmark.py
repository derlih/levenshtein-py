from timeit import timeit

if __name__ == "__main__":
    print("Benchmark:")
    iterations = 10_000
    full_matrix = timeit(
        setup="from levenshtein_py import full_matrix",
        stmt="full_matrix('Levenshtein', 'Frankenstein')",
        number=iterations,
    )
    print(f"Full matrix({iterations}): {full_matrix/iterations} sec")
