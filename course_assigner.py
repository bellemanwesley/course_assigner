import random

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

def standard_deviation_preference(assigned: dict,preferences: dict):
    num = 0
    denom = 0
    for x in preferences:
        denom += 1
        num += (preferences[x].index(assigned[x])+1)
    average = num/denom    
    num = 0
    for x in preferences:
        num += (preferences[x].index(assigned[x])+1-average)**2
    return (num/denom)**0.5

def simple_assign(courses: dict,preferences: dict):
    for x in preferences:
        assert len(preferences[x])==len(courses),"Must list a preference for all courses"
    for x in courses:
        assert courses[x]["min"]<=courses[x]["max"],"Minimum must be less than or equal to maximum"
        assert courses[x]["min"]>=0,"Minimum must be greater than or equal to zero"  
    #Assert that the sum of the maximums must be greater than or equal to the total number of students
    assert sum([courses[x]["max"] for x in courses])>=len(preferences),"Sum of maximums must be greater than or equal to the total number of students"

    #Assert that the sum of the minimums must be less than or equal to the total number of students 
    assert sum([courses[x]["min"] for x in courses])<=len(preferences),"Sum of minimums must be less than or equal to the total number of students"

    assigned = {}
    unassigned_students = [x for x in preferences]

    students_needed = {x:courses[x]["min"] for x in courses}

    for i in range(len(courses)):
        assigned_student_index = []
        for j in range(len(unassigned_students)):
            if students_needed[preferences[unassigned_students[j]][i]]>0:
                assigned[unassigned_students[j]] = preferences[unassigned_students[j]][i]
                students_needed[preferences[unassigned_students[j]][i]] -= 1
                assigned_student_index.append(j)
        #Sort in reverse order so that we can delete from the end of the list
        assigned_student_index.sort(reverse=True)
        for j in assigned_student_index:
            del unassigned_students[j]

    spaces_available = {x:courses[x]["max"]-len([y for y in assigned if assigned[y]==x]) for x in courses}
    for i in range(len(courses)):
        assigned_student_index = []
        for j in range(len(unassigned_students)):
            if spaces_available[preferences[unassigned_students[j]][i]]>0:
                assigned[unassigned_students[j]] = preferences[unassigned_students[j]][i]
                spaces_available[preferences[unassigned_students[j]][i]] -= 1
                assigned_student_index.append(j)
        #Sort in reverse order so that we can delete from the end of the list
        assigned_student_index.sort(reverse=True)
        for j in assigned_student_index:
            del unassigned_students[j]
    
    if len(unassigned_students)>0:
        print("Spaces Available:",spaces_available)
        for student in unassigned_students:
            print("Student",student,"was not assigned to a course.")
            print("Student preferences:",preferences[student])
    assert len(unassigned_students)==0,"Not all students were assigned due to an unexpected error."
    for course in courses:
        assert len([x for x in assigned if assigned[x]==course])<=courses[course]["max"],"Too many students were assigned to "+course
        assert len([x for x in assigned if assigned[x]==course])>=courses[course]["min"],"Too few students were assigned to "+course
    return assigned

def reverse_simple_assign(courses: dict,preferences: dict):
    for x in preferences:
        assert len(preferences[x])==len(courses),"Must list a preference for all courses"
    for x in courses:
        assert courses[x]["min"]<=courses[x]["max"],"Minimum must be less than or equal to maximum"
        assert courses[x]["min"]>=0,"Minimum must be greater than or equal to zero"  
    #Assert that the sum of the maximums must be greater than or equal to the total number of students
    assert sum([courses[x]["max"] for x in courses])>=len(preferences),"Sum of maximums must be greater than or equal to the total number of students"

    #Assert that the sum of the minimums must be less than or equal to the total number of students 
    assert sum([courses[x]["min"] for x in courses])<=len(preferences),"Sum of minimums must be less than or equal to the total number of students"

    assigned = {}
    unassigned_students = [x for x in preferences]

    spaces_available = {x:courses[x]["max"]-len([y for y in assigned if assigned[y]==x]) for x in courses}
    for i in range(len(courses)):
        assigned_student_index = []
        for j in range(len(unassigned_students)):
            students_needed = {x:courses[x]["min"]-len([y for y in assigned if assigned[y]==x]) for x in courses}
            total_students_needed = sum(students_needed[x] for x in students_needed if students_needed[x]>0)
            if spaces_available[preferences[unassigned_students[j]][i]]>0 and total_students_needed<len(preferences)-len(assigned):
                assigned[unassigned_students[j]] = preferences[unassigned_students[j]][i]
                spaces_available[preferences[unassigned_students[j]][i]] -= 1
                assigned_student_index.append(j)
        #Sort in reverse order so that we can delete from the end of the list
        assigned_student_index.sort(reverse=True)
        for j in assigned_student_index:
            del unassigned_students[j]

    students_needed = {x:courses[x]["min"]-len([y for y in assigned if assigned[y]==x]) for x in courses}
    for i in range(len(courses)):
        assigned_student_index = []
        for j in range(len(unassigned_students)):
            if students_needed[preferences[unassigned_students[j]][i]]>0:
                assigned[unassigned_students[j]] = preferences[unassigned_students[j]][i]
                students_needed[preferences[unassigned_students[j]][i]] -= 1
                assigned_student_index.append(j)
        #Sort in reverse order so that we can delete from the end of the list
        assigned_student_index.sort(reverse=True)
        for j in assigned_student_index:
            del unassigned_students[j]

    if len(unassigned_students)>0:
        print("Spaces Available:",spaces_available)
        for student in unassigned_students:
            print("Student",student,"was not assigned to a course.")
            print("Student preferences:",preferences[student])
    assert len(unassigned_students)==0,"Not all students were assigned due to an unexpected error."
    for course in courses:
        assert len([x for x in assigned if assigned[x]==course])<=courses[course]["max"],"Too many students were assigned to "+course
        assert len([x for x in assigned if assigned[x]==course])>=courses[course]["min"],"Too few students were assigned to "+course
    return assigned

