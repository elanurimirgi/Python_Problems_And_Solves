#Homework1
# Read the number of students' records
n = int(input())

# Create an empty dictionary to store students' marks
student_marks = {}

# Read and store the names and marks in the dictionary
for _ in range(n):
    student_info = input().split()
    name = student_info[0]
    marks = list(map(float, student_info[1:]))
    student_marks[name] = marks

# Read the query_name
query_name = input()

# Calculate the average marks for the query_name
average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

# Print the result with two decimal places
print("{:.2f}".format(average_marks))


#Honework2
supported = ["Lights off", "Lock the door", "Open the door", "Make coffee", "Shut down"]

# Take a command as input
command = input()

# Check if the command is in the list of supported commands
if command in supported:
    print("OK")
else:
    print("Unknown")
