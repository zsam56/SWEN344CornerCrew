from DB import *


"""
:return a list of sections
"""
def getSectionList():
    return list(section.values())


"""
:return course information
"""
def getCourse(course_id):
    if (course_id in course):
        return course[course_id]


"""
:return user dictionary
"""
def getUser(student_id):
    if (student_id in user):
        return user[student_id]


"""
:return number of grades for that section
"""
def getNumGrades(section_id):
    #TODO
    return 0


"""
:return number of students enrolled in that section
"""
def getNumStudents(section_id):
    #TODO
    return 0


"""
:return section and course information
"""
def getSection(section_id):
    section_info = {}
    if (section_id in section):
        s = section[section_id]
        section_info = s
        c = getCourse(s["course_id"])
        section_info["course_name"] = c["name"]
        # We probably won't need the following fields from course information
        #section_info["credits"] = c["credits"]
        #section_info["min_gpa"] = c["min_gpa"]
        section_info["num_graded"] = getNumGrades(section_id)
        section_info["num_students"] = getNumStudents(section_id)
    return section_info


"""
:return a list of section dictionaries for sections the processor teaches
"""
def getProfessorSections(professor_id):
    section_list = []
    for s in getSectionList():
        if s["professor_id"] == professor_id:
            section_list.append(getSection(s["id"]))
    return section_list


"""
:return a list of section dictionaries for sections the student is enrolled in
"""
def getStudentSections(student_id):
    section_list = []
    for ss in list(student_section.values()):
        if student_id == ss["student_id"]:
            section_list.append(getSection(ss["section_id"]))
    return section_list


"""
:return the grade dictonary for that student section
"""
def getGradeForStudentSection(student_section_id):
    for g in list(grade.values()):
        if g["student_section_id"] == student_section_id:
            return g


"""
:return a list of comment dictionaries for that student section
"""
def getCommentsForStudentSection(student_section_id):
    comments = []
    for c in list(comment.values()):
        if c["student_section_id"] == student_section_id:
            if (isinstance(c["author"], int)):
                c["author"] = getUser(c["author"])
            comments.append(c)
    return comments


"""
:return a dictionary with key being student user id and value "grade" with grade
        data and value "comment" with comment(s) data
"""
def getGradesAndCommentsForSection(section_id):
    grades_comments = {}
    for ss in list(student_section.values()):
        student_id = ""
        if (ss["section_id"] == section_id):
            student_id = student[ss["student_id"]]["user_id"]
            grades_comments[student_id] = {
                "student": getUser(student_id),
                "grade": getGradeForStudentSection(ss["id"]),
                "comments" : getCommentsForStudentSection(ss["id"])
            }
    return grades_comments


"""
:return dictionary with key being course id and value being a list of comments
"""
def getStudentComments(student_id):
    comment_list = {}
    for c in list(comment.values()):
        if (student_id in c["student_course_id"]):
            course_id = c["student_course_id"][:8]
            if (course_id in comment_list):
                comment_list[course_id].append(c)
            else:
                comment_list[course_id] = [c]
    return comment_list


def unit_test():
    print("getSectionList()")
    print(getSectionList())
    print("\n")
    print("getSection('swen-344-01')")
    print(getSection("swen-344-01"))
    print("\n")
    print("getProfessorSections(1)")
    print(getProfessorSections(1))
    print("\n")
    print("getStudentSections(4)")
    print(getStudentSections(4))
    print("\n")
    print("getGradesAndCommentsForSection('swen-344-01')")
    print(getGradesAndCommentsForSection("swen-344-01"))

if __name__ == "__main__":
    unit_test()
