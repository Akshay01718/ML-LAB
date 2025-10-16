student={}
op=0
while op!=4:
    op=int(input("1.Insert\n 2.Delete\n 3.Search\n 4.Exit\n Enter the operation:"))
    if op==1:
        r_no=int(input("Enter the roll no:"))
        name=input("Enter the name:")
        student[r_no]=name
        print(student)

    elif op==2:
        r_no=int(input("Enter the roll no:"))
        if r_no in student.keys():
            student.pop(r_no)
        else:
            print("Student not found")
        print(student)
    elif op==3:
        r_no=int(input("Enter the roll no:"))
        if r_no in student.keys():
            print(student.get(r_no))
        else:
            print("Student not found")
    elif op==4:
        exit()
    else:
        print("Invalid")
        

