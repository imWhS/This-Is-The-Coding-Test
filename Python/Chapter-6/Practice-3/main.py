#성적이 낮은 순서로 학생 출력하기

def compare(data):
    return data[1]

N = int(input())
students = []
for i in range(N):
    student = input().split()
    students.append((student[0], int(student[1])))

students = sorted(students, key = lambda student: student[1])

for student in students:
    print(f"{student[0]} ", end = "")

