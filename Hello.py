from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    classList = [{"courseName": "fake course One", "courseNumber": "swen-121", "numGrades": 0, "numStudents": 40}, {"courseName": "fake course Two", "courseNumber": "swen-221", "numGrades": 20, "numStudents": 20}, {"courseName": "fake course Three", "courseNumber": "swen-321", "numGrades": 40, "numStudents": 100}, {"courseName": "fake course One", "courseNumber": "swen-121", "numGrades": 0, "numStudents": 40}, {"courseName": "fake course One", "courseNumber": "swen-121", "numGrades": 0, "numStudents": 40}, {"courseName": "fake course One", "courseNumber": "swen-121", "numGrades": 0, "numStudents": 40}, {"courseName": "fake course One", "courseNumber": "swen-121", "numGrades": 0, "numStudents": 40}, {"courseName": "fake course Three", "courseNumber": "swen-321", "numGrades": 40, "numStudents": 100}, {"courseName": "fake course Three", "courseNumber": "swen-321", "numGrades": 40, "numStudents": 100}, {"courseName": "fake course Three", "courseNumber": "swen-321", "numGrades": 40, "numStudents": 100}]
    return render_template('flaskwebPage.jinja', classList=classList)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()