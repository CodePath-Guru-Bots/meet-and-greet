
# In progress

def test():
  date1, date2, date3, date4 = date(2021,9,7), date(2021,9,8), date(2021,9,9), date(2021,9,10)
  dates = [date1, date2, date3, date4]
  for d in dates:
    rotation = get_rotation(d)
    all_users = get_users(channel)
    rotated = rotate(all_users, rotation)
    user_pairs = create_user_pairs(rotated)
    print(rotated)
    print(user_pairs)