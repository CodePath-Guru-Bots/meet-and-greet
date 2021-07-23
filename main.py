import os
from dates import get_rotation, tf_initial_date

BOT_TOKEN = os.environ['BOT_TOKEN']
students = list('abcdefgh')

def create_pairs(students):
  """ 
  Create pairs of students will meet up this week.
  We accomplish this by shifting the first student to the end of the line
  """
  rotation = get_rotation(tf_initial_date)

  for n in range(rotation):
    # Rotate meetups (i.e. shift student 'a' to the end of array)
    students.append(students.pop(0))  


  # Create new pairs
  pairs = [(students[x], students[-x-1]) for x in range(len(students)//2)]
  print("\nStudents this week ->", students, "\n Meeting this week:", pairs)

if __name__ == "__main__":
  create_pairs(students)

