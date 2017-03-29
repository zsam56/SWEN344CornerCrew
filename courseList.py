from flask import Flask, render_template, url_for
from api_facade import *
app = Flask(__name__)


@app.route("/courses")
def courseList():
    #student = checkIfStudent() need check
    #student = True #for testing, true for student view, false for prof
    # TODO: update with professor id
    # if professor:
    return render_template('courseListPage.jinja', section_list=getProfessorSections(1))
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
    return render_template('coursePage.jinja', section=section, grades_comments=grades_comments)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()