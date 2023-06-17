import course_assigner
import random

courses_list = [
    "Spanish",
    "Algebra",
    "Geometry",
    "Biology",
    "History",
    "English"
]

courses = {}

for x in courses_list:
    courses[x] = {}
    courses[x]["min"] = random.randint(0,1000//len(courses_list))
    courses[x]["max"] = random.randint(courses[x]["min"],1000)

preferences = {}

for i in range(1000):
    random.shuffle(courses_list)
    preferences[i] = courses_list

assigned = course_assigner.random_assign(courses=courses,preferences=preferences)
average_preference = course_assigner.average_preference(assigned=assigned,preferences=preferences)
