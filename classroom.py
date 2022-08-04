class Student:
    def __init__(self, name, courses, grades):
        self.name=name
        self.courses=courses
        self.grades=grades

    def gpa(self):
        sum=0
        for grade in self.grades:
            sum=sum+grade
        gpa=sum/len(self.grades)
        return gpa

    #Returns if two students share a class      
    def shared_classes(self, other):
        for course in self.courses:
            for other_courses in other.courses:
                if (course==other_courses):
                    print("You share a course: " +course)
                    return
        print("You do not share a course")


alice=Student("Alice", ["Literature", "Calculus", "Computer Science"], [88, 87, 91])
gregory=Student("Gregory", ["Computer Science", "Algebra", "Chemistry"], [92, 84, 60])
brian=Student("Brian", ["World History", "Calculus", "Chemistry"], [95, 91, 87])