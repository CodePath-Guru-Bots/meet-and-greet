
from datetime import date

# Can be dynamic by creating an API server

def get_rotation(initial_date: date) -> int:
  """
  Gets the amount of weeks that has passed since `initial_date` using the start date.
  """
  current_date = date.today()
  weeks_since = abs(current_date - initial_date).days // 7
  return weeks_since


if __name__ == "__main__":
  initial_date = date(2021,8,1)
  weeks_passed = get_rotation(initial_date=initial_date)
  print("Weeks passed:", weeks_passed)
