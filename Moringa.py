print("Hello Wolrd")
print("John", "Allan")
list2=[2,3,"Allan", "Nairobi"]

#indetation
def new_function():
    print("Hey am a new function")
new_function()

def full_name(first_name, second_name):
    print(first_name + " " + second_name)
full_name("Allan", "Ngeiywa")

pass_mark =60

def student_grade(marks):
    if marks < pass_mark:
        print("student has failed")
    else:
        print("student has passed")
student_grade(70)
