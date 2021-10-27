def main():
    string = "Test string for Interview 321, blah blah ;#'/a"

    # String Building
    reverse_string = string[::-1]
    iterate_string = iterate_reverse_string(string)
    recursive_string = recursive_reverse_string(string)

    assert iterate_string == reverse_string, "Error in iterate_reverse_string"
    assert recursive_string == reverse_string, "Error in recursive_reverse_string"

    print("Passed all tests")
    print("Heres the reversed strings")
    print("{} Iterative Version{} Recursive Version".format(iterate_string, recursive_string))


# Input : Type (str), A normal non reversed string
# Return : Type (str), Reversed string using iteration
def iterate_reverse_string(string_i):
    string = list(string_i)

    for index in range(len(string) // 2):
        string[index], string[len(string) - index - 1] = string[len(string) - index - 1], string[index]
    
    return "".join(string)


# Input : Type (str), A normal non reversed string
# Return : Type (str), Reversed string using recursion
def recursive_reverse_string(string_r, index=0):
    if index == 0:
        string_r = list(string_r)
    elif (len(string_r) // 2) == index:
        return "".join(string_r)
    
    string_r[index], string_r[len(string_r) - index - 1] = string_r[len(string_r) - index - 1], string_r[index]

    return recursive_reverse_string(string_r, (index + 1))

if __name__ == "__main__":
    main()