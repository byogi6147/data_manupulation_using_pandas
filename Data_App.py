# a=[5,10,18,15,25, "Python"]
# for x in a:
#     if not isinstance(x, int):
#         a.remove(x)
#     elif  (x % 5 )!=0:
#         a.remove(x)
#
# print(sum(a))


a=[1,2,3,4,5,11,12,6]
b=[3,4,5,6]

u =[]

for i in range(len(a)-1,-1,-1):
    if( a[i] in b):
        a.pop(i)

final = (a + b)
final.sort(reverse=True)

print(final)

number_of_student = int(input("Provide total number of student: "))
student_marks ={}

for x in range(number_of_student):
    name = input("provide the name of the student: ")
    num_of_subjects = int(input("Provide number of subjects: "))
    subject_dict = {}
    for y in range(num_of_subjects):
        subject = input("Subject name: ")
        marks = int(input("Marks: "))
        temp_subject_dict = {subject:marks}
        subject_dict.update(temp_subject_dict)
    print(subject_dict)
    temp_student_marks ={name:subject_dict}
    student_marks.update(temp_student_marks)

print(student_marks)

