# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
# from wtforms_sqlalchemy.fields import QuerySelectField
# from ..models import Department, Role, Grade

# class DepartmentForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     description = StringField('Description', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# class RoleForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     description = StringField('Description', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# class GradeForm(FlaskForm):
#     paygrade = StringField('Pay Grade', validators=[DataRequired()])
#     amount = StringField('Amount', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# class EmployeeAssignForm(FlaskForm):
#     department = QuerySelectField(query_factory=lambda: Department.query.all(), get_label="name")
#     role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label="name")
#     grade = QuerySelectField(query_factory=lambda: Grade.query.all(), get_label="paygrade")
#     submit = SubmitField('Submit')



from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from ..models import Department, Role, Grade

# Common Base Form
class BaseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Specific Forms
class DepartmentForm(BaseForm):
    pass

class RoleForm(BaseForm):
    pass

class GradeForm(FlaskForm):
    paygrade = StringField('Pay Grade', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    department = QuerySelectField(query_factory=lambda: Department.query.all(), get_label="name", allow_blank=True)
    role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label="name", allow_blank=True)
    grade = QuerySelectField(query_factory=lambda: Grade.query.all(), get_label="paygrade", allow_blank=True)
    submit = SubmitField('Submit')
