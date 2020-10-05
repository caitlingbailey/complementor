#takes in an array of score answers for an individual and outputs their score
#score array has 50 numeric answers on a scale 1-5
#Each score output is in the range [-45,45]
def scorecalculator(answers):

    score=[]

    #iterate over 5 sets of 10 questions, 1 set per characteristic
    for j in range(0,4):
        #e is temp variable to add up each score
        E=0

        #iterate over each question and add or subtract from score accordingly
        for i in range(0+10*j,10+10*j,2):
            E=E+answers[i]
        for i in range(1+10*j,10+10*j,2):
            E=E-answers[i]

        #chracteristics 2 and 4 the +/- questions are the other way round
        if j%2==0:E=-E

        #store the score for this characteristic
        score.append(E)
    return(score)

#Calculates difference score for each potential pair
#A is the score of the mentee, B is the score of the mentor
def differencescore(A,B):

    ds=0
    for i in range(0,4):
        ds=ds+(A[i]-B[i])

        if ds<0:
            ds=-ds

    return(ds)

#Selects three mentors for the mentee
#A is the score of the mentee, B is the array of scores of the potential mentor
def matching(A, B):
    mentors = []

    # counter for iterating over mentors/id of mentors
    i = 0

    try:
        while len(mentors)<3 and i<100:
            difference = differencescore(A,B[i])
            if difference>40.0:
                mentors.append(i)

            i=i+1

        while len(mentors)<3 and i<1000:
            difference = differencescore(A,B[i])
            if difference>35.0:
                mentors.append(i)

            i=i+1

        while len(mentors)<3 and i<len(B):
            difference = differencescore(A,B[i])
            if difference>25.0:
                mentors.append(i)

            i=i+1

    except:return mentors

    return mentors
