# Task 1: Read a File and Handle Errors
def read_file(sample):
    try:
        with open('sample.txt', 'r') as file:
            print("Reading file content :\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{'sample.txt'}' does not exist.")


read_file('sample.txt')
