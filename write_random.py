"""
Write random
Preston Rizzo
"""

import random


def get_number():
    """
    Takes the user input and determines if it is a valid input
    :return: nums: the valid value inputted
    """
    nums = input("Enter how many numbers you want ")
    if nums.isdigit():
        nums = int(nums)
        if nums <= 0:
            print("Enter a positive integer")
            nums = get_number()
    else:
        print("Enter a positive integer")
        nums = get_number()
    return nums


def write_numbers(file, num):
    """
    Opens the previously named file and
    writes random numbers for num times
    :param file: The file named in the main function
    :param num: The number from get number
    """
    outfile = open(file, "w")
    for loop in range(num):
        number = random.randint(100, 1500)
        outfile.write(str(number) + "\n")
    outfile.close()


def read_numbers(file):
    """
    Prints the count, total, and average of the file
    :param file: filetype from main
    """
    line_read = open(file)
    count = 0
    total = 0
    for line in line_read:
        total += int(line)
        count += 1
    average = total / count
    print(f"Count: {count} \nTotal: {total} \nAverage: {average:.2f}")
    line_read.close()


def main():
    """
    Gets a number and a file name then passes
    them to another function to write and read the results
    """
    count = get_number()
    filetype = input("Name the type of file ")
    write_numbers(filetype, count)
    read_numbers(filetype)


if __name__ == '__main__':
    main()
