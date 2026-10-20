import matplotlib.pyplot as plt

subjects = ['Maths', 'Science', 'English', 'Computer']
marks = [85, 90, 75, 95]

plt.bar(subjects, marks, color='purple')
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()