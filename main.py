def comverter1(numbers):
    list_of_numbers = []
    snumbers = str(numbers)
    for number in snumbers[::-1]:
        list_of_numbers.append(int(number))
    return list_of_numbers


def comverter2(numbers):
    list_of_numbers = []
    for number in str(numbers):
        list_of_numbers.insert(0,int(number))
    return list_of_numbers

def comverter3(numbers):
    return [int(num)for num in str(numbers)[::-1]]


print(comverter1(451269786))
print(comverter2(451269786))
print(comverter3(451269786))