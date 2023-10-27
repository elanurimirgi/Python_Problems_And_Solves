#Homework1
max_bid = int(input("Enter the maximum bid: "))
winning_bid = 0

while True:
    bid = input("Enter a bid or press 'q' to quit: ")
    
    if bid == "q":
        break
    
    bid = int(bid)
    
    if bid > winning_bid:
        winning_bid = bid

print("Sold:", winning_bid)

#Homework2
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = []

for i in range(x + 1): 
    for j in range(y + 1): 
        for k in range(z + 1): 
            if i + j + k != n:
                coordinates.append([i,j,k])


print(coordinates)
