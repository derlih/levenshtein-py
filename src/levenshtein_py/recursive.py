def recursive(a: str, b: str) -> int:
    if not a:
        return len(b)
    if not b:
        return len(a)

    head_a, *tail_a = a
    head_b, *tail_b = b

    if head_a == head_b:
        return recursive(tail_a, tail_b)

    return 1 + min(
        recursive(tail_a, b), recursive(a, tail_b), recursive(tail_a, tail_b)
    )
