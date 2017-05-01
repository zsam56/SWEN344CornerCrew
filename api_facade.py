from DB import *
import requests

mockAPI = True
apiBaseURL = "http://vm344d.se.rit.edu:3333/API/API.php"

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
    return responseJSON

"""
:return student object given user_id
"""
def getStudent(user_id):
    for stud in student.values():
        if int(stud['user_id']) == int(user_id):
            return stud['id']

"""
:post to the API
"""
def postToAPI(team, function, data):
    postURL = apiBaseURL + '?team=' + team + '&function=' + function
    r = requests.post(postURL, data)
    responseJSON = r.json()
    if responseJSON == None:
        return {}
    return responseJSON


"""
:return a list of sections
"""
def getSectionList():
    if mockAPI:
        return list(section.values())
    else:
        section_list = []
        # the enrollment api is limited, so this is fun...
        # first, get the list of all courses
        course_list = getFromAPI('student_enrollment', 'getCourseList', {})
        for course in course_list:
            params = { 'courseID': course["ID"] }
            course_sections = getFromAPI('student_enrollment', 'getCourseSections', params)
            for s in course_sections:
                s["COURSE_ID"] = course["ID"]
            section_list.extend(course_sections)
        return section_list

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
        return responseJSON

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
            ss = student_section[g["STUDENT_SECTION_ID"]]
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
            c = getCourse(s["COURSE_ID"])
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
        return responseJSON


"""
:return a list of section dictionaries for sections the processor teaches
"""
def getProfessorSections(professor_id):
    if mockAPI:
        section_list = []
        for s in getSectionList():
            if s["professor_id"] == professor_id:
                section_list.append(getSection(s["ID"]))
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
            if int(student_id) == ss["student_id"]:
                sect = getSection(ss["section_id"])
                sect['id'] = ss['id']
                sect['section_id'] = ss["section_id"]
                sect['student_section_id'] = ss['student_section_id']
                section_list.append(sect)
        return section_list
    else:
        # get courseList
        course_list = getFromAPI('student_enrollment', 'getCourseList', {})

        course_sections_list = []
        for course in course_list:
            course_params = { 'courseID': course["ID"] }
            course_sections = getFromAPI('student_enrollment', 'getCourseSections', course_params)
            course_sections_list.extend(course_sections)
        
        # get studentSections
        params = { 'studentID': student_id }
        student_sections = getFromAPI('student_enrollment', 'getStudentSections', params)

        for s_section in student_sections:
            for c_section in course_sections_list:
                if c_section["ID"] == s_section["SECTION_ID"]:
                    s_section["COURSE_ID"] = c_section["COURSE_ID"]
                    s_section["CLASSROOM_ID"] = c_section["CLASSROOM_ID"]
                    break

        return student_sections


"""
returns the id of a student_section object that
includes the given student_id and section_id
"""
def getStudentSection(student_id, section_id):
    if mockAPI:
        for ss in list(student_section.values()):
            if int(student_id) == ss["student_id"] and section_id == ss["section_id"]:
                return ss['student_section_id']
    else:
        section_list = getStudentSections(student_id)
        for ss in section_list:
            if int(student_id) == ss["STUDENT_ID"] and section_id == ss["SECTION_ID"]:
                return ss["ID"]

"""
:return the grade dictonary for that student section
"""
def getGradeForStudentSection(student_section_id):
    if mockAPI:
        for g in list(grade.values()):
            if g["STUDENT_SECTION_ID"] == int(student_section_id):
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
                if (isinstance(c["USER_ID"], int)):
                    c["USER"] = getUser(c["USER_ID"])
                comments.append(c)
        return comments
    else:
        params = { 'student_section_id': student_section_id }
        comments_list = getFromAPI('grading', 'getCommentsForStudentSection', params);
            
        return comments_list


"""
:return a list of notification dictionaries for that student section
"""
def getNotificationssForStudentSection(student_section_id):
    if mockAPI:
        notifications = []
        for n in list(notification.values()):
            if n["student_section_id"] == student_section_id:
                notifications.append(n)
        return notifications
    else:
        params = {'student_section_id': student_section_id}
        notifications_list = getFromAPI('grading', 'getNotificationsForStudentSection', params);

        return notifications_list


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
    if mockAPI:
        for c in list(comment.values()):
            if (student_id in c["student_course_id"]):
                course_id = c["student_course_id"][:8]
                if (course_id in comment_list):
                    comment_list[course_id].append(c)
                else:
                    comment_list[course_id] = [c]
        return comment_list
    else:
        params = { 'studentID': student_id }
        responseJSON = getFromAPI('grading', 'getStudentComments', params)
        for comment in responseJSON:
            if comment['STUDENT_SECTION_ID'] in comment_list:
                comment_list[comment['STUDENT_SECTION_ID']].append(comment)
            else:
                comment_list[comment['STUDENT_SECTION_ID']] = [comment]
        return comment_list

"""
:update student grade to be locked
"""
def lockStudentGrade(student_id, section_id):
    ss_id = getStudentSection(student_id, section_id)
    if mockAPI:
        student_grade = getGradeForStudentSection(ss_id)
        student_grade['is_locked'] = 1
        return True
    else:
        data = { 'student_section_id': ss_id }
        responseJSON = postToAPI('grading', 'postLockGrade', data)
        return responseJSON

"""
:update student grade
"""
def saveStudentGrade(student_id, section_id, new_grade):
    ss_id = getStudentSection(student_id, section_id)
    grade_dict = { 'A': 90, 'B': 80, 'C': 70, 'D': 65, 'F': 50 }
    numGrade = grade_dict[new_grade]
    if mockAPI:
        student_grade = getGradeForStudentSection(ss_id)
        student_grade["VALUE"] = grade_dict[new_grade]
    else:
        data = { 'student_section_id': ss_id, 'value': numGrade }
        responseJSON = postToAPI('grading', 'postUpdateGrade', data)
        return responseJSON

"""
:return True if the user is a student, False if not
"""
def checkIfStudent(user_id):
    if mockAPI:
        for s in list(student.values()):
            if int(user_id) == s['user_id']:
                return True
        return False
    else:
        user = getUser(user_id)
        if user['ROLE'] == "Student":
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
