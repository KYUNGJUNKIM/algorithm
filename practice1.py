#1

text = input("Please Enter a string: ")
length = len(text) + 2
ceiling = "-+" * (length//2) + "-"
print(ceiling[:-1] if length%2 == 0 else ceiling)
print("|" + text + "|")
floor = ceiling[::-1][1:] + "+"
print(floor[:-1] if length % 2 == 0 else floor) 


#2
a, b= map(int, input("Enter two positive integers: ").split())

x_list = list(range(-a, a+1))
y_list = list(range(-b, b+1))

cnt=0
for x in x_list:
    for y in y_list:
        if (x**2/a**2)+(y**2/b**2) <= 1:
            print("%d, %d" %(x, y))
            cnt += 1

print ("The number of points is %d" %cnt)  


#3
n = int(input("Enter an integer which is greater than or equal to 3: "))
if n<3:
    print("A number greater than or eqaul to 3 is required.")

cnt = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y: continue
        for z in range(1, n+1):
            if z == x or z == y: continue
            print(x,y,z)
            cnt += 1

print("A number of cases is %d: " %cnt)      



#4
odd = int(input("Enter an odd number: "))
if odd % 2 == 0:
    print("Wrong Input")

background = "="
diamond = "*"

row_num = (odd * 2) - 1

top = []
for x in range(1, odd+1, 2):
    row = background * ((row_num-x)//2)
    row += diamond * x + row
    print(row)
    top.append(row)

bottom = top[::-1][1:]
for row in bottom:
    print(row)



#5
import random

card = list(range(1,12))*4

mine, dealer = [], []

for i in range(2):
    mine.append(card.pop(random.randint(0, len(card)-1)))
    dealer.append(card.pop(random.randint(0, len(card)-1)))

mine_sum = sum(mine)
dealer_sum = sum(dealer)

print(mine)
print("my score: %d" %mine_sum)
print(dealer)
print("dealer's score: %d" %dealer_sum)

if mine_sum > dealer_sum:
    print("Win")
elif mine_sum == dealer_sum:
    print("Draw")
else:
    print("Lose")

