#just for test uses

array01 = [1, 2, 3, 4]
array02 = [5, 6, 7, 8]

all_numbers = [numbers for sublist in [array01, array02] for numbers in sublist]

print(all_numbers)