import random
import time
#Import the script located at ../course_assigner.py
import sys
sys.path.append("..")
import course_assigner

courses_list = [
    "Spanish",
    "Algebra",
    "Geometry",
    "Biology",
    "History",
    "English",
    "Chemistry",
    "Physics",
    "Calculus"
]

courses = {}

for x in courses_list:
    courses[x] = {}
    courses[x]["min"] = random.randint(0,1000//len(courses_list))
    courses[x]["max"] = random.randint(max(courses[x]["min"],300),1000)

preferences = {}

for i in range(4000):
    random.shuffle(courses_list)
    preferences[i] = courses_list

start = time.time()
assigned_random = course_assigner.random_assign(courses=courses,preferences=preferences)
end = time.time()
time_random = end-start
average_preference_random = course_assigner.average_preference(assigned=assigned_random,preferences=preferences)
standard_deviation_preference_random = course_assigner.standard_deviation_preference(assigned=assigned_random,preferences=preferences)
print("_RANDOM_","Average:",average_preference_random,"Standard Deviation:",standard_deviation_preference_random,"Time:",time_random)

start = time.time()
assigned_simple = course_assigner.simple_assign(courses=courses,preferences=preferences)
end = time.time()
time_simple = end-start
average_preference_simple = course_assigner.average_preference(assigned=assigned_simple,preferences=preferences)
standard_deviation_preference_simple = course_assigner.standard_deviation_preference(assigned=assigned_simple,preferences=preferences)
print("_SIMPLE_","Average:",average_preference_simple,"Standard Deviation:",standard_deviation_preference_simple,"Time:",time_simple)

start = time.time()
assigned_reverse_simple = course_assigner.reverse_simple_assign(courses=courses,preferences=preferences)
end = time.time()
time_reverse_simple = end-start
average_preference_reverse_simple = course_assigner.average_preference(assigned=assigned_reverse_simple,preferences=preferences)
standard_deviation_preference_reverse_simple = course_assigner.standard_deviation_preference(assigned=assigned_reverse_simple,preferences=preferences)
print("_REVERSE_SIMPLE_","Average:",average_preference_reverse_simple,"Standard Deviation:",standard_deviation_preference_reverse_simple,"Time:",time_reverse_simple)

start = time.time()
assigned_compare = course_assigner.compare_assign(courses=courses,preferences=preferences)
end = time.time()
time_compare = end-start
average_preference_compare = course_assigner.average_preference(assigned=assigned_compare,preferences=preferences)
standard_deviation_preference_compare = course_assigner.standard_deviation_preference(assigned=assigned_compare,preferences=preferences)
print("_COMPARE_","Average:",average_preference_compare,"Standard Deviation:",standard_deviation_preference_compare,"Time:",time_compare)