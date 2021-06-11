kor, eng, math, science = 100, 86, 81, 91

def get_max_score(*args):
    score = 0
    for i in args:
        if score < i:
            score = i
    return score

max_score = get_max_score(kor, eng, math, science)
print(max_score)
max_score = get_max_score(eng, science)
print(max_score)