__version__ = "0.5.0"


def classic(a: str, b: str) -> int:
    if not a:
        return len(b)
    if not b:
        return len(a)

    head_a = a[0]
    tail_a = a[1:]
    head_b = b[0]
    tail_b = b[1:]

    if head_a == head_b:
        return classic(tail_a, tail_b)

    return 1 + min(classic(tail_a, b), classic(a, tail_b), classic(tail_a, tail_b))


def wagner_fischer(a: str, b: str) -> int:
    len_a = len(a)
    len_b = len(b)
    v0 = [i for i in range(len_b + 1)]
    v1 = [0 for _ in range(len_b + 1)]

    for i in range(len_a):
        v1[0] = i + 1

        for j in range(len_b):
            deletion_cost = v0[j + 1] + 1
            insertion_cost = v1[j] + 1
            if a[i] == b[j]:
                substitution_cost = v0[j]
            else:
                substitution_cost = v0[j] + 1

            v1[j + 1] = min(deletion_cost, insertion_cost, substitution_cost)

        v1, v0 = v0, v1

    return v0[len_b]


try:
    from .native import wagner_fischer_native

    def levenshtein(a: str, b: str) -> int:
        return wagner_fischer_native(a, b)

except ImportError:
    levenshtein = wagner_fischer
