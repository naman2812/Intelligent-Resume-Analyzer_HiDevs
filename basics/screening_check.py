python_skill = input().strip().lower() == 'yes'
degree = input().strip().lower() == 'yes'
experience = int(input().strip())

if (python_skill and degree) or (python_skill and experience >= 3):
    print("Qualified for the job!")
else:
    print("Does not meet requirements")
