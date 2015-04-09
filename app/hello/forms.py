from wtforms import Form, DateTimeField, TextAreaField, SelectField

class BulletinForm(Form):
	startDate = DateTimeField('Start Date')
	endDate = DateTimeField('End Date')
	affectedProjects = SelectField(u'Affected Projects', choices=[('1', 'Project1'), ('2', 'Project2'),('3', 'Project3')])
	affectedGroups = SelectField(u'Affected Groups', choices=[('1', 'Group1'), ('2', 'Group2'),('3', 'Group3')])
	description  = TextAreaField(u'Description')
