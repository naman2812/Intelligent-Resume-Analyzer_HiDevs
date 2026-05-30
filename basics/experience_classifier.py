exp = float(input().strip())

if exp < 0:
    level = "Invalid"
elif 0 <= exp < 2:
    level = "Fresher"
elif 2 <= exp < 4:
    level = "Junior"
elif 4 <= exp < 7:
    level = "Mid-Level"
else:
    level = "Senior"

print(f"Experience level: {level}")
