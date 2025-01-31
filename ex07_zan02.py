# %%

conn = dict(
    host='localhost',
    db='sales',
    port=1521,
    keepalive=True
)

print(f'host = {conn["host"]}')

# %%

user = {
    'first_name':'Anna',
    'last_name': 'Smith',
    'phone': '111-22-44',
    'age': 34,
    'friends': ['John', 'Markus']
}

print(f'{user["first_name"]} friends:{user["friends"]}')

# %%

print( user.keys())

# %%

print(user.values())

# %%

print(user.items())

# %%

print( 'age' in user )

# %%

print( 'Smith' in user.values() )

# %%

print(user['address'])

# %%

print(user.get('address', 'Bulgaria, Sofia'))

# %%
