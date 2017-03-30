from __future__ import print_function
import sys
from flask import Flask, render_template, url_for, request, redirect
from api_facade import *
app = Flask(__name__)


@app.route("/courses")
def courseList():
    student = checkIfStudent(1)     # Use to test professor view
    student = checkIfStudent(4)     # Use to test student view
    # TODO: update with professor id
    if not student:
        return render_template('courseListPage.jinja', section_list=getProfessorSections(1), student=student)
    # TODO: update with student id
    if student:
        section_list = getStudentSections(1)
        for s in section_list:
            s['grade'] = (getGradeForStudentSection(s['student_section_id']))
            if s['grade'] == None:
                s['grade'] = 'N/A'
            s['comments'] = getCommentsForStudentSection(s['student_section_id'])
        return render_template('courseListPage.jinja', section_list=section_list, student=student)


@app.route("/course/<section_id>")
def courseView(section_id):
    section = getSection(section_id)
    grades_comments = getGradesAndCommentsForSection(section_id)
    #get the role of the user and load that with the template
    return render_template('coursePage.jinja', professor=True, section=section, grades_comments=grades_comments)

@app.route("/save_grade", methods=['POST'])
def saveGrades():
    print(request.form['save_grade'])
    print(request.form['student_section'])
    return render_template('courseListPage.jinja', section_list=getProfessorSections(1))

@app.route("/lock", methods=['POST'])
def lockGrade():
    print(request.form['lock_grade'])
        #TODO: call function to lock grade on each student id
    return render_template('courseListPage.jinja', section_list=getProfessorSections(1))
        
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()