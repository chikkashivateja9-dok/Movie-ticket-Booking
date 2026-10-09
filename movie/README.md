# Movie Ticket Booking – Maximum Non-Overlapping Shows

## Problem Statement
A cinema has several shows scheduled throughout the day. Each show has a starting time and an ending time. A customer wants to watch the maximum number of complete shows without watching two overlapping shows. Select the maximum number of non-overlapping shows.

## Problem Understanding
- **Given:** n shows, each with a (start, end) time.
- **Find:** the largest set of shows with no two overlapping.
- **Rules:** each show must be watched completely; only one show at a time.
- **Assumption:** if one show ends at time T and another starts at T, they do **not** overlap.
- We maximise the **count** of shows, not the total time watched.

## Approach
Greedy – this is the classic **Activity Selection Problem**.
1. Sort all shows by **end time**.
2. Pick the first show.
3. For every next show, pick it only if its start time >= end time of the last picked show.

## Why This Algorithm?
| Approach | Time | Verdict |
|---|---|---|
| Brute force (all subsets) | O(2^n) | Correct but far too slow |
| Dynamic Programming | O(n²) | Unnecessary; needed only if shows had weights/values |
| Greedy – earliest finish first | O(n log n) | Optimal and fastest |

Other greedy rules **fail**: earliest start (a long show blocks many), shortest duration (a short show in the middle can block two).

**Correctness (exchange argument):** take any optimal solution. If it doesn't begin with the earliest-finishing show, swap its first show with that one. The new show ends no later, so nothing conflicts and the count stays the same. Repeating this shows greedy is as good as optimal.

## Pseudocode
```
Sort shows by end time (ascending)
count = 1
lastEnd = end time of first show
For each remaining show (s, e):
    If s >= lastEnd:
        select this show
        count = count + 1
        lastEnd = e
Return count
```

## Complexity Analysis
- **Time:** O(n log n) – sorting dominates; the scan is O(n).
- **Space:** O(n) to store selected shows (O(1) extra if only the count is needed).

## Implementation
`src/solution.py` (Python 3, no external libraries).

Run:
```
python src/solution.py
```
Run tests:
```
python test/test_solution.py
```

## Test Cases
Covered in `test/test_solution.py`: sample case, empty input, single show, all overlapping, none overlapping, back-to-back shows, same end time, duplicates, unsorted input, long blocking show, invalid input (start > end), 300 random cases verified against brute force, and a 200,000-show performance test.

## Sample Input / Output
Input:
```
11
1 4
3 5
0 6
5 7
3 9
5 9
6 10
8 11
8 12
2 14
12 16
```
Output:
```
Maximum shows you can watch: 4
Selected shows: [(1.0, 4.0), (5.0, 7.0), (8.0, 11.0), (12.0, 16.0)]
```

## Team Members
- Member 1 – Problem Analysis + Algorithm: _name_
- Member 2 – Implementation + Integration: _name_
- Member 3 – Testing + Debugging + Optimization: _name_
- Member 4 – GitHub + Documentation + Presentation: _name_

## AI Tools Used
Claude – used to explain the problem, compare algorithms, draft pseudocode, generate test cases and draft this README. All logic was reviewed, understood and tested by the team.
