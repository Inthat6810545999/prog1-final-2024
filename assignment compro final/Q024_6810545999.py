# Name: Inthat # Student ID: 68010545999

f = open("scores.txt" , "r" , encoding = "utf-8")
score = f.read()
score = score.splitlines()

socrelist = []

for sc in score:
    sc1 = sc.split(",")
    socrelist.append(sc1)



top_student = ""
max_score = "0"

for n,m in socrelist:
    current_score = m
    if current_score > max_score:
        max_score = current_score
        top_student = n

total = 0
avg = 0

for score in socrelist:
    total += float(score[1])

avg = total / len(socrelist)

print("--- Score Analysis ---")
print(f"Class Average: {avg:.2f}")
print(f"Highest Score: {top_student} with {max_score} points.")