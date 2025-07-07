# Task 2: Write and Append Data to a File
def write_to_file(output):

    initial_input = input("Enter text to write to the file: ")
    with open('output', 'w') as file:
        file.write(initial_input + '\n')
    print("Initial content written.")


    additional_input = input("Enter text to append to the file: ")
    with open('output', 'a') as file:
        file.write(additional_input + '\n')
    print("Additional content appended.")

def read_file(output):

    print("\nFinal content of the file:")
    with open('output', 'r') as file:
        for line in file:
            print(line.strip())


file_name = 'output.txt'


write_to_file(file_name)
read_file(file_name)
