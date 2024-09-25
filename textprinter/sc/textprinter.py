# Using open() function
file_path = "input_to_file.txt"

text_for_file = input("Enter the content of the file:")

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write content to the file
    file.write(text_for_file)
    
print("File {} created successfully".format(file_path))