def compare_assign(courses: dict, preferences: dict):
    for x in preferences:
        assert len(preferences[x])==len(courses),"Must list a preference for all courses"
    for x in courses:
        assert courses[x]["min"]<=courses[x]["max"],"Minimum must be less than or equal to maximum"
        assert courses[x]["min"]>=0,"Minimum must be greater than or equal to zero"  
    #Assert that the sum of the maximums must be greater than or equal to the total number of students
    assert sum([courses[x]["max"] for x in courses])>=len(preferences),"Sum of maximums must be greater than or equal to the total number of students"

    #Assert that the sum of the minimums must be less than or equal to the total number of students 
    assert sum([courses[x]["min"] for x in courses])<=len(preferences),"Sum of minimums must be less than or equal to the total number of students"

    assigned = {}
    unassigned_students = [x for x in preferences]

    students_needed = {x:courses[x]["min"] for x in courses}

    for i in range(len(courses)):
        for course in courses:
            assigned_student_index = []
            #Determine the number of students who have course as their ith preference
            potential_students = [x for x in unassigned_students if preferences[x][i]==course]
            if students_needed[course]>len(potential_students) or i==len(courses)-1:
                for j in range(len(unassigned_students)):
                    if students_needed[preferences[unassigned_students[j]][i]]>0:
                        assigned[unassigned_students[j]] = preferences[unassigned_students[j]][i]
                        students_needed[preferences[unassigned_students[j]][i]] -= 1
                        assigned_student_index.append(j)
            else:
                second_preferences = {}
                for student in potential_students:
                    for k in range(len(preferences[student])):
                        if students_needed[preferences[student][k]]>0 and preferences[student][k]!=course:
                            second_preferences[student] = preferences[student][k]
                            break                
                for j in range(students_needed[course]):
                    highest_value = max(second_preferences.values())
                    highest_student = [x for x in second_preferences if second_preferences[x]==highest_value][0]
                    assigned[highest_student] = course
                    students_needed[course] -= 1
                    del second_preferences[highest_student]
                    assigned_student_index.append(unassigned_students.index(highest_student))
            #Sort in reverse order so that we can delete from the end of the list
            assigned_student_index.sort(reverse=True)
            for j in assigned_student_index:
                del unassigned_students[j]


    spaces_available = {x:courses[x]["max"]-len([y for y in assigned if assigned[y]==x]) for x in courses}
    for i in range(len(courses)):
        assigned_student_index = []
        for j in range(len(unassigned_students)):
            if spaces_available[preferences[unassigned_students[j]][i]]>0:
                assigned[unassigned_students[j]] = preferences[unassigned_students[j]][i]
                spaces_available[preferences[unassigned_students[j]][i]] -= 1
                assigned_student_index.append(j)
        #Sort in reverse order so that we can delete from the end of the list
        assigned_student_index.sort(reverse=True)
        for j in assigned_student_index:
            del unassigned_students[j]
    
    if len(unassigned_students)>0:
        print("Spaces Available:",spaces_available)
        for student in unassigned_students:
            print("Student",student,"was not assigned to a course.")
            print("Student preferences:",preferences[student])
    assert len(unassigned_students)==0,"Not all students were assigned due to an unexpected error."
    for course in courses:
        assert len([x for x in assigned if assigned[x]==course])<=courses[course]["max"],"Too many students were assigned to "+course
        assert len([x for x in assigned if assigned[x]==course])>=courses[course]["min"],"Too few students were assigned to "+course
    return assigned