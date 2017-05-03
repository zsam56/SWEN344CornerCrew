from wtforms import Form, widgets, HiddenField, BooleanField, SelectField, StringField

class LockGradeForm(Form):
	student_id = HiddenField("student_id")
	course_id = HiddenField("course_id")
	section_id = HiddenField("section_id")

class SaveGradeForm(Form):
	new_grade = SelectField(u'Grade', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
	course_id = HiddenField("course_id")
	student_id = HiddenField("student_id")
	section_id = HiddenField("section_id")

class LoginForm(Form):
	username = StringField('username')
	password = StringField('password')
