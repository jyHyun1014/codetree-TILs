arr = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]

def print_array(arr):
    if isinstance(arr, list):
        print("{", end="")
        print(", ".join([print_array(x) for x in arr]), end="")
        print("}", end="")
    else:
        return "{" + ", ".join(map(str, arr)) + "}"

print_array(arr)