from DB import *
import requests

mockAPI = False
apiBaseURL = "http://localhost:3333/API/API.php"

"""
:return JSON response from API
"""
def getFromAPI(team, function, payload):
    payload['team'] = team
    payload['function'] = function
    r = requests.get(apiBaseURL, params=payload)
    responseJSON = r.json()
    if responseJSON == None:
        return {}
    return r.json()

"""
:return a list of sections
"""
def getSectionList():
        return list(section.values())


"""
:return course information
"""
def getCourse(course_id):
    if mockAPI:
        if (course_id in course):
            return course[course_id]
    else:
        params = { 'courseID': course_id }
        responseJSON = getFromAPI('general', 'getCourse', params)
        return responseJSON;


"""
:return user dictionary
"""
def getUser(student_id):
    if mockAPI:
        if (student_id in user):
            return user[student_id]
        return None
    else:
        params = { 'studentID': student_id }
        responseJSON = getFromAPI('general', 'getStudent', params)
        return responseJSON


"""
:return number of grades for that section
"""
def getNumGrades(section_id):
    if mockAPI:
        count = 0
        for g in list(grade.values()):
            ss = student_section[g["student_section_id"]]
            if (ss["section_id"] == section_id):
                count += 1
        return count
    else:
        params = { 'section_id': section_id }
        responseJSON = getFromAPI('grading', 'getGradesForCourseSection', params);
        return len(responseJSON)

"""
:return number of students enrolled in that section
"""
def getNumStudents(section_id):
    if mockAPI:
        count = 0
        for ss in list(student_section.values()):
            if (ss["section_id"] == section_id):
                count += 1
        return count
    else:
        params = { 'sectionID': section_id }
        responseJSON = getFromAPI('student_enrollment', 'getSectionEnrolled', params)
        return len(responseJSON)

"""
:return section and course information
"""
def getSection(section_id):
    if mockAPI:
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
    else:
        params = { 'sectionID': section_id }
        responseJSON = getFromAPI('student_enrollment', 'getSection', params)


"""
:return a list of section dictionaries for sections the processor teaches
"""
def getProfessorSections(professor_id):
    if mockAPI:
        section_list = []
        for s in getSectionList():
            if s["professor_id"] == professor_id:
                section_list.append(getSection(s["id"]))
        return section_list
    else:
        params = { 'professorID': professor_id }
        responseJSON = getFromAPI('student_enrollment', 'getProfessorSections', params)
        return responseJSON

"""
:return a list of section dictionaries for sections the student is enrolled in
"""
def getStudentSections(student_id):
    if mockAPI:
        section_list = []
        for ss in list(student_section.values()):
            if student_id == ss["student_id"]:
                section = getSection(ss["section_id"])
                section['student_section_id'] = ss['student_section_id']
                section_list.append(section)
        return section_list
    else:
        params = { 'studentID': student_id }
        responseJSON = getFromAPI('student_enrollment', 'getStudentSections', params)
        return responseJSON

"""
:return the grade dictonary for that student section
"""
def getGradeForStudentSection(student_section_id):
    if mockAPI:
        for g in list(grade.values()):
            if g["student_section_id"] == student_section_id:
                return g
    else:
        params = {'student_section_id': student_section_id}
        responseJSON = getFromAPI('grading', 'getGradeForStudentSection', params)
        return responseJSON

"""
:return a list of comment dictionaries for that student section
"""
def getCommentsForStudentSection(student_section_id):
    if mockAPI:
        comments = []
        for c in list(comment.values()):
            if c["student_section_id"] == student_section_id:
                if (isinstance(c["author"], int)):
                    c["author"] = getUser(c["author"])
                comments.append(c)
        return comments
    else:
        params = { 'student_section_id': student_section_id }
        responseJSON = getFromAPI('grading', 'getCommentsForStudentSection', params);
        print(responseJSON)
        return responseJSON


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


"""
:return True if the user is a student, False if not
"""
def checkIfStudent(user_id):
    for s in list(student.values()):
        if int(user_id) == s['user_id']:
            return True
    return False


"""
Simple unit tests
"""
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
    print("\n")
    print("check if student")
    print(checkIfStudent(1))
    print(checkIfStudent(7))

if __name__ == "__main__":
    unit_test()
