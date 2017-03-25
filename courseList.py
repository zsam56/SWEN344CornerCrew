from flask import Flask, render_template, url_for
from api_facade import *
app = Flask(__name__)

@app.route("/courses")
def courseList():
    # TODO: update with professor id
    # if professor:
    return render_template('courseListPage.jinja', section_list=getProfessorSections(1))
    # TODO: update with student id
    # if student:
    # return render_template('courseListPage.jinja', classList=getStudentCourses("9999))


@app.route("/course/<section_id>")
def courseView(section_id):
    section = getSection(section_id)
    grades_comments = getGradesAndCommentsForSection(section_id)
    return render_template('coursePage.jinja', section=section, grades_comments=grades_comments)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()