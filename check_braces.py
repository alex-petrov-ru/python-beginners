import _stack

def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочный последовательности
    из круглых и квадратных скобок () []

    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False
    """
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            _stack.push(brace)
        else:
            assert brace in ")]", "Катасрофа! Ожидалась закрывающая скобка: " + str(brace)
            if _stack.is_empty():
                return False
            left = _stack.pop()
            assert left in "([", "Катасрофа! Ожидалась открывающая скобка: " + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return _stack.is_empty()


print(is_braces_sequence_correct('()([][]()()())))'))


if __name__ == "__name__":
    import doctest
    doctest.testmod(verbose=False)

