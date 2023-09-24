class student:
  
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


  def sort_student(student_list):
  # sort the list of students in descending order of CGPA
  sort_students = sorted(student_list,
                       key=lambda student:stuent.cgpa
                       reverse=True)
  return sorted_students


#Example usage:
student=[
  student("Hari", "A123", 7.8),
  student("Srikanth", "A124", 8.9),
  student("Sowmiya", "A125", 9.1),
  student("Mahidhari", "A126", 9.9)
]

sorted_students = sort_student(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                    
student.roll_number,
                                            studemt.cgpa))