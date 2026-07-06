players = [
    {"name": "Zex", "score": 1500, "time_seconds": 340},
    {"name": "Kalo", "score": 1500, "time_seconds": 290},
    {"name": "Ryn", "score": 1800, "time_seconds": 400},
    {"name": "Vex", "score": 1200, "time_seconds": 150},
    {"name": "Nia", "score": 1800, "time_seconds": 380},
    {"name": "Tob", "score": 1500, "time_seconds": 290},
]

sorted_players = sorted(
    players, key=lambda player: (-player["score"], player["time_seconds"])
)

for number, item in enumerate(sorted_players, start=1):
    print(
        f"Rank {number}. {item['name']} - score: {item['score']} - time: {item['time_seconds']}"
    )


top_players = list(filter(lambda player: player["score"] >= 1500, players))
fastest = min(top_players, key=lambda top_player: top_player["time_seconds"])

print("\nTop players with a score of 1500 and higher")
for number, item in enumerate(top_players, start=1):
    print(
        f"{number}. {item['name']} - score: {item['score']} - time: {item['time_seconds']}"
    )

print("\nPlayer with the fastest time")
print(f"{fastest['name']} with a time of {fastest['time_seconds']}")
