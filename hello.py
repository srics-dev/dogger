# Prompt the user to enter the number of scores
n = int(input("Enter the number of scores: "))

# Prompt the user to enter the scores
input_str = input("Enter space-separated scores: ")

# Convert the input string to a list of integers using map
scores = list(map(int, input_str.split()))

# Sort the list of scores in descending order
scores.sort(reverse=True)

# Find the runner-up score
runner_up_score = None
for score in scores:
    print(score,scores)
    if score < scores[0]:
        runner_up_score = score
        break

# Print the runner-up score
if runner_up_score is not None:
    print("The runner-up score is:", runner_up_score)
else:
    print("There is no runner-up score.")
