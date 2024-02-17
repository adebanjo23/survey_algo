import collections

question_data = [
    ("Do you enjoy solving puzzles, finding patterns, breaking down problems, and figuring things out with data?", (0.35, 0.33, 0.30, 0.32)),
    ("Can you evaluate arguments and identify faulty logic?", (0.34, 0.30, 0.25, 0.32)),
    ("Are you comfortable working with numbers and formulas?", (0.37, 0.35, 0.28, 0.33)),
]

fields = ["Data Science", "Data Analytics", "Data Engineering", "AI"]
field_weights = collections.defaultdict(list)

for question, weights in question_data:
    for field, weight in zip(fields, weights):
        field_weights[field].append((question, weight))

print(field_weights)
def ask_questions():
    scores = collections.defaultdict(int)
    # Store responses for each question
    responses = {}
    for question, weight in question_data:
        while True:
            response = input(f"{question} (Very Confident/Confident/Not Confident/Not at all Confident): ").lower()
            if response in ["very confident", "confident", "not confident", "not at all confident"]:
                responses[question] = response
                break
            else:
                print("Invalid response")

    # Calculate scores based on responses
    for field, questions in field_weights.items():
        for question, weight in questions:
            scores[field] += weight * {
                "very confident": 0.8,
                "confident": 0.5,
                "not confident": 0.2,
                "not at all confident": 0.0,
            }[responses[question]]
    return scores


def display_results(scores):
    max_scores_per_field = {
        field: sum(weight * 0.8 for _, weight in weights)  # Calculate max score assuming all "very confident" responses
        for field, weights in field_weights.items()
    }

    results = [(field, (score / max_scores_per_field[field]) * 100) for field, score in scores.items()]
    results.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommended Fields (in order of likelihood of success):\n")
    for field, percentage in results:
        print(f"{field}: {percentage:.2f}%")


# max_scores_per_field = {
#         field: sum(weight * 0.8 for _, weight in weights)  # Calculate max score assuming all "very confident" responses
#         for field, weights in field_weights.items()
#     }
# print(max_scores_per_field)
scores = ask_questions()
print(scores)
display_results(scores)
