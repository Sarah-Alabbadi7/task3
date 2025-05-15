num_count = int(input("how many numbers?: "))

number_1 = 10
number_2 = 20
number_3 = 30
number_4= 40
number_5 = 50

list_of_numbers = [10,20,30,40,50]
list_of_numbers.append(60)
for _ in range (num_count ):
 user_input = int(input("enter the number: "))
 list_of_numbers.append(user_input)


print("the numbers : ", list_of_numbers)
print ("the last number is: !!",  list_of_numbers[len(list_of_numbers)-1])

