# %%
tp = (12, 45, 65, 78, 89)

# %%

print(f'second element of tuple: {tp[1]}')
# %%
# TypeError: 'tuple' object does not support item assignment
# tp[2] = 10

# %%
a, b, c, d, e = tp
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

# %%

a, b, *_ = tp

print(f'a={a}, b={b}')

# %%

*_, a, b = tp

print(f'a={a}, b={b}')

# %%

tp = 1, 2, 5, 7, 9

print(f'tp={tp}')
# %%
t1 = (10,)

print(f'type of t1 is {type(t1)}')

# %%

print( 2 in tp )

# %%
print( 4 not in tp )

# %%

print( type(tp) is tuple )

# може и така, но не е правилно
# print( type(tp) == tuple )
# %%
