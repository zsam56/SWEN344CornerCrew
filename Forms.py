from wtforms import Form, widgets, HiddenField, BooleanField, SelectField, StringField

class LockGradeForm(Form):
	user_id = HiddenField('user_id')
	student_id = HiddenField("student_id")
	course_id = HiddenField("course_id")
	section_id = HiddenField("section_id")

class SaveGradeForm(Form):
	user_id = HiddenField('user_id')
	new_grade = SelectField(u'Grade', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
	course_id = HiddenField("course_id")
	student_id = HiddenField("student_id")
	section_id = HiddenField("section_id")

class LoginForm(Form):
	username = StringField('username')
	password = StringField('password')

class CommentForm(Form):
	user_id = HiddenField('user_id')
	grade_id = HiddenField('grade_id')
	course_id = HiddenField('course_id')
	section_id = HiddenField('section_id')
	message = StringField('message')