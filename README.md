# Student Performance Analysis using NumPy

## 📌 Project Overview

Student Performance Analysis is a beginner-friendly Python project created to practice NumPy and basic data analysis. It stores marks for 10 students across 5 subjects in a 2D NumPy array and performs calculations about student and subject performance.

The project uses a Python class and methods to display marks, calculate statistics, identify high and low performers, assign grades, and determine Pass/Fail results.

## ✨ Features

- Display marks for all students
- Calculate total marks for each student
- Calculate average marks for each student
- Find the highest and lowest mark in the dataset
- Calculate overall mean, median, standard deviation, and variance
- Find the topper using total marks
- Find the lowest-scoring student using total marks
- Calculate subject-wise averages
- Find the highest mark for each student
- Find the lowest mark for each student
- Assign grades based on each student's average
- Determine whether each student passed or failed
- Display a student performance report

## 🛠️ Technologies Used

- Python
- NumPy
- VS Code

## 🧠 NumPy Concepts Used

The project uses these NumPy functions:

| Function | Use in the project |
| --- | --- |
| `np.array()` | Stores the student marks in a 2D array. |
| `np.sum()` | Calculates student totals. |
| `np.mean()` | Calculates student, subject, and overall averages. |
| `np.median()` | Calculates the overall median mark. |
| `np.std()` | Calculates standard deviation. |
| `np.var()` | Calculates variance. |
| `np.max()` | Finds the highest mark. |
| `np.min()` | Finds the lowest mark. |
| `np.argmax()` | Finds the position of the student with the highest total. |
| `np.argmin()` | Finds the position of the student with the lowest total. |
| `np.all()` | Checks whether all marks for a student meet the passing mark. |

### Understanding `axis`

- `axis=1` performs calculations row by row. Here, each row represents one student, so it is used for each student's total, average, highest mark, and lowest mark.
- `axis=0` performs calculations column by column. Here, each column represents one subject, so it is used to calculate the average for each subject.

## 📊 Subjects and Student Data

The project analyzes marks for 10 students in these 5 subjects:

| Subject | Meaning in the data |
| --- | --- |
| Math | Mathematics marks |
| Physics | Physics marks |
| Chemistry | Chemistry marks |
| English | English marks |
| Computer | Computer marks |

The marks are stored in a 2D NumPy array. Each row contains the marks of one student, and each column contains the marks for one subject.

## ⚙️ How the Project Works

1. The `StudentAnalysis` class creates the subject list and the marks array.
2. The program displays the complete marks array.
3. Row-wise calculations find each student's total, average, highest mark, and lowest mark.
4. Overall calculations find the mean, median, standard deviation, and variance for all marks.
5. Student totals are used to identify the topper and the lowest-scoring student.
6. Column-wise calculations find the average mark for each subject.
7. Each student's average is used to assign a grade:
	- `A+`: 90 or above
	- `A`: 80 to 89.99
	- `B`: 70 to 79.99
	- `C`: 60 to 69.99
	- `F`: below 60
8. A student receives `Pass` when all of their subject marks are at least 35. Otherwise, the result is `Fail`.
9. The program prints a final student performance report.

## 📁 Project Structure

```text
NUMPY-project/
│
├── Student's_result.py
└── README.md
```

## 🚀 How to Install and Run

1. Install Python.
2. Open the `NUMPY-project` folder in VS Code.
3. Open the VS Code terminal.
4. Install NumPy:

	```bash
	pip install numpy
	```

5. Run the existing Python file:

	```bash
	python "Student's_result.py"
	```

## 🖥️ Example Output

The values below are based on the marks currently stored in the project:

```text
Total Students : 10
Overall Mean: 83.24
Overall Median: 84.5
Standard Deviation: 10.312245148366092
Variance: 106.34240000000001

Highest Mark: 100
Lowest Mark: 60
Student Topper: Student 10
Total: 487
Lowest Score student:Student 4
Total: 335
```

The program also prints the full marks array, individual student totals and averages, subject averages, grades, and Pass/Fail results.

## 📚 What I Learned

- How to create and use a 2D NumPy array
- How to perform mathematical and statistical calculations with NumPy
- How `axis=0` and `axis=1` affect array calculations
- How to use Python classes and methods
- How to analyze student and subject performance
- How to use conditions to assign grades and results

## 🔮 Future Improvements

The following are planned improvements and are not currently implemented:

- Accept marks from user input or a file
- Add input validation for marks
- Display the report in a more organized table
- Add charts for comparing student and subject performance
- Allow the number of students and subjects to be changed easily

## 👤 Author

**Archana R**