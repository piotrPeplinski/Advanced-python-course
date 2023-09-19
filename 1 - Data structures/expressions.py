names = ['Marek', 'Piotr', 'Maja', 'Anna', 'Robert', 'Marek']

#males = [name for name in names if name[-1] != 'a']
#males = {name for name in names if name[-1] != 'a'}

# names_len = {
#     name:len(name)
#     for name in names
# }

names = (name for name in names)

print(next(names))
print(next(names))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

a = {
    number:number**2
    for number in numbers
}
print(a)