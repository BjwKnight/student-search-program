students = {}

file = open("students.txt", "r")

for line in file:
    line = line.strip()

    if line != "":
        parts = line.split(",")

        student_id = parts[0]
        last_name = parts[1]
        first_name = parts[2]
        major = parts[3]
        gpa = parts[4]

        students[student_id] = [last_name, first_name, major, gpa]

file.close()

while True:

    print("\nChoose an option:")
    print("1) Search by Last Name")
    print("2) Search by Major")
    print("3) Quit")

    choice = input("Enter choice: ")

    if choice == "1":

        search_name = input("Enter last name to search for: ")

        for student_id in students:

            student = students[student_id]

            if student[0] == search_name:

                print(student_id,
                      student[0],
                      student[1],
                      student[2],
                      student[3])

    elif choice == "2":

        search_major = input("Enter major to search for: ")

        for student_id in students:

            student = students[student_id]

            if student[2] == search_major:

                print(student_id,
                      student[0],
                      student[1],
                      student[2],
                      student[3])

    elif choice == "3":

        print("Goodbye")
        break

    else:
        print("Invalid choice")