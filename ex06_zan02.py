# %%

arr = [19, 23, 45, 67, 63]
print(f'arr={arr}, type is {type(arr)}')

# %%
print(f'second element: {arr[1]}')

arr[2] = 14

print(f'arr={arr}')

# %%
print(f'arr id={id(arr)}')

arr[3] = 5
arr.append(12)

print(f'arr id={id(arr)}')
# %%
tp = 1, 3, 5, 7, 9

arr1 = list( tp )

print(f'arr1={arr1}')

# %%
arr_s = list('Hello Python')

print(f'arr_s={arr_s}')

# %%
