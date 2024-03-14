import os 
import csv

#create path to electiondata csv file 
#used the full path due to it not being able to locate resources file
csv_path = 'C:\\Users\\riona\\pythonn-challenge\\PyPoll\\Resources\\election_data.csv'

# Initialize variables to store the total votes and candidate votes
total_votes = 0
candidate_votes = {}

#read csv file
with open(csv_path, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
 #create a loop through each row in the csv
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # Check if the candidate is in the dictionary, add a vote if they exist, or add them with one vote if not
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Create an empty dictionary to store the candidates' percentage of votes
candidate_percentages = {}

# Calculate the percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

#use max function to find the winner by popular votes
winner = max(candidate_votes, key=candidate_votes.get)

#print results in terminal 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save results to a text file
# https://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file used 5th responce
output_file = "election_results.txt"
with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        textfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")
