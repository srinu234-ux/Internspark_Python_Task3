import pandas as pd
data = {
    "Student_ID": range(1, 11),
    "Department": [
        "CSE", "ECE", "CSE", "EEE", "ME",
        "CSE", "ECE", "EEE", "CSE", "ME"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    "Attendance": [92, 85, 78, 88, 95, 76, 82, 90, 73, 91],
    "Marks": [88, 76, 69, 82, 91, 65, 72, 85, 61, 87]
}
df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)

print("=" * 50)
print("TASK 3 - PANDAS DATA ANALYSIS")
print("=" * 50)
df = pd.read_csv("student_data.csv")

print("\n1. DATASET")
print(df)
print("\n2. MISSING VALUES")
print(df.isnull().sum())
df = df.drop_duplicates()

print("\n3. DATA AFTER CLEANING")
print(df)
high_marks = df[df["Marks"] > 80]

print("\n4. STUDENTS WITH MARKS ABOVE 80")
print(high_marks)
good_attendance = df[df["Attendance"] > 85]

print("\n5. STUDENTS WITH ATTENDANCE ABOVE 85%")
print(good_attendance)
department_analysis = df.groupby("Department")[["Attendance", "Marks"]].mean()

print("\n6. AVERAGE ATTENDANCE AND MARKS BY DEPARTMENT")
print(department_analysis)
print("\n7. SUMMARY STATISTICS")
print(df.describe())
top_student = df.loc[df["Marks"].idxmax()]

print("\n8. TOP-PERFORMING STUDENT")
print(top_student)
lowest_student = df.loc[df["Marks"].idxmin()]

print("\n9. LOWEST-PERFORMING STUDENT")
print(lowest_student)
print("\n10. KEY INSIGHTS")

print(f"- Average marks: {df['Marks'].mean():.2f}")
print(f"- Average attendance: {df['Attendance'].mean():.2f}%")
print(f"- Highest marks: {df['Marks'].max()}")
print(f"- Lowest marks: {df['Marks'].min()}")

best_department = (
    df.groupby("Department")["Marks"]
    .mean()
    .idxmax()
)

print(f"- Department with highest average marks: {best_department}")

print("\nAnalysis completed successfully!")

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.bar(df["Student_ID"], df["Marks"])
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.savefig("student_marks.png")
plt.show()

avg_marks = df.groupby("Department")["Marks"].mean()

plt.figure(figsize=(8, 5))
avg_marks.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Average Marks by Department")
plt.xticks(rotation=0)
plt.savefig("average_marks_department.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.savefig("attendance_vs_marks.png")
plt.show()

print("\nGraphs created successfully!")
