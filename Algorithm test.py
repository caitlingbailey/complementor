import pandas as pd
from Subroutines import scorecalculator,matching, differencescore

'''testing mentor matching algorithm using a sample of 11,000 individuals answers to personality quiz. Sample is split into 1000 'mentees' and 10000 'mentors' '''

#read in the score csv
samplescores=pd.read_csv('data.csv',usecols=range(7,47))


#pulling samples of mentees/mentors
mentees=samplescores.head(1000)
mentees=mentees.values.tolist()
mentors=samplescores.tail(10000)
mentors=mentors.values.tolist()

#calculating scores for each test submission
menteesscores=[]
mentorscores=[]

for i in range(0,1000):
    score=scorecalculator(mentees[i])
    menteesscores.append(score)

for i in range(0,10000):
    score=scorecalculator(mentors[i])
    mentorscores.append(score)

#making sure each mentee has choice of 3 matches
matches=[]

for i in range(0,1000):
    matches.append(matching(mentorscores[i],mentorscores))

#return any mentees with less than 3 matches
for i in range(0,1000):
    if len(matches[i])<3:
        print(i,matches[i])

#check average final match to check efficiency
sum=0

for i in matches:
    sum=sum+(i[2])

print(sum/1000)
