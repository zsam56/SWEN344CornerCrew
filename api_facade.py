courses = {
    'swen-101':
        {
            "courseName": "Freshman Seminar",
            "courseId": "swen-101",
            "numGrades": 0,
            "numStudents": 60,
            "instructor": "0001",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-220':
        {
            "courseName": "Math Models",
            "courseId": "swen-220",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0003",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-250':
        {
            "courseName": "Personal Software Engineering",
            "courseId": "swen-250",
            "numGrades": 20,
            "numStudents": 20,
            "instructor": "0003",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-256':
        {
            "courseName": "Software Process and Project Management",
            "courseId": "swen-256",
            "numGrades": 40,
            "numStudents": 100,
            "instructor": "0001",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-261':
        {
            "courseName": "Introduction to Software Engineering",
            "courseId": "swen-261",
            "numGrades": 40,
            "numStudents": 100,
            "instructor": "0002",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-262':
        {
            "courseName": "Engineering of Software Subsystems",
            "courseId": "swen-262",
            "numGrades": 40,
            "numStudents": 100,
            "instructor": "0001",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-344':
        {
            "courseName": "Web Engineering",
            "courseId": "swen-344",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0001",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-331':
        {
            "courseName": "Engineering Secure Software",
            "courseId": "swen-331",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0002",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-440':
        {
            "courseName": "Software System Requirements and Architecture",
            "courseId": "swen-440",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0002",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-444':
        {
            "courseName": "Human Centered Requirements and Design",
            "courseId": "swen-444",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0001",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-561':
        {
            "courseName": "Senior Project I",
            "courseId": "swen-561",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0003",
            "students": ["0001", "0002", "0003", "0004"],
        },
    'swen-562':
        {
            "courseName": "Senior Project II",
            "courseId": "swen-562",
            "numGrades": 40,
            "numStudents": 40,
            "instructor": "0003",
            "students": ["9999", "9998", "9997", "9996"],
        },
}


instructors = {
    "0001":
        {
            "name": "Krutz",
        },
    "0002":
        {
            "name": "Malachowsky",
        },
    "0003":
        {
            "name": "Vallino",
        },
}


students = {
    "9999":
        {
            "name": "Lexie",
        },
    "9998":
        {
            "name": "Sam",
        },
    "9997":
        {
            "name": "Shayde",
        },
    "9996":
        {
            "name:" "Yura",
        }
}


student_courses = {
    "swen-3449999": {
        "student_id": "9999",
        "course_id": "swen-562",
        "grade": "A",
        "locked": 0,
    },
    "swen-3449998": {
        "student_id": "9998",
        "course_id": "swen-344",
        "grade": "B",
        "locked": 1,
    },
    "swen-3449997": {
        "student_id": "9997",
        "course_id": "swen-344",
        "grade": "C",
        "locked": 0,
    },
    "swen-3449996": {
        "student_id": "9996",
        "course_id": "swen-344",
        "grade": "D",
        "locked": 1,
    }
}


comments = {
    "0001":
        {
            "student_course_id": "swen-3449999",
            "comment": "Thanks",
            "timestamp": "Yesterday",
            "author": "Lexie",
        },
    "0002":
        {
            "student_course_id": "swen-3449999",
            "comment": "Good job!",
            "timestamp": "Today",
            "author": "Krutz",
        },
    "0003":
        {
            "student_course_id": "swen-3449996",
            "comment": "You need to do better",
            "timestamp": "Yesterday",
            "author": "Krutz",
        },
    "0004":
        {
            "student_course_id": "swen-3449998",
            "comment": "Give me an A...or else.",
            "timestamp": "Tomorrow",
            "author": "Sam",
        },
}


def getCourseList():
    return list(courses.values())


def getCourse(id):
    if (id in courses):
        return courses[id]
    return {}


def getInstructorCourses(instructor_id):
    course_list = []
    for c in getCourseList():
        if c["instructor"] == instructor_id:
            course_list.append(c)
    return course_list


def getStudentCourses(student_id):
    course_list = []
    for c in getCourseList():
        if student_id in c["students"]:
            course_list.append(c)
    return course_list


def getGrades(course_id):
    grades = []
    for g in list(student_courses.values()):
        if (g["course_id"] == course_id):
            grades.append(g)
    return grades

def getStudentGrade(course_id, student_id):
    for g in list(student_courses.values()):
        if (g["course_id"] == course_id):
            if(g['student_id'] == student_id):
                return g['grade']


"""
:return a dictionary with key being student id and value being a list of comments
swen-3449999
"""
def getCourseComments(course_id):
    comment_list = {}
    for c in list(comments.values()):
        if (course_id in c["student_course_id"]):
            student_id = c["student_course_id"][8:]
            if (student_id in comment_list):
                comment_list[student_id].append(c)
            else:
                comment_list[student_id] = [c]
    return comment_list


"""
:return dictionary with key being course id and value being a list of comments
"""
def getStudentComments(student_id):
    comment_list = {}
    for c in list(comments.values()):
        if (student_id in c["student_course_id"]):
            course_id = c["student_course_id"][:8]
            if (course_id in comment_list):
                comment_list[course_id].append(c)
            else:
                comment_list[course_id] = [c]
    return comment_list


def test():
    print(getCourseList())
    print("\n")
    print(getCourse("swen-344"))
    print("\n")
    print(getInstructorCourses("0001"))
    print("\n")
    print(getStudentCourses("0001"))
    print("\n")
    print(getGrades("swen-344"))
    print("\n")
    print(getCourseComments("swen-344"))
    print("\n")
    print(getStudentComments("9999"))

if __name__ == "__main__":
    test()
