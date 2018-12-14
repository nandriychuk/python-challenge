# In this challenge, you are tasked with helping a small, 
# rural town modernize its vote-counting process. (Up until now, Uncle Cleetus 
# had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# Modules
import os
import csv

# Set path for csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Count the total number of votes
    data = list(csvreader)
    total_votes = len(data)

    #Create empty arrays for the new data
    candidates_row = []
    candidates = []
    vote_percent = []
    candidate_votes = []

#loop through data and append the candidates row to use later
for row in data:
    candidates_row.append(row[2])

#loop through the data to find the unique candidates and do the calculations
for value in set(candidates_row):
    #identifying unique candidates
    candidates.append(value)
    # print(value)

# print(candidates)
    # Counting total value of votes per candidate
    total_per_candidate = candidates_row.count(value)
    candidate_votes.append(total_per_candidate)
    # print(total_per_candidate)

    #     # percent of total votes per candidate
    percent = round((total_per_candidate /total_votes)*100,1)
    #print(percent)
    vote_percent.append(percent)
# print(vote_percent)
        
winning_count = max(candidate_votes)
winning_index = candidate_votes.index(winning_count)
winning_candidate = candidates[winning_index]
# print(winning_count)
# print(candidate_votes)
# print(vote_percent[0])

print(f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates[0]}: {vote_percent[0]}% ({candidate_votes[0]})
{candidates[1]}: {vote_percent[1]}% ({candidate_votes[1]})
{candidates[2]}: {vote_percent[2]}% ({candidate_votes[2]})
{candidates[3]}: {vote_percent[3]}% ({candidate_votes[3]})
--------------------------
Winner: {winning_candidate}
''')

with open("election_data.txt", 'w') as text:
    text.write(f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates[0]}: {vote_percent[0]}% ({candidate_votes[0]})
{candidates[1]}: {vote_percent[1]}% ({candidate_votes[1]})
{candidates[2]}: {vote_percent[2]}% ({candidate_votes[2]})
{candidates[3]}: {vote_percent[3]}% ({candidate_votes[3]})
--------------------------
Winner: {winning_candidate}
''')
