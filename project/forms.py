from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired


class AddTaskForm(Form):
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField('Date Due (mm/dd/yyyy)',
                         validators=[DataRequired()],
                         format='%m/%d/%Y'
                         )
    priority = SelectField('Priority',
                           choices=[(x, x) for x in range(1, 11)]
                           )
    status = IntegerField("Status")
