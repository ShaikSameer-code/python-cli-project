students=[
    {"id":1,"name":"sameer","grade":"A+"},
    {"id":2,"name":"usama","grade":"A+"},
]
while True:
    option=input("1.showstudents \n2.add \n3.delete \n4.update \n5.exit \nchoose option:")
    
    if option=="1":
        if not students:
            print("no students found")
        else:
            for student in students:
               print(student)
    elif option=="2":
        id=int(input("enter the id for new student :"))
        name=input("enter the name for new student :")
        grade=input("enter the grade for new student :")
        student={"id":id,"name":name,"grade":grade}
        students.append(student)
        print(students)
    elif option=="3":    
        id=int(input("enter the id to delete :"))
        for student in students:
            if student["id"]==id:
                students.remove(student)
                print("student deleted ",student)
                break
    elif option=="4":  
        id=int(input("enter by id to update :" ))
        for student in students:
            if student["id"]==id: 
                name=input("enter the new name :")
                grade=input("enter the new grade :")
                student["name"]=name
                student["grade"]=grade
                print("student updated ",student)
                break
    elif option=="5":
        print("progam ended")
        break
     
