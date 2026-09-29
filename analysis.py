import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("students.csv")

# Calculate overall academic score
df["Average"] = df[["Maths", "Python", "ML"]].mean(axis=1).round(2)

# Performance category
def category(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    return "Needs Improvement"

df["Performance"] = df["Average"].apply(category)

# Display top students
print("\n===== TOP 5 STUDENTS =====")
print(df.sort_values("Average", ascending=False)[
    ["Name", "Branch", "Average", "Attendance", "Performance"]
].head())

# Branch-wise performance
branch_avg = df.groupby("Branch")["Average"].mean().sort_values(ascending=False)
print("\n===== BRANCH-WISE AVERAGE =====")
print(branch_avg.round(2))

# Basic insights
top_student = df.loc[df["Average"].idxmax()]
low_attendance = df.loc[df["Attendance"].idxmin()]

print("\n===== KEY INSIGHTS =====")
print(f"Top performer: {top_student['Name']} ({top_student['Average']:.2f} average)")
print(f"Lowest attendance: {low_attendance['Name']} ({low_attendance['Attendance']}%)")

# Chart 1: Student averages
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Performance")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_performance.png", dpi=150)
plt.show()

# Chart 2: Branch-wise average
plt.figure(figsize=(7, 5))
plt.bar(branch_avg.index, branch_avg.values)
plt.title("Average Performance by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("branch_performance.png", dpi=150)
plt.show()

# Export analyzed data
df.to_csv("analyzed_students.csv", index=False)
print("\nAnalyzed data saved as analyzed_students.csv")
