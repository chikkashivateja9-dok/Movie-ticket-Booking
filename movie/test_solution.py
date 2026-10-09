import sys, os, random, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from itertools import combinations
from solution import max_shows


def no_overlap(shows):
    shows = sorted(shows, key=lambda x: (x[1], x[0]))
    return all(shows[i][1] <= shows[i + 1][0] for i in range(len(shows) - 1))


def brute_force(shows):
    """Try every subset - only for tiny inputs, used to verify greedy."""
    best = 0
    for r in range(len(shows) + 1):
        for combo in combinations(shows, r):
            if no_overlap(list(combo)):
                best = max(best, r)
    return best


def test_sample():
    shows = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    count, chosen = max_shows(shows)
    assert count == 4 and no_overlap(chosen)

def test_empty():            assert max_shows([])[0] == 0
def test_single():           assert max_shows([(1, 2)])[0] == 1
def test_all_overlap():      assert max_shows([(1,10),(2,9),(3,8)])[0] == 1
def test_none_overlap():     assert max_shows([(1,2),(3,4),(5,6)])[0] == 3
def test_back_to_back():     assert max_shows([(1,3),(3,5),(5,7)])[0] == 3
def test_same_end():         assert max_shows([(1,5),(3,5),(4,5)])[0] == 1
def test_duplicates():       assert max_shows([(1,3),(1,3),(1,3)])[0] == 1
def test_unsorted():         assert max_shows([(8,9),(1,2),(5,6)])[0] == 3
def test_long_blocker():     assert max_shows([(0,100),(1,2),(3,4),(5,6)])[0] == 3

def test_invalid():
    try:
        max_shows([(5, 2)])
        assert False
    except ValueError:
        pass

def test_random_vs_bruteforce():
    random.seed(1)
    for _ in range(300):
        n = random.randint(0, 9)
        shows = []
        for _ in range(n):
            s = random.randint(0, 20)
            shows.append((s, s + random.randint(0, 6)))
        count, chosen = max_shows(shows)
        assert count == brute_force(shows), shows
        assert no_overlap(chosen)

def test_large_input():
    random.seed(2)
    shows = []
    for _ in range(200000):
        s = random.randint(0, 10**6)
        shows.append((s, s + random.randint(1, 100)))
    t = time.time()
    max_shows(shows)
    assert time.time() - t < 2


if __name__ == "__main__":
    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print("PASS", t.__name__)
    print(f"\nAll {len(tests)} tests passed")
