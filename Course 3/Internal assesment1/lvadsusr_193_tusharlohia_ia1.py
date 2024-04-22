# -*- coding: utf-8 -*-
"""LVADSUSR_193_tusharlohia_IA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C-p6rDyqmrE1bztSbamFHooHLVarv4Wh

Q1
"""

length = float(input("Enter length(m): "))
width = float(input("Enter width(m): "))

area = length * width
print(f"Your property area is {area} meter sq")
if area < 10:
  print("you have a small property")
elif area < 50:
  print("you have a medium property")
else:
  print("you have a large property")

"""Q2"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = round(weight / (height * height),2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
elif bmi < 35:
    category = "Obese (Class 1)"
elif bmi < 40:
    category = "Obese (Class 2)"
else:
    category = "Bariatic Obese (Class 3)"
print("Your bmi is:", bmi)
print(f"You are in {category} category")

"""Q3"""

class Record:
    def __init__(self):
        self.records = {}

    def add_record(self,id,subject,grade):
        if id not in self.records:
            self.records[id] = {}
        self.records[id][subject] = grade

    def update_record(self, id, subject, grade):
        if id in self.records:
            self.records[id][subject] = grade

    def retrieve_record(self, id):
        if id in self.records:
            return self.records[id]

    def print_report(self, id):
        student_record = self.retrieve_record(id)
        if student_record:
            print(f"report for student ID: {id}")
            for subject, grade in student_record.items():
                print(f"subject: {subject}, grade: {grade}")
        else:
            print("student not found.")

"""Q4"""

age = int(input("enter your age:"))

if age < 13:
  print(" As you are in Children category so watch children rated content")
elif 13 <= age < 20:
  print(" As you are in Teen category so watch UA rated content")
elif 20 <= age < 65:
  print(" As you are in Adult category so can watch UA rated or A rated content")
else:
  print(" As you are in Senior citizen category so can watch Any content")

"""Q5"""

def targeted_user_ids(user_ids):
    even_user_ids = []
    for user_id in user_ids:
        if user_id % 2 == 0:
            even_user_ids.append(user_id)
    return even_user_ids

def main():
        user_ids_input = input("Enter user IDs (, in between21): ")
        user_ids = [int(user_id) for user_id in user_ids_input.split(",")]
        even_user_ids = targeted_user_ids(user_ids)

        print("Target these subscriber IDs:")
        print(even_user_ids)

main()

"""Q6"""

def main():
    file_name = "example.txt"
    correct_password = "pass"

    entered_password = input("Enter the password to read the file: ")
    if entered_password == correct_password:
        print("Password correct. Access granted")
    else:
        print("Incorrect password. Access denied.")

main()

"""Q7"""

def calculate_average(ratings):
    return sum(ratings) / len(ratings)

def main():
  ratings = input("enter ratings for you place (1-5 only) (, in between): ").strip().split(",")
  ratings = [int(rating) for rating in ratings]
  average_rating = calculate_average(ratings)
  print("Average rating:", average_rating)

main()

"""Q8"""

def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    string = input("Enter a string: ")
    vowel_count = count_vowels(string)
    print("No. of vowels in the string:", vowel_count)


main()

"""Q9"""

pass

"""Q10"""

def calculate_SI(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def main():
    try:
        principal = float(input("enter the principal amount Rs. "))
        rate = float(input("enter the interest rate: "))
        time = float(input("enter the time period: "))
        interest = calculate_SI(principal, rate, time)

        print("simple interest: Rs.",interest)

    except ValueError:
        print("enter valid numerical values.")

main()

"""Q11"""

pass

"""Q12"""

def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def main():

  x = float(input("Enter the first number: "))
  y = float(input("Enter the second number: "))
  operator = input("Enter the operator (+,/): ")

  if operator == '+':
    result = add(x, y)
  elif operator == '/':
    result = divide(x, y)
  else:
    print("Invalid operator.")
    return

  print("Result:", result)


main()

"""Q13"""

def append_server_uptime_to_file(file_name, server_uptime):
    with open(file_name, 'a') as file:
        file.write(str(server_uptime))

def main():
  file_name = "server_uptime.txt"
  server_uptime = input("enter server_uptime: ")

  append_server_uptime_to_file(file_name, server_uptime)
  print(f"server_uptime ({server_uptime}) appended to {file_name}")


main()

"""Q14"""

def append_server_uptime_to_file(file_name, server_uptime):
    with open(file_name, 'a') as file:
        file.write(str(server_uptime))

def main():
  file_name = "server_uptime.txt"
  server_uptime = input("enter server_uptime: ")

  append_server_uptime_to_file(file_name, server_uptime)
  print(f"server_uptime ({server_uptime}) appended to {file_name}")


main()

"""Q15"""

def append_server_uptime_to_file(file_name, server_uptime):
    with open(file_name, 'a') as file:
        file.write(str(server_uptime))

def main():
  file_name = "server_uptime.txt"
  server_uptime = input("enter server_uptime: ")

  append_server_uptime_to_file(file_name, server_uptime)
  print(f"server_uptime ({server_uptime}) appended to {file_name}")

  stock_value = input("enter the stock value for that day: ")
  with open(file_name, 'a') as file:
     file.write(f"stock value in Rs.: {stock_value}\n")
     file.read()

main()