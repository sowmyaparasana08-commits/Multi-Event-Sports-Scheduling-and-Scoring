# Multi-Event-Sports-Scheduling-and-Scoring
# Multi-Event Sports Scheduling and Scoring

## Student Information

- **Name:** P.Sowmya
- **Roll Number:** N26V01A0316
- **Branch:** CSE
- **Section:** Section-4

## 1. Problem Statement

Develop a Python program to represent multiple sports event schedules and team scores using lists and tuples. The program identifies scheduling conflicts, aggregates points earned by teams, and generates final team rankings.

## 2. Objectives

1. Represent multiple sports events using lists and tuples.
2. Identify scheduling conflicts between events.
3. Detect teams participating in multiple events at the same time.
4. Calculate the total points earned by each team.
5. Generate final rankings based on aggregate points.
6. Apply fundamental Python programming concepts.

## 3. Assumptions

1. Each event has a fixed day, time, and venue.
2. Every event involves two teams.
3. Two events conflict when they occur on the same day and at the same time.
4. A team cannot participate in two events simultaneously.
5. Points are already available for each participating team.
6. The team with the highest total points receives the first rank.
7. Teams with equal points are arranged alphabetically.

## 4. Algorithm

1. Start the program.
2. Create a list containing sports event schedules.
3. Store event details using tuples.
4. Create another list containing team scores.
5. Display all scheduled events.
6. Compare each pair of events.
7. Check whether two events have the same day and time.
8. Identify venue conflicts.
9. Identify teams participating in multiple events simultaneously.
10. Calculate the total points earned by each team.
11. Sort the teams according to their total points.
12. Display the final rankings.
13. Stop the program.

## 5. Flowchart

```text
          +-----------+
          |   START   |
          +-----+-----+
                |
                v
     +----------------------+
     | Create Event Schedule|
     | and Score Lists      |
     +----------+-----------+
                |
                v
     +----------------------+
     | Display Event        |
     | Schedule             |
     +----------+-----------+
                |
                v
     +----------------------+
     | Check Scheduling     |
     | Conflicts            |
     +----------+-----------+
                |
                v
     +----------------------+
     | Calculate Team       |
     | Total Points         |
     +----------+-----------+
                |
                v
     +----------------------+
     | Sort Team Rankings   |
     +----------+-----------+
                |
                v
     +----------------------+
     | Display Final        |
     | Rankings             |
     +----------+-----------+
                |
                v
          +-----------+
          |    END    |
          +-----------+
```

## 6. Pseudocode

```text
BEGIN

    CREATE schedule list
    CREATE scores list

    DISPLAY event schedule

    FOR each pair of events

        IF day and time are equal THEN

            IF venue is equal THEN
                DISPLAY venue conflict
            END IF

            CHECK common teams

            IF common team exists THEN
                DISPLAY team conflict
            END IF

        END IF

    END FOR

    CREATE empty team totals

    FOR each score tuple

        IF team does not exist THEN
            INITIALIZE team points to zero
        END IF

        ADD points to team total

    END FOR

    SORT teams by total points in descending order

    DISPLAY final rankings

END
```

## 7. Python Concepts Used

- Variables and data types
- Lists
- Tuples
- Dictionaries
- Conditional statements
- For loops
- Nested loops
- Functions
- Sorting
- String formatting

## 8. Test Cases

| Test Case | Input / Condition | Expected Result |
|---|---|---|
| TC01 | Events have different timings | No conflict |
| TC02 | Events have the same venue and time | Venue conflict detected |
| TC03 | Same team participates in two events at the same time | Team conflict detected |
| TC04 | Team receives points from multiple events | Points aggregated |
| TC05 | Teams have different total points | Correct ranking generated |
| TC06 | Teams have equal total points | Alphabetical order used |

## 9. Sample Input

The program uses the following sample sports events:

- Football
- Basketball
- Volleyball
- Cricket
- Badminton

Participating teams:

- Falcons
- Tigers
- Lions
- Eagles

## 10. Sample Output

```text
========== SCHEDULING CONFLICTS ==========

Team Conflict: Falcons in Football and Badminton

========== FINAL TEAM RANKINGS ==========

1 . Falcons - 6 points
2 . Eagles - 3 points
3 . Lions - 3 points
4 . Tigers - 3 points

Program executed successfully.
```

## 11. How to Execute the Program

**Step 1:** Install Python 3 on your computer.

**Step 2:** Save the Python source code as:

`sports_scheduler.py`

**Step 3:** Open the terminal in the project folder.

**Step 4:** Execute the following command:

```bash
python sports_scheduler.py
```

**Step 5:** Observe the scheduling conflicts and final team rankings.

No external libraries are required.

## 12. Conclusion

The Multi-Event Sports Scheduling and Scoring program successfully demonstrates the use of Python lists and tuples for managing sports event schedules and team scores.

The program identifies scheduling conflicts, calculates aggregate points, and generates final team rankings.

This case study provides practical understanding of fundamental Python
