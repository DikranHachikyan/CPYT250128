

if __name__ == '__main__':
    
    config = {
        'title': 'Text Editor',
        'version': '1.2.4',
        'max_tabs': 1000,
        'magins': [5, 10, 10, 5],
        'printer': 'HP Laser Jet'
    }

    for key, value in config.items():
        print(f'key={key} => {value}')
    else:
        print('--- else ---')

    print('---')