
import pytest
from solution import tracer


def lines(capsys):
    return capsys.readouterr().out.splitlines()


def test_exact_linear_trace(capsys):
    @tracer
    def factorial(n):
        return 1 if n <= 1 else n * factorial(n - 1)

    assert factorial(4) == 24
    assert lines(capsys) == [
        '→ factorial(4)',
        '  → factorial(3)',
        '    → factorial(2)',
        '      → factorial(1)',
        '      ← factorial = 1',
        '    ← factorial = 2',
        '  ← factorial = 6',
        '← factorial = 24',
    ]


def test_branching_recursion_exact_trace(capsys):
    @tracer
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    assert fib(3) == 2
    assert lines(capsys) == [
        '→ fib(3)',
        '  → fib(2)',
        '    → fib(1)',
        '    ← fib = 1',
        '    → fib(0)',
        '    ← fib = 0',
        '  ← fib = 1',
        '  → fib(1)',
        '  ← fib = 1',
        '← fib = 2',
    ]


@pytest.mark.parametrize(
    'n, expected',
    [(0, 0), (1, 1), (7, 28), (25, 325)]
)
def test_recursive_sum_and_depth(n, expected, capsys):
    @tracer
    def summation(k):
        return 0 if k == 0 else k + summation(k - 1)

    assert summation(n) == expected

    trace = lines(capsys)
    assert len(trace) == 2 * (n + 1)
    assert trace[0] == f'→ summation({n})'
    assert trace[-1] == f'← summation = {expected}'
    assert f'{"  " * n}→ summation(0)' in trace


def test_multiple_positional_arguments(capsys):
    @tracer
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    assert gcd(1071, 462) == 21
    assert lines(capsys) == [
        '→ gcd(1071, 462)',
        '  → gcd(462, 147)',
        '    → gcd(147, 21)',
        '      → gcd(21, 0)',
        '      ← gcd = 21',
        '    ← gcd = 21',
        '  ← gcd = 21',
        '← gcd = 21',
    ]


def test_branching_non_numeric_result(capsys):
    @tracer
    def build(n):
        if n == 0:
            return 'x'
        return '(' + build(n - 1) + build(n - 1) + ')'

    assert build(2) == '((xx)(xx))'

    trace = lines(capsys)
    assert len(trace) == 14
    assert trace[-1] == "← build = '((xx)(xx))'"
    assert trace.count('    → build(0)') == 4


def test_repeated_calls_reset_depth(capsys):
    @tracer
    def countdown(n):
        return 0 if n == 0 else countdown(n - 1)

    assert countdown(3) == 0
    lines(capsys)

    assert countdown(1) == 0
    assert lines(capsys)[0] == '→ countdown(1)'


def test_independent_decorators(capsys):
    @tracer
    def inner(n):
        return n * 2

    @tracer
    def outer(n):
        return inner(n) + 1

    assert outer(3) == 7
    assert lines(capsys) == [
        '→ outer(3)',
        '→ inner(3)',
        '← inner = 6',
        '← outer = 7',
    ]


def test_keyword_arguments_are_forwarded(capsys):
    @tracer
    def power(base, exponent=2):
        return 1 if exponent == 0 else base * power(
            base, exponent=exponent - 1
        )

    assert power(3, exponent=3) == 27

    trace = lines(capsys)
    assert len(trace) == 8
    assert trace[0] == '→ power(3, exponent=3)'
    assert trace[-1] == '← power = 27'


def test_exception_propagates_and_depth_recovers(capsys):
    @tracer
    def may_fail(n):
        if n == 0:
            raise ValueError('stop')
        return may_fail(n - 1)

    with pytest.raises(ValueError, match='stop'):
        may_fail(3)

    first = lines(capsys)
    assert len(first) == 4
    assert first[-1] == '      → may_fail(0)'

    with pytest.raises(ValueError, match='stop'):
        may_fail(0)

    assert lines(capsys) == ['→ may_fail(0)']


def test_no_recursion_and_none_result(capsys):
    @tracer
    def do_nothing():
        return None

    assert do_nothing() is None
    assert lines(capsys) == [
        '→ do_nothing()',
        '← do_nothing = None',
    ]


def test_deep_recursion_no_depth_leak(capsys):
    @tracer
    def descend(n):
        return 0 if n == 0 else descend(n - 1)

    assert descend(100) == 0

    trace = lines(capsys)
    assert len(trace) == 202
    assert trace[101] == '  ' * 100 + '← descend = 0'
    assert trace[-1] == '← descend = 0'


# Дополнительные строгие тесты


def test_keyword_arguments_visible(capsys):
    @tracer
    def add(a, b=0):
        return a + b

    assert add(2, b=3) == 5
    assert lines(capsys) == [
        '→ add(2, b=3)',
        '← add = 5',
    ]


def test_string_arguments(capsys):
    @tracer
    def repeat(text, n):
        if n == 0:
            return ''
        return text + repeat(text, n - 1)

    assert repeat('a', 2) == 'aa'

    trace = lines(capsys)
    assert trace[0] == "→ repeat('a', 2)"
    assert trace[-1] == "← repeat = 'aa'"
    assert len(trace) == 6


@pytest.mark.parametrize(
    'value',
    [None, [], {}, (), True, 0, '', [1, 2, 3]]
)
def test_different_return_types(value, capsys):
    @tracer
    def identity(x):
        return x

    assert identity(value) == value
    assert lines(capsys) == [
        f'→ identity({value!r})',
        f'← identity = {value!r}',
    ]


def test_function_metadata():
    @tracer
    def calculate(n):
        """Example function."""
        return n * 2

    assert calculate.__name__ == 'calculate'
    assert calculate.__doc__ == 'Example function.'


def test_exception_in_middle(capsys):
    @tracer
    def countdown(n):
        if n == 2:
            raise ValueError('stop')
        if n == 0:
            return 0
        return countdown(n - 1)

    with pytest.raises(ValueError, match='stop'):
        countdown(4)

    assert lines(capsys) == [
        '→ countdown(4)',
        '  → countdown(3)',
        '    → countdown(2)',
    ]

    with pytest.raises(ValueError, match='stop'):
        countdown(2)

    assert lines(capsys) == ['→ countdown(2)']


def test_recursive_keyword_arguments(capsys):
    @tracer
    def power(base, exponent=0):
        if exponent == 0:
            return 1
        return base * power(base, exponent=exponent - 1)

    assert power(2, exponent=3) == 8

    assert lines(capsys) == [
        '→ power(2, exponent=3)',
        '  → power(2, exponent=2)',
        '    → power(2, exponent=1)',
        '      → power(2, exponent=0)',
        '      ← power = 1',
        '    ← power = 2',
        '  ← power = 4',
        '← power = 8',
    ]
