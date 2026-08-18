def calculate_readiness(hours, python, ai_interest):
    score = 0

    if hours >= 7:
        score += 40
    elif hours >= 4:
        score += 25
    else:
        score += 10

    if python:
        score += 30

    if ai_interest:
        score += 30

    return score


print("=== AI Learning Readiness Checker ===")
hours = float(input("How many hours per week can you study? "))
python_answer = input("Do you know basic Python? (yes/no): ").strip().lower()
ai_answer = input("Are you interested in learning AI? (yes/no): ").strip().lower()

python_known = python_answer == "yes"
ai_interested = ai_answer == "yes"

score = calculate_readiness(hours, python_known, ai_interested)

print(f"\nReadiness score: {score}/100")

if score >= 80:
    print("Excellent — you are ready to continue with structured AI learning.")
elif score >= 50:
    print("Good start — strengthen Python fundamentals and continue.")
else:
    print("Start with consistent Python practice and build your foundation.")
