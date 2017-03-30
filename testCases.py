from api_facade import *
import unittest

sectionKeyArray = ['professor_id', 'max_students', 'term_id', 'course_id', 'location_id', 'id']
courseKeyArray = ['min_gpa', 'credits', 'course_code', 'name']
studentGradeKeyArray = ['is_locked', 'student_section_id', 'last_modified', 'value']

class testCases(unittest.TestCase):

    def testGetSectionList(self):
        sectionList = getSectionList()
        for key in sectionKeyArray:
            if key not in sectionList[0]:
                assert False
        assert True

    def testGetCourse(self):
        course = getCourse('swen-101')
        for key in courseKeyArray:
            if key not in course:
                assert False
        assert True

    def testGetUser(self):
        user = getUser(1)
        if user['first_name'] == 'Dan' and user['last_name'] == 'Krutz':
            assert True
        else:
            assert False

    def testGetNonexistantUser(self):
        user = getUser(666)
        if user == None:
            assert True
        else:
            assert False

    def testGetNumGrades(self):
        numGrades = getNumGrades('swen-344-01')
        if numGrades == 4:
            assert True
        else:
            assert False

    def testGetNumStudents(self):
        numStudents = getNumStudents('swen-344-01')
        if numStudents == 4:
            assert True
        else:
            assert False

    def testGetSection(self):
        section = getSection('swen-344-01')
        for key in sectionKeyArray:
            if key not in section:
                assert False
        assert True

    def testGetProffessorSections(self):
        sections = getProfessorSections(1)
        if len(sections) == 2:
            assert True
        else:
            assert False

    def testGetStudentSections(self):
        sections = getStudentSections(1)
        if len(sections) == 2:
            assert True
        else:
            assert False

    def testgetGradeForStudentSection(self):
        grade = getGradeForStudentSection(1)
        for key in studentGradeKeyArray:
            if key not in grade:
                assert False
        assert True

    def testgetCommentsForStudentSection(self):
        comments = getCommentsForStudentSection(1)
        if comments[0]['comment'] == 'Thanks':
            assert True
        else:
            assert False

    def testGetGradesAndCommentsForSection(self):
        gradesAndComments = getGradesAndCommentsForSection('swen-344-01')
        if 'grade' in gradesAndComments[4] and 'comments' in gradesAndComments[4]:
            assert True
        else:
            assert False

    def testCheckIfProfessor(self):
        student = checkIfStudent(1)
        if student == False:
            assert True
        else:
            assert False


    def testCheckIfStudent(self):
        student = checkIfStudent(5)
        if student == True:
            assert True
        else:
            assert False




if __name__ == '__main__':
    unittest.main()