
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_performance.csv")

# Display dataset
print("Student Performance Data:")
print(data)

# Basic analysis
print("\nAverage Marks:", data["Marks"].mean())
print("Average Attendance:", data["Attendance"].mean())

# Find top student
top_student = data.loc[data["Marks"].idxmax()]

print("\nTop Student:")
print(top_student)

# Bar Chart - Student Marks
plt.figure()
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("marks_chart.png")
plt.show()

# Histogram - Marks Distribution
plt.figure()
plt.hist(data["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig("marks_histogram.png")
plt.show()

# Pie Chart - Attendance
above_75 = (data["Attendance"] >= 75).sum()
below_75 = (data["Attendance"] < 75).sum()

plt.figure()
plt.pie(
    [above_75, below_75],
    labels=["75% and Above", "Below 75%"],
    autopct="%1.1f%%"
)
plt.title("Attendance Distribution")
plt.savefig("attendance_pie.png")
plt.show()

# Attendance and Marks relationship
correlation = data["Attendance"].corr(data["Marks"])

print("\nAttendance-Mark Correlation:", correlation)

if correlation > 0:
    print("Higher attendance is associated with higher marks.")
else:
    print("No positive relationship was found.")
