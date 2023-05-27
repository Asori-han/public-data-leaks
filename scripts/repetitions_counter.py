import sys
# Open the file in read mode
with open(sys.argv[1], "r") as f:
    # Create an empty dictionary to store the count of each line
    repetitions = {}

    # Read the file line by line
    for line in f:
        # Strip whitespace from the beginning and end of the line
        line = line.strip()

        # If the line is already in the dictionary, increment its count by 1
        if line in repetitions:
            repetitions[line] += 1
        # If the line is not in the dictionary, add a new entry with count 1
        else:
            repetitions[line] = 1

# Get the total number of lines
total_lines = sum(repetitions.values())

# Print the dictionary
print("Line\t\tCount")
print("---------------------")
for line, count in repetitions.items():
    percentage = (count / total_lines) * 100
    print(f"{line}\t\t{count}\t\t{percentage:.2f}%")
