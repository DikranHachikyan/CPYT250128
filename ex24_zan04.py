

if __name__ == '__main__':
    
    config = {
        'title': 'Text Editor',
        'version': '1.2.4',
        'max_tabs': 1000,
        'magins': [5, 10, 10, 5],
        'printer': 'HP Laser Jet'
    }

    for key in config:
        print(f'key={key} => {config[key]}')

        if type( config[key] ) is list:
            for value in config[key]:
                print(f'  value={value}')

    print('---')