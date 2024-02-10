class StudentDatabase:
    def __init__(self):
        self.students = {}
    def addStudent(self,name,grade):
        self.student[name]= grade
        print(f"added name {name} with grade {grade} in the dataset")
    def searchStudent(self,name):
        if name in self.students:
            print(f"{name} scored {self.students[name]}")
        else:
            print(f"{name} is not found in the dataset")
    def updateStudent(self,name,newgrade):
        if name in self.students:
            self.students[name] = newgrade
            print(f"Updated {name}'s grade to {self.student[name]}")
        else:
            print(f"{name} is not found in the dataset")
    def main():
        studentdb = StudentDatabase()
        while True:
            print("\nOptions")
            print("1. Add a student")
            print("2. Search for a student")
            print("3. Update a student's grade")
            print("4. Exit")
            choise = input("Enter your input(1-4): ")
            if choise == 1:
                name = input("Enter the name: ")
                grade = input("Enter the grade: ")
                studentdb.addStudent(name,grade)
            elif choise == 2:
                name = input("Enter the student name to search: ")
                studentdb.searchStudent(name)
            elif choise == 3:
                name = input("Enter the name of the student to update grade: ")
                grade = input("Enter the new grade: ")
                studentdb.updateStudent(name,grade)
            elif choise ==4:
                print("Exiting the program.")
                break
            else:
                print("Invalid Input")
    if __name__=="__main__":
        main()


