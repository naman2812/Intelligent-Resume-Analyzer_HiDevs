python_skill = input().strip() == 'True'
experience = int(input().strip())
degree = input().strip() == 'True'

score = 50.0

if python_skill:
    score += 10.0

exp_bonus = experience * 5
if exp_bonus > 20:
    exp_bonus = 20
score += exp_bonus

if degree:
    score *= 1.1

print(f"Final match score: {score:.1f}")
