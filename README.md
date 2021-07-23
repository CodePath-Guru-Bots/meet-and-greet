# TF Meet and Greet Bot

##### `Source` [hackmd.io/](https://hackmd.io/j8FV3tJtTAisG3tzhdmZcg)
#### `Mission:` Build community relationships amongst TFs
#### `Other Goals:` create serendipity, increase awareness of student's lives, learn from each other

[](https://)
## Requirements

- Get all users from all-tf-announcements (https://api.slack.com/methods/users.list)
- Choose 2 TFs at random from there
- Crate a dm between those students
- Bot will say "Welcome to CodePath's meet and greet bot. Feel free to introduce yourselves and setup a zoom chat between the two of you :)"

Bonuses
- ✅ Do not allow people from the same school

# Scope

- Meeting TFs:
    build community by havibg the TFs have a 15 min talk 
    -zoom link
    -calander so they can see the schedule 


- for TF training a use case is:
    meet other iOS TFs to increase networking 
    
    pods -3 people 
    - TF training anouncments 
    - starter projects 
    - assign HW 
        - turn in their project 

Classes
```
Class Student
 - name 
 - userid 
 - (maybe School) if we want to make sure matches do not have same schools 
```

Main Methods
```
get_user_list() - so can be reused for ios and, cyb all tf
 """gets the list of users from specific user-groups (i.e. @new-ios-tfs-fall2021)"""

create_group_dm()
""" Takes in array of students and 
creates a dm in groups of two"""
```


