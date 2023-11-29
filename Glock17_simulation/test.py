grade = int(input("Enter your grade  "))
student_name = str(input("Enter your name"))
def grade_student(student_name:str,grade:int):
    if grade >0 and grade <= 39:
        print(f"You got an E {student_name}")
    # elif grade >39 and grade <= 49:
    #     print(f"You got a D" ({student_name}))
    # elif grade >49 and grade <=59:
    #     print(f"You got a C" ({student_name}))
    # elif grade >59 and grade <=79:
    #     print(f"You got a B" ({student_name}))
    # elif grade >79 and grade <= 100:
    #     print(f"You got an A {student_name}")
    else:
        print("Input correct marks")  

