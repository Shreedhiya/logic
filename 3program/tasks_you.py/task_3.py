# get input the student name and  subject marks 
# print student name, marks total value and total percentage

student_name=input("Enter student name:")
tamil_mark=int(input("Enter tamil mark:"))
english_mark=int(input("Enter english mark :"))
maths_mark=int(input("Enter maths mark:"))
science_mark=int(input("Enter science mark:"))
sscience_mark=int(input("Enter s.science mark:"))
total_mark=tamil_mark+english_mark+maths_mark+science_mark+sscience_mark
average=(total_mark/500)*100
print("~~~~~~~~~~~~~~~~~~~")

print(f"{student_name}")
print(f"{student_name} total mark is {total_mark}")
print(f"{student_name} average mark is {average}")