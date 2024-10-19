
ss = []

def calculate_structure_sum(*args):
    for i in range (len(args)):
        if type(args[i]) == tuple or type(args[i]) == list or type(args[i]) == set:
            calculate_structure_sum(*args[i])
        elif type(args[i]) == dict:
            calculate_structure_sum(*args[i].values())
            calculate_structure_sum(*args[i].keys())
        elif type(args[i]) == int:
            ss.append(args[i])
        else:
            ss.append(len(args[i]))
    return sum(ss)













data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)