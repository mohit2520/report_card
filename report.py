# 2.Write a Python Program for Generating a Report Card
print("\n\n\n\t\t\t\t\t\tWELCOME TO F5 DEVELOPERS PORTAL")
print("\t\t\t\t\t      ", end="")
for i in range(18):
    print("_", end=" ")
n = int(input("\n\nEnter number of students data you want : "))
total = 0
for i in range(n):
    name = str(input("\nEnter the student name : "))
    roll = int(input("Enter the roll number : "))
    Class = input("Enter the class : ")
    print("\n****************************************")
    print("Student name :", name)
    print("Roll number :", roll)
    print("Class :", Class)
    print("****************************************\n")
    List = ["maths", "physics", "chemistry", "Cse", "english"]
    List1 = []
    dic = {}
    for j in List:
        subjects = int(input("Enter the marks of " + str(j) + " : "))
        List1.append(subjects)
        dic[j] = subjects
    print(
        "****************************************************************************"
    )
    for j, k in dic.items():
        print("Marks of " + str(j) + " is " + str(k))
    print(
        "****************************************************************************"
    )
    per = sum(List1) // len(List)
    print(
        name,
        "have scored",
        sum(List1),
        "out of",
        (len(List) * 100),
        "marks and he/she have scored",
        per,
        "%",
    )
    # print("The percentage is ", per)
    if per >= 90:
        print("...................A Grade.................")
    elif per >= 75 and per < 90:
        print(".................B Grade...................")
    elif per >= 60 and per < 75:
        print("...............C Grade..............")
    elif per >= 40 and per < 60:
        print("........................D Grade.....................")
    elif per >= 33 and per < 40:
        print("...............E Grade.............")
    elif per < 33:
        print(".................FAIL....................")
