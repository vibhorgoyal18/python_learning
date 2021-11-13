# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

min_score = scores[0]
max_score = scores[0]
min_score_broken_times = 0
max_score_broken_times = 0
for score in scores:
    if score > max_score:
        max_score_broken_times +=1
        max_score = score
    elif score < min_score:
        min_score_broken_times +=1
        min_score = score

print(f"{max_score_broken_times} {min_score_broken_times}")
