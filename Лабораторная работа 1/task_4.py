visits = ["user1", "user2", "user1", "user3", "user3", "user2"]

stats = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

stats["Общее количество"] = len(visits)
stats["Уникальные посещения"] = len(set(visits))

print(stats)
