required_skills = input().strip().split(',')
candidate_skills = input().strip().split(',')

# Filter out empty strings if any
required_skills = [s for s in required_skills if s]
candidate_skills = [s for s in candidate_skills if s]

matched = 0
for skill in required_skills:
    if skill in candidate_skills:
        matched += 1

if required_skills:
    percentage = (matched / len(required_skills)) * 100
else:
    percentage = 0.0

print(f"Skills matched: {matched}/{len(required_skills)}")
print(f"Match percentage: {percentage:.1f}%")
