import collections

question_data = [
    ("Do you enjoy solving puzzles, finding patterns, breaking down problems, and figuring things out with data?", [
        (0.6, 0.25, 0.1, 0.05),   # Very Confident
        (0.4, 0.35, 0.15, 0.1),  # Confident (Data Analytics)
        (0.25, 0.25, 0.3, 0.2),  # Not Confident (Data Engineering)
        (0.1, 0.2, 0.35, 0.35),  # Not at all Confident (AI)
    ]),
    ("Can you evaluate arguments and identify faulty logic?", [
        (0.3, 0.2, 0.8, 0.7),  # Very Confident (AI)
        (0.4, 0.3, 0.7, 0.6),  # Confident (Data Engineering)
        (0.7, 0.5, 0.3, 0.1),  # Not Confident (Data Science)
        (0.8, 0.6, 0.4, 0.2),  # Not at all Confident (Data Analytics)
    ]),
    ("Are you comfortable working with numbers and formulas?", [
        (0.8, 0.6, 0.4, 0.2),  # Very Confident (Data Analytics)
        (0.7, 0.5, 0.3, 0.1),  # Confident (Data Science)
        (0.5, 0.4, 0.6, 0.5),  # Not Confident (Data Engineering)
        (0.3, 0.2, 0.8, 0.7),  # Not at all Confident (AI)
    ]),
]

fields = ["Data Science", "Data Analytics", "Data Engineering", "AI"]
field_weights = collections.defaultdict(list)

for question, weights in question_data:
    for i, (field, weight) in enumerate(zip(fields, weights)):
        # Extract the desired elements based on field index
        extracted_weight = weight[i]
        field_weights[field].append((question, extracted_weight))

print(field_weights)