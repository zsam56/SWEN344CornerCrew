from api_facade import *
import unittest

sectionKeyArray = ['CLASSROOM_ID', 'PROFESSOR_ID', 'AVAILABILITY', 'MAX_STUDENTS', 'TERM_ID', 'COURSE_ID', 'ID']
courseKeyArray = ['NAME', 'ID', 'CREDITS', 'MIN_GPA', 'COURSE_CODE', 'AVAILABILITY']
studentGradeKeyArray = ['IS_LOCKED', 'STUDENT_SECTION_ID', 'LAST_MODIFIED', 'ID', 'VALUE']

class testCases(unittest.TestCase):

    # def testGetSectionList(self):
    #     sectionList = getSectionList()
    #     print sectionList
    #     for key in sectionKeyArray:
    #         if key not in sectionList[0]:
    #             assert False
    #     assert True

    def testGetCourse(self):
        course = getCourse(1)
        for key in courseKeyArray:
            if key not in course:
                assert False
        assert True

    def testGetUser(self):
        user = getUser(1)
        if user['FIRSTNAME'] == 'John' and user['LASTNAME'] == 'Doe':
            assert True
        else:
            assert False

    def testGetNonexistantUser(self):
        user = getUser(666)
        if not bool(user):
            assert True
        else:
            assert False

    def testGetNumGrades(self):
        numGrades = getNumGrades(1)
        if numGrades == 2:
            assert True
        else:
            assert False

    def testGetNumStudents(self):
        numStudents = getNumStudents(1)
        if numStudents == 3:
            assert True
        else:
            assert False

    def testGetSection(self):
        section = getSection(1)
        for key in sectionKeyArray:
            if key not in section:
                assert False
        assert True

    def testGetProffessorSections(self):
        sections = getProfessorSections(1)
        if len(sections) == 5:
            assert True
        else:
            assert False

    def testGetStudentSections(self):
        sections = getStudentSections(1)
        if len(sections) == 1:
            assert True
        else:
            assert False

    def testGetGradeForStudentSection(self):
        grade = getGradeForStudentSection(1)
        for key in studentGradeKeyArray:
            if key not in grade:
                assert False
        assert True

    def testgetCommentsForStudentSection(self):
        comments = getCommentsForStudentSection(1)
        if comments[0]['CONTENT'] == "I can't believe you didn't give me an A+!":
            assert True
        else:
            assert False

    def testGetGradesAndCommentsForSection(self):
        gradesAndComments = getGradesAndCommentsForSection('swen-344-01')
        if 'grade' in gradesAndComments[4] and 'comments' in gradesAndComments[4]:
            assert True
        else:
            assert False

    def testCheckIfStudent(self):
        student = checkIfStudent(1)
        if student:
            assert True
        else:
            assert False

    def testCheckIfStudent(self):
        student = checkIfStudent(4)
        if student == True:
            assert True
        else:
            assert False

if __name__ == '__main__':
    unittest.main()