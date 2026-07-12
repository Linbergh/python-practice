students = [
    {"name": "Ana", "scores": [88, 92, 79]},
    {"name": "Ben", "scores": [95, 91, 98]},
    {"name": "Cid", "scores": [60, 55, 70]},
    {"name": "Dax", "scores": [82, 82, 82]},
    {"name": "Eli", "scores": [70, 88, 95]},
    {"name": "Bins", "scores": [99, 98, 99]},
]


def get_average(score):
    return sum(score) / len(score)


enriched = []
for student in students:
    enriched.append(
        {
            "name": student["name"],
            "scores": student["scores"],
            "average": get_average(student["scores"]),
        }
    )

sorted_avg = sorted(enriched, key=lambda s: s["average"], reverse=True)
highest_score = max(enriched, key=lambda s: max(s["scores"]))
lowest_avg = min(enriched, key=lambda s: s["average"])


for index, student in enumerate(sorted_avg, start=1):
    print(f"Rank {index}: {student['name']} - avg {student['average']:.1f}")

print(
    f"\nHighest single score: {highest_score['name']} with {max(highest_score['scores'])}"
)
print(f"Lowest average: {lowest_avg['name']}")
