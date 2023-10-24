#Homework1
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)  # Find the maximum score

    runner_up_score = -float('inf')  # Initialize runner-up score as negative infinity

    for score in arr:
        if score < max_score and score > runner_up_score:
            runner_up_score = score

    print(runner_up_score)


#Homework2
# Input the person's weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category and output the result
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(category)
