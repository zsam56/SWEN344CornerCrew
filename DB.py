""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                 COURSE/SECTION                 """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
course = {
    'swen-101':
        {
            "name": "Freshman Seminar",
            "course_code": "swen-101",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-220':
        {
            "name": "Math Models",
            "course_code": "swen-220",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-250':
        {
            "name": "Personal Software Engineering",
            "course_code": "swen-250",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-256':
        {
            "name": "Software Process and Project Management",
            "course_code": "swen-256",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-261':
        {
            "name": "Introduction to Software Engineering",
            "course_code": "swen-261",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-262':
        {
            "name": "Engineering of Software Subsystems",
            "course_code": "swen-262",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-344':
        {
            "name": "Web Engineering",
            "course_code": "swen-344",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-331':
        {
            "name": "Engineering Secure Software",
            "course_code": "swen-331",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-440':
        {
            "name": "Software System Requirements and Architecture",
            "course_code": "swen-440",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-444':
        {
            "name": "Human Centered Requirements and Design",
            "course_code": "swen-444",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-561':
        {
            "name": "Senior Project I",
            "course_code": "swen-561",
            "credits": 3,
            "min_gpa": 2,
        },
    'swen-562':
        {
            "name": "Senior Project II",
            "course_code": "swen-562",
            "credits": 3,
            "min_gpa": 2,
        },
}


section = {
    "swen-344-01":
        {
            "ID": "swen-344-01",
            "MAX_STUDENTS": 20,
            "professor_id": 1,
            "COURSE_ID": "swen-344",
            "term_id": 201617,
            "location_id": 0,
        },
    "swen-344-02":
        {
            "ID": "swen-344-02",
            "MAX_STUDENTS": 20,
            "professor_id": 1,
            "COURSE_ID": "swen-344",
            "term_id": 201617,
            "location_id": 0,
        }
}


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                     USERS                      """
""""""""""""""""""""""""""""""""""""""""""""""""""""""


user = {
    1:
        {
            "username": "krutz",
            "password": "password",
            "email": "krutz@se.rit.edu",
            "FIRSTNAME": "Dan",
            "LASTNAME": "Krutz",
            "role": "professor",
        },
     2:
        {
            "username": "malachowsky",
            "password": "password",
            "email": "malachowsky@se.rit.edu",
            "FIRSTNAME": "Sam",
            "LASTNAME": "Malachowsky",
            "role": "professor",
        },
    3:
        {
            "username": "vallino",
            "password": "password",
            "email": "vallino@se.rit.edu",
            "FIRSTNAME": "Jim",
            "LASTNAME": "Vallino",
            "role": "professor",
        },
    4:
        {
            "username": "youknownothing",
            "password": "password",
            "email": "jsnow@se.rit.edu",
            "FIRSTNAME": "John",
            "LASTNAME": "Snow",
            "role": "student",
        },
    5:
        {
            "username": "squidward",
            "password": "password",
            "email": "squidward@se.rit.edu",
            "FIRSTNAME": "Squid",
            "LASTNAME": "Ward",
            "role": "student",
        },
    6:
        {
            "username": "l337",
            "password": "password",
            "email": "l337@se.rit.edu",
            "FIRSTNAME": "l337",
            "LASTNAME": "h4x0r",
            "role": "student",
        },
    7:
        {
            "username": "yoloswag",
            "password": "password",
            "email": "#blessed@se.rit.edu",
            "FIRSTNAME": "Yolo",
            "LASTNAME": "Swag",
            "role": "student",
        },
    8:
        {
            "username": "admin",
            "password": "password",
            "email": "webmaster@rit.edu",
            "FIRSTNAME": "admin",
            "LASTNAME": "nimda",
            "role": "admin",
        }
}


professor = {
    1:
        {
            "user_id": 1,
        },
    2:
        {
            "user_id": 2,
        },
    3:
        {
            "user_id": 3,
        },
}


student = {
    1:
        {
            "id": 1,
            "user_id": 4,
        },
    2:
        {
            "id": 2,
            "user_id": 5,
        },
    3:
        {
            "id": 3,
            "user_id": 6,
        },
    4:
        {
            "id": 4,
            "user_id": 7,
        }
}


admin = {
    1:
        {
            "user_id": 8,
        }
}


""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                STUDENT SECTIONS                """
""""""""""""""""""""""""""""""""""""""""""""""""""""""


student_section = {
    1:
        {
            "id": 1,
            "student_id": 1,
            "section_id": "swen-344-01",
            "student_section_id": 1,
        },
    2:
        {
            "id": 2,
            "student_id": 2,
            "section_id": "swen-344-01",
            "student_section_id": 2,
        },
    3:
        {
            "id": 3,
            "student_id": 3,
            "section_id": "swen-344-01",
            "student_section_id": 3,
        },
    4:
        {
            "id": 4,
            "student_id": 4,
            "section_id": "swen-344-01",
            "student_section_id": 4,
        },
    5:
        {
            "id": 5,
            "student_id": 1,
            "section_id": "swen-344-02",
            "student_section_id": 2,
        },
    6:
        {
            "id": 6,
            "student_id": 2,
            "section_id": "swen-344-02",
            "student_section_id": 6,
        },
}


grade = {
    1:
        {
            "ID": 1,
            "VALUE": 90,
            "IS_LOCKED": 0,
            "LAST_MODIFIED": "2017-03-28 15:30:00.000",
            "STUDENT_SECTION_ID": 1
        },
    2:
        {
            "ID": 2,
            "VALUE": 75,
            "IS_LOCKED": 0,
            "LAST_MODIFIED": "2017-03-28 15:30:00.000",
            "STUDENT_SECTION_ID": 2
        },
    3:
        {
            "VALUE": "B",
            "is_locked": 1,
            "last_modified": 100000000,
            "STUDENT_SECTION_ID": 3,
        },
    4:
        {
            "VALUE": "B",
            "is_locked": 1,
            "last_modified": 100000000,
            "STUDENT_SECTION_ID": 4,
        },
}


comment = {
    1:
        {
            "grade_id": 1,
            "student_section_id": 1,
            "comment": "Thanks",
            "created_time": 100000000,
            "USER_ID": 4,
        },
    2:
        {
            "grade_id": 1,
            "student_section_id": 1,
            "comment": "Good job!",
            "created_time": 100000000,
            "USER_ID": 1,
        },
    3:
        {
            "grade_id": 4,
            "student_section_id": 4,
            "comment": "You need to do better",
            "created_time": 100000000,
            "USER_ID": 1,
        },
    4:
        {
            "grade_id": 2,
            "student_section_id": 2,
            "comment": "Give me an A...or else.",
            "created_time": 100000000,
            "USER_ID": 5,
        },
}


notification = {
    1: {
        "id": 1,
        "created_time": 100000000,
        "is_expired": 0,
        "message": "Notification 1",
        "student_section_id": 4,
    },
    2: {
        "id": 2,
        "created_time": 100000000,
        "is_expired": 0,
        "message": "This is a notification2",
        "student_section_id": 5,
    },
    3: {
        "id": 3,
        "created_time": 100000000,
        "is_expired": 0,
        "message": "Grade availabe to view",
        "student_section_id": 4,
    },
}
