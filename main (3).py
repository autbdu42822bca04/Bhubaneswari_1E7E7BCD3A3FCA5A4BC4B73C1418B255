class Student:
  def __init__(self,name,roll_number,cgpa):
      self.name=name
      self.roll_number=roll_number
      self.cgpa=cgpa
def sort_students(student_list):
      sorted_students=sorted (student_list,key=lambda student:student.cgpa, reverse=True)
      return sorted_students

students=[
  Student("priya","A123",8.9),
  Student("jeya","A124",9.1),
  Student("varsha","A125",9.9)
]

sorted_students = sort_students(students)
for student in sorted_students:
  print("name:{},roll_number:{},cgpa:{}". format(student.name,student.roll_number,student.cgpa))


    