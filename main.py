
# Multi-Event Sports Scheduling and Scoring

# Event schedule stored as tuples inside a list
# (Event, Day, Time, Venue, Teams)

schedule = [
    ("Football", "Monday", "09:00", "Ground A",
     ("Falcons", "Tigers")),
    ("Basketball", "Monday", "09:00", "Court A",
     ("Lions", "Eagles")),
    ("Volleyball", "Monday", "10:00", "Ground B",
     ("Falcons", "Lions")),
    ("Cricket", "Tuesday", "09:00", "Ground A",
     ("Tigers", "Eagles")),
    ("Badminton", "Monday", "09:00", "Court B",
     ("Falcons", "Eagles"))
]

# Scores stored as tuples
# (Event, Team, Points)

scores = [
    ("Football", "Falcons", 3),
    ("Football", "Tigers", 0),
    ("Basketball", "Lions", 2),
    ("Basketball", "Eagles", 1),
    ("Volleyball", "Falcons", 2),
    ("Volleyball", "Lions", 1),
    ("Cricket", "Tigers", 3),
    ("Cricket", "Eagles", 0),
    ("Badminton", "Falcons", 1),
    ("Badminton", "Eagles", 2)
]


# Display event schedule
def display_schedule():
    print("\n===== EVENT SCHEDULE =====")

    for event in schedule:
        print(event)


# Identify scheduling conflicts
def check_conflicts():
    print("\n===== SCHEDULING CONFLICTS =====")

    found = False

    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):

            first = schedule[i]
            second = schedule[j]

            if first[1] == second[1] and first[2] == second[2]:

                if first[3] == second[3]:
                    print("Venue Conflict:",
                          first[0], "and", second[0])
                    found = True

                for team in first[4]:
                    if team in second[4]:
                        print("Team Conflict:",
                              team, "in", first[0],
                              "and", second[0])
                        found = True

    if not found:
        print("No scheduling conflicts found.")


# Calculate total points
def calculate_points():
    totals = {}

    for event, team, points in scores:

        if team not in totals:
            totals[team] = 0

        totals[team] += points

    return totals


# Generate final rankings
def display_rankings(totals):
    print("\n===== FINAL TEAM RANKINGS =====")

    ranking = sorted(
        totals.items(),
        key=lambda item: (-item[1], item[0])
    )

    position = 1

    for team, points in ranking:
        print(position, ".", team, "-", points, "points")
        position += 1


# Main function
def main():
    display_schedule()

    check_conflicts()

    totals = calculate_points()

    display_rankings(totals)

    print("\nProgram completed successfully.")


main()
