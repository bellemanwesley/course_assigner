import random

def assign(courses: dict, preferences: dict):
    for x in preferences:
        assert len(preferences[x])==len(courses),"Must list a preference for all courses"

    return courses,preferences

def random_assign(courses: dict,preferences: dict):
    result = {}
    for x in preferences:
        result[x] = random.choice(list(courses))
    return result

def average_preference(assigned: dict,preferences: dict):
    num = 0
    denom = 0
    for x in preferences:
        denom += 1
        num += (preferences[x].index(assigned[x])+1)
    return num/denom