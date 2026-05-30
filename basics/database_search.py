n = int(input().strip())

database = []
for _ in range(n):
    name = input().strip()
    skills = input().strip().split(',')
    exp = int(input().strip())
    database.append({'name': name, 'skills': skills})

search_skill = input().strip()

matching_candidates = []
for candidate in database:
    if search_skill in candidate['skills']:
        matching_candidates.append(candidate['name'])

print(f"Candidates with {search_skill}: {matching_candidates}")
