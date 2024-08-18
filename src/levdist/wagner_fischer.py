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
