
def foo(values, n):
    n **= 2
    print(f'inside foo ({id(n)}) n={n}')

    values.sort(reverse=True)
    print(f'inside foo ({id(values)}) values={values}')


if __name__ == '__main__':
    # mutable
    numbers = [ 5, 4, 6, 3, 7, 8, 9]
    # immutable
    a = 10

    print(f'(before) numbers ({id(numbers)})->{numbers} a ({id(a)})->{a}')

    foo(numbers, a)

    print(f'(after) numbers ({id(numbers)})->{numbers} a ({id(a)})->{a}')

    print('---')