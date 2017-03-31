from wtforms import Form, widgets, HiddenField, BooleanField, SelectField

class LockGradeForm(Form):
	student_id = HiddenField("student_id")
	section_id = HiddenField("section_id")

class SaveGradeForm(Form):
	new_grade = SelectField(u'Grade', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
	student_id = HiddenField("student_id")
	section_id = HiddenField("section_id")
