#Homework1
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    scores = set([student[1] for student in students])
    second_lowest = sorted(scores)[1]

    # Get the names of students with the second lowest grade
    names = [student[0] for student in students if student[1] == second_lowest]

    # Sort the names alphabetically
    names.sort()

    # Print each name on a new line
    for name in names:
        print(name)


#Homework2
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
         "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T", "U", "V", "W", "X", "Y", "Z"]

# Take three numbers as input
index1 = int(input())
index2 = int(input())
index3 = int(input())

# Retrieve letters from the alpha list using the indexes
letter1 = alpha[index1]
letter2 = alpha[index2]
letter3 = alpha[index3]

# Output the letters
print(letter1 + letter2 + letter3)

