def find_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    :param numbers: List of numbers
    :return: Average of the numbers
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

def reverse_list(input_list):
    return input_list[::-1]

def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == "__main__":
    # Code inside this block will only run if this file is executed directly.
    # It won't run when this module is imported elsewhere.
    print(reverse_list([2, 4, 5, 7, 9]))