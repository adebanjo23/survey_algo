import collections

question_data = [
    ("Do you enjoy solving puzzles, finding patterns, breaking down problems, and figuring things out with data?", (0.35, 0.33, 0.30, 0.32)),
    ("Can you evaluate arguments and identify faulty logic?", (0.34, 0.30, 0.25, 0.32)),
    ("Are you comfortable working with numbers and formulas?", (0.37, 0.35, 0.28, 0.33)),
    ("Do you stay persistent and motivated even when faced with difficulties?", (0.36, 0.32, 0.28, 0.37)),
    ("Are you comfortable learning from theoretical concepts and textbooks?", (0.33, 0.30, 0.26, 0.33)),
    ("Do you notice subtle patterns and discrepancies in data?", (0.35, 0.38, 0.33, 0.32)),
    ("Can you objectively analyze data and draw unbiased conclusions?", (0.38, 0.39, 0.32, 0.38)),
    ("Are you comfortable working with large datasets and remembering complex information?", (0.32, 0.34, 0.29, 0.31)),
    ("Can you stay motivated and productive even without constant supervision?", (0.34, 0.31, 0.32, 0.34)),
    ("Can you collaborate effectively with people from diverse backgrounds and skillsets?", (0.34, 0.37, 0.30, 0.35)),
    ("Do you learn from your mistakes and bounce back stronger?", (0.36, 0.34, 0.35, 0.37)),
    ("Are you open to experimenting with different approaches and strategies?", (0.39, 0.35, 0.32, 0.40)),
    ("Are you comfortable stepping outside your comfort zone and learning new skills?", (0.40, 0.38, 0.36, 0.40)),
    ("Can you ensure the quality and reliability of your work?", (0.40, 0.40, 0.40, 0.40)),
    ("Are you able to communicate complex technical concepts clearly and concisely?", (0.40, 0.40, 0.35, 0.40)),
    ("How comfortable are you with mathematical concepts, statistics, and calculations?", (0.40, 0.40, 0.30, 0.33)),
    ("Have you taken courses in computer science and programming, including languages like Python, R, Java, etc.?", (0.38, 0.36, 0.39, 0.34)),
    ("Do you have a background in natural sciences or engineering, such as physics, chemistry, or computer engineering?", (0.33, 0.28, 0.24, 0.34)),
    ("Do you have a background in social sciences or humanities, such as economics, psychology, or history?", (0.34, 0.37, 0.21, 0.30)),
    ("Are you familiar with popular data analysis software and tools like Tableau, Power BI, SQL, or TensorFlow?", (0.32, 0.32, 0.34, 0.30)),
    ("Have you participated in any hackathons, data science competitions, or research projects related to data analysis?", (0.36, 0.32, 0.27, 0.32)),
    ("Are you curious about the stories data can tell and the insights it can reveal?", (0.40, 0.36, 0.26, 0.32)),
    ("Can you interpret charts, graphs, and other data visualizations effectively?", (0.37, 0.34, 0.26, 0.31)),
    ("Do you have an interest in learning how to code and build software applications?", (0.33, 0.28, 0.34, 0.35)),
    ("Are you excited about the potential of data to drive innovation and change?", (0.39, 0.36, 0.31, 0.36)),
    ("Does the prospect of a data-driven career excite you more than other potential career paths?", (0.39, 0.35, 0.30, 0.35))
]

fields = ["Data Science", "Data Analytics", "Data Engineering", "AI"]
field_weights = collections.defaultdict(list)

for question, weights in question_data:
    for field, weight in zip(fields, weights):
        field_weights[field].append((question, weight))


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
