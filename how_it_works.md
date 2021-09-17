Knowledge Check

Figure out to make sure that each week we get a unique pair of students. 
Before learning the content below, do some research on:

- Intro to Combinations
- Combinations vs Permutations


Everything else I just googled my way through to understand and find the code to 
create unique pairs each week (examples below)

Practice creating tests of combinations with students ABCD and then ABCDEF.
Go through your head on how to create the combinations of 2 students.
Next step is to figure out to create pairs of combinations, example:

- Week 1 pairings --> AB CD


### 1st Test: ABCD

Using Combinations (python itertools <-- google this)

- 4 total people
- 6 combinations total
- 2 pairs per week
- 3 weeks for everyone to meet each other (6/2 = 3)

```
AB AC AD | BC BD | CD
1  2  3    4  5    6

1 AB CD     1, 6
2 AC BD     2, 5
3 AD BC     3, 4
```

How it should look in code
```
[{('A', 'B'), ('C', 'D')}, 
{('A', 'C'), ('B', 'D')}, 
{('A', 'D'), ('B', 'C')}]
```

-------


### 2nd Test: ABCDEF

- 6 people total
- 15 combinations total
- 3 pairs per week
- 5 pairings until everyone meets each other (15/3 = 5)

```
AB AC AD AE AF | BC BD BE BF | CD CE CF | DE DF | EF
1  2  3  4  5     6  7  8 9    10 11 12   13 14   15


1 AB CD EF        1, 10, 15 
2 AC BE DF        2, 8, 14
3 AD BC DE        3, 6, 13
4 AE BD CF        4, 7, 12
5 AF BF CE        5, 9, 11
```

I figured it out by this point through this link:
https://stackoverflow.com/questions/54200347/python-get-groups-of-combinations-that-each-member-appear-only-once








