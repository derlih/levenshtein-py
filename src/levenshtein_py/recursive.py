def recursive(a: str, b: str) -> int:
    if not a:
        return len(b)
    if not b:
        return len(a)

    head_a = a[0]
    tail_a = a[1:]
    head_b = b[0]
    tail_b = b[1:]

    if head_a == head_b:
        return recursive(tail_a, tail_b)

    return 1 + min(
        recursive(tail_a, b), recursive(a, tail_b), recursive(tail_a, tail_b)
    )
