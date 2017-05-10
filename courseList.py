from __future__ import print_function
import sys
import Forms
from flask import Flask, render_template, url_for, request, redirect, jsonify
from api_facade import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.jinja')

@app.route("/login", methods=['POST'])
def login():
    login_form = Forms.LoginForm(request.form)
    username = login_form.username.data
    password = login_form.password.data
    user = login_api(username, password)
    return redirect(url_for('courseList', user_id=user['ID']))

@app.route("/courses/<user_id>")
def courseList(user_id):
    user = getUser(user_id)
    if (checkIfStudent(user_id)):
        #student
        notifications = []
        section_list = getStudentSections(user_id)
        for s in section_list:
            s['grade'] = (getGradeForStudentSection(s['ID']))
            if s['grade'] == None:
                s['grade'] = 'N/A'
            s['comments'] = getCommentsForStudentSection(s['ID'])
            notifications.append(getNotificationssForStudentSection(s['SECTION_ID']))
            notifications = notifications[0]
        return render_template('courseListPage.jinja', section_list=section_list, student=student, notifications=notifications)
    else:
        #prof
        sections = getProfessorSections(user_id)
        print(sections)

        return render_template('courseListPage.jinja', section_list=getProfessorSections(user_id), student=False)


@app.route("/course/<course_id>/<section_id>")
def courseView(course_id, section_id):
    lock_form = Forms.LockGradeForm()
    save_form = Forms.SaveGradeForm()
    section = getSection(section_id)
    grades_comments = getGradesAndCommentsForSection(section_id)
    hashtag = getClassHashtag(section)
    #get the role of the user and load that with the template
    return render_template('coursePage.jinja', professor=True, course_id=course_id, section=section, grades_comments=grades_comments, 
        form=lock_form, save_form=save_form, hashtag=hashtag)

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

@app.route("/expireNotification", methods=["POST"])
def expireNotification():
    markAsExpired(request.form['id'])
    return jsonify({'key':'value'})

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
