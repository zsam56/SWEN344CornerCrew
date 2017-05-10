""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                 COURSE/SECTION                 """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
course = {
    1:
        {
            "ID": 1,
            "NAME": "Freshman Seminar",
            "COURSE_CODE": "swen-101",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    2:
        {
            "ID": 2,
            "NAME": "Math Models",
            "COURSE_CODE": "swen-220",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    3:
        {
            "ID": 3,
            "NAME": "Personal Software Engineering",
            "COURSE_CODE": "swen-250",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    4:
        {
            "ID": 4,
            "NAME": "Software Process and Project Management",
            "COURSE_CODE": "swen-256",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    5:
        {
            "ID": 5,
            "NAME": "Introduction to Software Engineering",
            "COURSE_CODE": "swen-261",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    6:
        {
            "ID": 6,
            "NAME": "Engineering of Software Subsystems",
            "COURSE_CODE": "swen-262",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    7:
        {
            "ID": 7,
            "NAME": "Web Engineering",
            "COURSE_CODE": "swen-344",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    8:
        {
            "ID": 8,
            "NAME": "Engineering Secure Software",
            "COURSE_CODE": "swen-331",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    9:
        {
            "ID": 9,
            "NAME": "Software System Requirements and Architecture",
            "COURSE_CODE": "swen-440",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    10:
        {
            "ID": 10,
            "NAME": "Human Centered Requirements and Design",
            "COURSE_CODE": "swen-444",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    11:
        {
            "ID": 11,
            "NAME": "Senior Project I",
            "COURSE_CODE": "swen-561",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
    12:
        {
            "ID": 12,
            "NAME": "Senior Project II",
            "COURSE_CODE": "swen-562",
            "CREDITS": 3,
            "MIN_GPA": 2,
        },
}


section = {
    1:
        {
            "ID": 1,
            "MAX_STUDENTS": 20,
            "PROFESSOR_ID": 1,
            "COURSE_ID": 7,
            "TERM_ID": 201617,
            "LOCATION_ID": 0,
            "CLASSROOM_ID": 0,
            "AVAILABILITY": 10
        },
    2:
        {
            "ID": 2,
            "MAX_STUDENTS": 20,
            "PROFESSOR_ID": 1,
            "COURSE_ID": 7,
            "TERM_ID": 201617,
            "LOCATION_ID": 0,
            "CLASSROOM_ID": 0,
            "AVAILABILITY": 10
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
            "FIRSTNAME": "John",
            "LASTNAME": "Doe",
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
    4:
        {
            "id": 1,
            "student_id": 1,
            "section_id": 1,
            "student_section_id": 1,
        },
    2:
        {
            "id": 2,
            "student_id": 2,
            "section_id": 1,
            "student_section_id": 2,
        },
    3:
        {
            "id": 3,
            "student_id": 3,
            "section_id": 1,
            "student_section_id": 3,
        },
    1:
        {
            "id": 4,
            "student_id": 4,
            "section_id": 1,
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
        "ID": 1,
        "CREATED_TIME": 100000000,
        "ID_EXPIRED": 0,
        "MESSAGE": "Notification 1",
        "STUDENT_SECTION_ID": 4,
    },
    2: {
        "ID": 2,
        "CREATED_TIME": 100000000,
        "IS_EXPIRED": 0,
        "MESSAGE": "This is a notification2",
        "STUDENT_SECTION_ID": 5,
    },
    3: {
        "ID": 3,
        "CREATED_TIME": 100000000,
        "IS_EXPIRED": 0,
        "MESSAGE": "Grade availabe to view",
        "STUDENT_SECTION_ID": 4,
    },
}
