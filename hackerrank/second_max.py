scores = [10,50,30]
max_score=0
second_max_score=0
for score in scores:
    if score>max_score :
        second_max_score=max_score
        max_score=score
    elif score>second_max_score and score!= max_score:
        second_max_score =score
print("second runner up is :",second_max_score)
#the another simple method
scores = [10,20,30]
print(sorted(set(scores), reverse=True)[1])