# 3 "decent"
# 4 "good"
# 5 "great"

class student:
    def __init__(self, name, gender, grade):
        self.name = name
        self.gender = gender
        self.grade = grade
        
    def check_grade_and_gender(self):
        cond1 = self.grade == "good"
        cond2 = self.grade == "great"
        cond3 = self.gender == "male"
        if (cond1 or cond2) and cond3:
            return self.name
        
student1 = student("aaron", "male", "good")
student2 = student("avraam", "male", "decent")
student3 = student("agafia", "female", "great")
student4 = student("aglaia", "female", "decent")

students = []
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)

res = []
for i in students:
    name = i.check_grade_and_gender()
    if name != None:
        res.append(name)

if len(res) != 0:
    print("Yes!")
    for i in res:
        print(i)
        