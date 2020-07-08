import os
import csv

#open the path
path=os.path.join('Election_Data.csv')
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header/first row
    csvhead=next(csvreader)

    #identify variables & create lists
    candidates=[]
    votes=[]
    num_votes=[]
    per_votes=[]
    votes_cand=0
    total_votes=[]
    percent_votes=0
    most_votes=0

    #Importing list of votes
    for vote in csvreader:
        total_votes.append(vote[2])

    

#Total Votes Acquired
print(len(total_votes))


#Total Votes by Candidate
Khan = []
OTooley= []
Correy= []
Li= []

for votes in total_votes:
    if votes=="Khan":
        Khan.append(votes)
    if votes=="OTooley":
        OTooley.append(votes)
    if votes=="Correy":
        Correy.append(votes)
    if votes=="Li":
        Li.append(votes)       
#print(len(Khan))
#Percentages 

KhanPerc=len(Khan)/len(total_votes)
KhanPerc = KhanPerc * 100
KhanPerc = "{:.2f}".format(KhanPerc)
print("Khan received "+str(KhanPerc))

OTooleyPerc=len(OTooley)/len(total_votes)
OTooleyPerc= OTooleyPerc * 100
OTooleyPerc = "{:.2f}".format(OTooleyPerc)
print("OTooley recieved "+str(OTooleyPerc))

LiPerc=len(Li)/len(total_votes)
LiPerc= LiPerc * 100
LiPerc = "{:.2f}".format(LiPerc)
print("Li recieved "+str(LiPerc))

CorreyPerc=len(Correy)/len(total_votes)
CorreyPerc= CorreyPerc * 100
CorreyPerc = "{:.2f}".format(CorreyPerc)
print("Correy recieved "+str(CorreyPerc))

# def get_percentage(name):
#    Average = len(name)/len(total_votes)
#    Average = Average * 100
#    name = len(name)
#    Average = "{:.2f}".format(name)
#    return(Average)
#    print("The percentage of the vote for" +str(name) + "is "+str(Average) )


# get_percentage(Khan)
#Winner











