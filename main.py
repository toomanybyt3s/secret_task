# Task 1, integer frequency

from random import randrange

def main():
    results_dict = int_freq(int_array_gen())
    for num, amount in sorted(results_dict.items(), key=lambda x: x[1], reverse=True):
        print("{} apppeared {} numbers of times".format(num, amount))

# Input : Type (list(int)), Takes in a list of numbers
# Return : Type (dict{}), Returns a dictionary with frequency of integers
def int_freq(int_array):
    freq_dict = {}

    for value in int_array:
        if value in freq_dict.keys():
            freq_dict.update({value:(freq_dict.get(value) + 1)})
        else:
            freq_dict.update({value:1})

    return freq_dict

# Input : Type (), Nothing
# Return : Type (list(int)), Returns a List of integers 
def int_array_gen():
    # 32bit limit 2147483647
    data_size = 100000
    data_range = 10
    

    array_limit = randrange(data_size)
    
    
    int_array = [None] * array_limit
    for index, _ in enumerate(int_array):
        int_array[index] = randrange(data_range) # randrange(start,stop,step)

    return int_array

if __name__ == "__main__":
    main()