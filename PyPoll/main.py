import os
import csv
totes_votes = 0
candidate_votes = {}
person = ''
vote_count = []
vote_percent =[]
winner_name =''
winner_count = 0
# reading in my CSV
csvpath = os.path.join('Resources', 'election_data.csv')
with open (csvpath, newline='') as election_data:
    csvreader = csv.reader(election_data, delimiter= ',')
    #next csv read slipts the header from the table to give us just the data
    next(csvreader)
    #for loop to loop through and count the rows while also 
    for row in csvreader:
        totes_votes+=1
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else: 
            candidate_votes[row[2]] = 1
person = list(candidate_votes.keys())    
vote_count = list(candidate_votes.values())
for i in range(len(person)):
    vote_percent.append((vote_count[i] / totes_votes) * 100)

for i in range(len(vote_count)):
    if vote_count[i] > vote_count[winner_count]:
        winner_count = i

print("---Election Results---")
print("----------------------")
print(f"-Total Votes: {totes_votes}-")
print("----------------------")
for i in range(len(person)):
    print(f"{person[i]}: {round(vote_percent[i], 3)}% ({vote_count[i]})")
print("----------------------")
print(f"Winner: {person[winner_count]}")
print("----------------------")
output_path = os.path.join('Resources','election_data.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write("---Election Results---")
    txtfile.write("----------------------")
    txtfile.write(f"-Total Votes: {totes_votes}-")
    txtfile.write("----------------------")
    for i in range(len(person)):
        txtfile.write(f"{person[i]}: {round(vote_percent[i], 3)}% ({vote_count[i]})")
    txtfile.write("----------------------")
    txtfile.write(f"Winner: {person[winner_count]}")
    txtfile.write("----------------------")