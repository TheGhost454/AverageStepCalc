"""
Average steps taken
Preston Rizzo
"""
import sys


def average_steps(file, days):
    """
    Takes the average from the file numbers based on the length of the month
    :param file: The file from open_input_file
    :param days: The days in a month
    :return: The average number
    """
    total = 0
    count = 0
    try:
        for day in range(days):
            num = int(file.readline())
            total += num
            count += 1
    except ValueError:
        # Ends program if value is below 365 and cannot run properly anymore
        print("The program was aborted because there were less than 365 numbers in the file")
        sys.exit(1)
    average = total / count
    return average


def open_input_file():
    """
    Takes an input of a file name and opens it if possible
    :return: returns an opened version of the file
    """
    file = ""
    file_obj = ""
    while file == "":
        try:
            file = input("Enter the file name ")
            file_obj = open(file, "r")
        except FileNotFoundError:
            # Informs user the file doesn't exist and resets the input
            print("The file ", file, "was not found enter a different file name")
            file = ""
    return file_obj


def main():
    """
    Gets a file and prints the average for
    each month from the file
    :return:
    """
    filetype = open_input_file()
    print("the average number of steps in January is ", format(average_steps(filetype, 31), ".2f"))
    print("the average number of steps in February is ", format(average_steps(filetype, 28), ".2f"))
    print("the average number of steps in March is ", format(average_steps(filetype, 31), ".2f"))
    print("the average number of steps in April is ", format(average_steps(filetype, 30), ".2f"))
    print("the average number of steps in May is ", format(average_steps(filetype, 31), ".2f"))
    print("the average number of steps in June is ", format(average_steps(filetype, 30), ".2f"))
    print("the average number of steps in July is ", format(average_steps(filetype, 31), ".2f"))
    print("the average number of steps in August is ", format(average_steps(filetype, 31), ".2f"))
    print("the average number of steps in September is ", format(average_steps(filetype, 30), ".2f"))
    print("the average number of steps in October is ", format(average_steps(filetype, 31), ".2f"))
    print("the average number of steps in November is ", format(average_steps(filetype, 30), ".2f"))
    print("the average number of steps in December is ", format(average_steps(filetype, 31), ".2f"))
    filetype.close()


if __name__ == '__main__':
    main()
