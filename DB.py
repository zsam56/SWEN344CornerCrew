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
            "id": "swen-344-01",
            "max_students": 20,
            "professor_id": 1,
            "course_id": "swen-344",
            "term_id": 201617,
            "location_id": 0,
        },
    "swen-344-02":
        {
            "id": "swen-344-02",
            "max_students": 20,
            "professor_id": 1,
            "course_id": "swen-344",
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
            "first_name": "Dan",
            "last_name": "Krutz",
            "role": "professor",
        },
     2:
        {
            "username": "malachowsky",
            "password": "password",
            "email": "malachowsky@se.rit.edu",
            "first_name": "Sam",
            "last_name": "Malachowsky",
            "role": "professor",
        },
    3:
        {
            "username": "vallino",
            "password": "password",
            "email": "vallino@se.rit.edu",
            "first_name": "Jim",
            "last_name": "Vallino",
            "role": "professor",
        },
    4:
        {
            "username": "youknownothing",
            "password": "password",
            "email": "jsnow@se.rit.edu",
            "first_name": "John",
            "last_name": "Snow",
            "role": "student",
        },
    5:
        {
            "username": "squidward",
            "password": "password",
            "email": "squidward@se.rit.edu",
            "first_name": "Squid",
            "last_name": "Ward",
            "role": "student",
        },
    6:
        {
            "username": "l337",
            "password": "password",
            "email": "l337@se.rit.edu",
            "first_name": "l337",
            "last_name": "h4x0r",
            "role": "student",
        },
    7:
        {
            "username": "yoloswag",
            "password": "password",
            "email": "#blessed@se.rit.edu",
            "first_name": "Yolo",
            "last_name": "Swag",
            "role": "student",
        },
    8:
        {
            "username": "admin",
            "password": "password",
            "email": "webmaster@rit.edu",
            "first_name": "admin",
            "last_name": "nimda",
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
            "user_id": 4,
        },
    2:
        {
            "user_id": 5,
        },
    3:
        {
            "user_id": 6,
        },
    4:
        {
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
        },
    2:
        {
            "id": 2,
            "student_id": 2,
            "section_id": "swen-344-01",
        },
    3:
        {
            "id": 3,
            "student_id": 3,
            "section_id": "swen-344-01",
        },
    4:
        {
            "id": 4,
            "student_id": 4,
            "section_id": "swen-344-01",
        },
    5:
        {
            "id": 5,
            "student_id": 1,
            "section_id": "swen-344-02",
        },
    6:
        {
            "id": 6,
            "student_id": 2,
            "section_id": "swen-344-02",
        },
}


grade = {
    1:
        {
            "value": "A",
            "is_locked": 0,
            "last_modified": 100000000,
            "student_section_id": 1,
        },
    2:
        {
            "value": "B",
            "is_locked": 1,
            "last_modified": 100000000,
            "student_section_id": 2,
        },
    3:
        {
            "value": "B",
            "is_locked": 1,
            "last_modified": 100000000,
            "student_section_id": 3,
        },
    4:
        {
            "value": "B",
            "is_locked": 1,
            "last_modified": 100000000,
            "student_section_id": 4,
        },
}


comment = {
    1:
        {
            "grade_id": 1,
            "student_section_id": 1,
            "comment": "Thanks",
            "created_time": 100000000,
            "author": 4,
        },
    2:
        {
            "grade_id": 1,
            "student_section_id": 1,
            "comment": "Good job!",
            "created_time": 100000000,
            "author": 1,
        },
    3:
        {
            "grade_id": 4,
            "student_section_id": 4,
            "comment": "You need to do better",
            "created_time": 100000000,
            "author": 1,
        },
    4:
        {
            "grade_id": 2,
            "student_section_id": 2,
            "comment": "Give me an A...or else.",
            "created_time": 100000000,
            "author": 5,
        },
}