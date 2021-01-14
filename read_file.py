# Store the file path for the data file
file = 'Data/input.txt'

# Open the file in "read" mode ('r') and store the contents in a variable
with open(file,'r') as text:

    # This stores a reference to a file stream
    # print(text)

    # Store all of the text inside a variable
    contents = text.read()

    # Print the contents of the text file
    print(contents)