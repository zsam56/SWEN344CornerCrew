from flask import Flask, render_template, url_for
from api_facade import *
app = Flask(__name__)

@app.route("/courses")
def courseList():
    # TODO: update with professor id
    # if professor:
    return render_template('courseListPage.jinja', classList=getInstructorCourses("0001"))
    # TODO: update with student id
    # if student:
    # return render_template('courseListPage.jinja', classList=getStudentCourses("9999))


@app.route("/course/<course_id>")
def courseView(course_id):
    course = getCourse(course_id)
    grades = getGrades(course_id)
    comments = getCourseComments(course_id)
    return render_template('coursePage.jinja', course=course, grades=grades, comments=comments)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()