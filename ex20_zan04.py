


if __name__ == '__main__':
    tpl = 12, 34, 56, 78, 90

    for item in enumerate(tpl):
        key, value = item
        print(f'key = {key}, value={value}')

    print('---')