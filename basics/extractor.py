name = input().strip()
age = int(input().strip())
experience = float(input().strip())
knows_python_str = input().strip()
knows_python = True if knows_python_str == 'True' else False
skills_str = input().strip()
skills = [s.strip() for s in skills_str.split(',')]

print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"Experience: {experience} ({type(experience).__name__})")
print(f"Knows Python: {knows_python} ({type(knows_python).__name__})")
print(f"Skills: {skills} ({type(skills).__name__})")
