from __future__ import print_function
import sys
import Forms
from flask import Flask, render_template, url_for, request, redirect
from api_facade import *
app = Flask(__name__)

@app.route("/courses")
def courseList():
    student = False    # Use to test professor view
    # student = checkIfStudent(4)     # Use to test student view
    # TODO: update with professor id
    # print(getProfessorSections(1))
    if not student:
        return render_template('courseListPage.jinja', section_list=getProfessorSections(1), student=student)
    # TODO: update with student id
    if student:
        section_list = getStudentSections(1)
        for s in section_list:
            s['grade'] = (getGradeForStudentSection(s['id']))
            if s['grade'] == None:
                s['grade'] = 'N/A'
            s['comments'] = getCommentsForStudentSection(s['id'])
        return render_template('courseListPage.jinja', section_list=section_list, student=student)


@app.route("/course/<course_id>/<section_id>")
def courseView(course_id, section_id):
    lock_form = Forms.LockGradeForm()
    save_form = Forms.SaveGradeForm()
    section = getSection(section_id)
    grades_comments = getGradesAndCommentsForSection(section_id)

    #get the role of the user and load that with the template
    return render_template('coursePage.jinja', professor=True, course_id=course_id, section=section, grades_comments=grades_comments, 
        form=lock_form, save_form=save_form)

@app.route("/save_grade", methods=['GET', 'POST'])
def saveGrades():
    save_form = Forms.SaveGradeForm(request.form)
    new_grade = save_form.new_grade.data
    user_id = save_form.student_id.data
    course_id = save_form.course_id.data
    section_id = save_form.section_id.data
    saveStudentGrade(user_id, section_id, new_grade)
    
    return redirect(url_for('courseView', course_id=course_id, section_id=section_id))

@app.route("/lock_grades", methods=['GET', 'POST'])
def lockGrade():
    lock_form = Forms.LockGradeForm(request.form)
    user_id = lock_form.student_id.data
    course_id = lock_form.course_id.data
    section_id = lock_form.section_id.data
    lockStudentGrade(user_id, section_id)

    return redirect(url_for('courseView', course_id=course_id, section_id=section_id))
        
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()