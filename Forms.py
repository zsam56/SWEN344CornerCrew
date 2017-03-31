from wtforms import Form, widgets, HiddenField, BooleanField, SelectField

class LockGradeForm(Form):
	student_id = HiddenField("student_id")
	section_id = HiddenField("section_id")

class SaveGradeForm(Form):
	new_grade = SelectField(u'Grade', choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'F')])
	student_id = HiddenField("student_id")
	section_id = HiddenField("section_id")
