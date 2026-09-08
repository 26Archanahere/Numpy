import numpy as np

class StudentAnalysis:

    def __init__(self):
        self.subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]

        self.marks = np.array([
            [85, 90, 78, 88, 95],
            [72, 65, 80, 75, 70],
            [95, 92, 96, 94, 98],
            [60, 70, 65, 68, 72],
            [88, 84, 90, 85, 91],
            [76, 81, 79, 74, 80],
            [91, 89, 93, 90, 94],
            [69, 73, 71, 75, 78],
            [82, 80, 85, 83, 86],
            [97, 95, 99, 96, 100]
        ])

    # Display Marks
    def display_marks(self):
        print("\n------ Student Marks ------")
        print(self.marks)

    # Total Marks
    def total_marks(self):
        total = np.sum(self.marks, axis=1)
        print("\n------ Total Marks ------")
        for i, total in enumerate(total):
            print(f"Student {i+1}: {total}")
        return total


    #Average Marks
    def average_marks(self):
        averages = np.mean(self.marks, axis=1)
        print("\n------Average Marks------")
        for i, avg in enumerate(averages):
            print(f"Student {i+1}: {avg:.2f}")
        return averages


    #Highest Marks
    def highest_marks(self):
        print("\nHighest Mark:",np.max(self.marks))



    #Lowest Marks
    def lowest_marks(self):
        print("\nLowest Mark:",np.min(self.marks))



    #Overall Statistic
    def overall_statistic(self):
        print("\n-------Overall Statistic------")


    #overall mean    
    def overall_mean(self):
        mean = np.mean(self.marks)
        print("Overall Mean:",mean)
        return mean

    #overall median
    def overall_median(self):
        median = np.median(self.marks)
        print("Overall Median:",median)
        return median

    #Standard deviation
    def Standard_Deviation(self):
        std = np.std(self.marks)
        print("Standard Deviation:",std)
        return std


    
    #Variance
    def Variance(self):
        variance = np.var(self.marks)
        print("Variance:",variance)
        return variance

    

    #Student Topper
    def Topper(self):
        total = np.sum(self.marks, axis=1)
        topper =np.argmax(total)
        
        print("Student Topper: Student", topper + 1)
        print("Total:",total[topper])
        
        return topper



    #Lowest Score Student
    def Lowest_Score_Student(self):
        total = np.sum(self.marks, axis=1)
        lowest = np.argmin(total)
        
        print("Lowest Score student:Student", lowest + 1)
        print("Total:",total[lowest])
        
        return lowest



    #Subject Average
    def Subject_Average(self):
        subject_average = np.mean(self.marks, axis=0)
        
        print("\n------Subject Average------")
    
        
        for i, avg in enumerate(subject_average):
            print(f"{subject_average}: {avg:.2f}")
            
        return subject_average




    #Highest mark
    def Highest_Mark_Student(self):
        
          print("\n------Highest Marks in Each Student------")

          highest = np.max(self.marks, axis=1)


          for i, mark in enumerate(highest):
               print(f"Student {i+1}: {mark}")
               
          return highest
 
          

    #Lowest mark
    def Lowest_Mark_Student(self):
        
         print("\n------ Lowest Marks in Each Student------")

         lowest_mark = np.min(self.marks, axis=1) 

         for i, mark in enumerate(lowest_mark):
                  print(f"Student {i+1}: {mark}")

         return lowest_mark



    #Grade of each student
    def Grades(self):
        average = np.mean(self.marks, axis=1)


        print("\n------ Grades ------")

        for i, avg in enumerate(average):

            if avg >= 90:
                grade = "A+"
            elif avg >= 80:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 60:
                grade = "C"
            else:
                grade = "F"

            print(f"Student {i+1}: {grade}")
                  
                  

    #Result
    def Result(self):
        print("\n------Result------")

        for i in range(len(self.marks)):
           if np.all(self.marks[i] >= 35):
                result = "Pass"
           else:
                result = "Fail"


           print(f"Student {i+1}: {result}")



student = StudentAnalysis()



print("Total Students:",len(student.marks))

student.display_marks()

student.total_marks()

student.average_marks()

student.highest_marks()
student.lowest_marks()

student.overall_statistic()

student.overall_mean()
student.overall_median()
student.Standard_Deviation()
student.Variance()

student.Topper()
student.Lowest_Score_Student()

student.Subject_Average()

student.Highest_Mark_Student()
student.Lowest_Mark_Student()

student.Grades()

student.Result()





print("\n********************************************")
print("      STUDENT PERFORMANCE REPORT")
print("********************************************")

print("Total Students :", len(student.marks))
print("Overall Mean:",mean)
print("Overall Median:",median)
print("Standard Deviation:",std)
print("Variance:",variance)
print("Highest Mark:",highest)
print("Lowest Mark:",lowest)
print("Student Topper: Student", topper + 1)
print("Lowest Score student:Student", lowest + 1)

print("\nSubject Average")

print("************************************************")
