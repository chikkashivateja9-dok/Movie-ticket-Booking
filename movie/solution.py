"""
Movie Ticket Booking - Maximum Non-Overlapping Shows
Technique: Greedy (Activity Selection Problem)
Rule: always pick the show that FINISHES earliest among those that don't clash.
Time: O(n log n)   Space: O(n) (O(1) extra if you only need the count)
"""


def max_shows(shows):
    """
    shows: list of (start, end) pairs.
    Returns (count, selected_shows).
    A show starting exactly when the previous one ends is allowed.
    """
    if not shows:
        return 0, []

    for s, e in shows:
        if s > e:
            raise ValueError(f"Invalid show: start {s} is after end {e}")

    # Step 1: sort by end time (ties broken by start time)
    ordered = sorted(shows, key=lambda show: (show[1], show[0]))

    # Step 2: take the first show, then greedily take every compatible one
    selected = [ordered[0]]
    last_end = ordered[0][1]

    for start, end in ordered[1:]:
        if start >= last_end:        # no overlap with last chosen show
            selected.append((start, end))
            last_end = end

    return len(selected), selected


def main():
    n = int(input("Number of shows: "))
    shows = []
    print("Enter each show as: start end  (e.g. 9 11)")
    for _ in range(n):
        s, e = map(float, input().split())
        shows.append((s, e))

    count, chosen = max_shows(shows)
    print("\nMaximum shows you can watch:", count)
    print("Selected shows:", chosen)


if __name__ == "__main__":
    main()
