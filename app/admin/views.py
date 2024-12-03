from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from . import admin
from .. import db
from ..models import Employee, Department, Role, Grade
from .forms import DepartmentForm, RoleForm, GradeForm, EmployeeAssignForm


def check_admin():
    """
    Prevent non-admins from accessing the admin routes.
    """
    if not current_user.is_admin:
        abort(403)


# Admin Dashboard
@admin.route('/dashboard')
@login_required
def admin_dashboard():
    """
    Render the admin dashboard page.
    """
    check_admin()
    return render_template('admin/dashboard.html', title="Admin Dashboard")


# Departments
@admin.route('/departments')
@login_required
def list_departments():
    """
    List all departments.
    """
    check_admin()
    departments = Department.query.all()
    return render_template('admin/departments/departments.html', departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database.
    """
    check_admin()
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data, description=form.description.data)
        try:
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except Exception:
            flash('Error: department name already exists.')
        return redirect(url_for('admin.list_departments'))
    return render_template('admin/departments/department.html', form=form, title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department.
    """
    check_admin()
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')
        return redirect(url_for('admin.list_departments'))
    return render_template('admin/departments/department.html', form=form, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database.
    """
    check_admin()
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')
    return redirect(url_for('admin.list_departments'))


# Roles
@admin.route('/roles')
@login_required
def list_roles():
    """
    List all roles.
    """
    check_admin()
    roles = Role.query.all()
    return render_template('admin/roles/roles.html', roles=roles, title="Roles")


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database.
    """
    check_admin()
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data, description=form.description.data)
        try:
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except Exception:
            flash('Error: role name already exists.')
        return redirect(url_for('admin.list_roles'))
    return render_template('admin/roles/role.html', form=form, title="Add Role")


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role.
    """
    check_admin()
    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the role.')
        return redirect(url_for('admin.list_roles'))
    return render_template('admin/roles/role.html', form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database.
    """
    check_admin()
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')
    return redirect(url_for('admin.list_roles'))


# Employees
@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees.
    """
    check_admin()
    employees = Employee.query.all()
    return render_template('admin/employees/employees.html', employees=employees, title="Employees")


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department, role, and grade to an employee.
    """
    check_admin()
    employee = Employee.query.get_or_404(id)
    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        employee.grade = form.grade.data
        db.session.commit()
        flash('You have successfully assigned a department, role, and grade.')
        return redirect(url_for('admin.list_employees'))
    return render_template('admin/employees/employee.html', form=form, employee=employee, title="Assign Employee")


@admin.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_employee(id):
    """
    Delete an employee from the database.
    """
    check_admin()
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('You have successfully deleted the employee.')
    return redirect(url_for('admin.list_employees'))



# Grades
@admin.route('/grades')
@login_required
def list_grades():
    """
    List all grades.
    """
    check_admin()
    grades = Grade.query.all()
    return render_template('admin/grades/grades.html', grades=grades, title="Grades")


@admin.route('/grades/add', methods=['GET', 'POST'])
@login_required
def add_grade():
    """
    Add a grade to the database.
    """
    check_admin()
    form = GradeForm()
    if form.validate_on_submit():
        grade = Grade(paygrade=form.paygrade.data, amount=form.amount.data)
        try:
            db.session.add(grade)
            db.session.commit()
            flash('You have successfully added a new grade.')
        except Exception:
            flash('Error: grade already exists.')
        return redirect(url_for('admin.list_grades'))
    return render_template('admin/grades/grade.html', form=form, title="Add Grade")


@admin.route('/grades/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_grade(id):
    """
    Edit a grade.
    """
    check_admin()
    grade = Grade.query.get_or_404(id)
    form = GradeForm(obj=grade)
    if form.validate_on_submit():
        grade.paygrade = form.paygrade.data
        grade.amount = form.amount.data
        db.session.commit()
        flash('You have successfully edited the grade.')
        return redirect(url_for('admin.list_grades'))
    return render_template('admin/grades/grade.html', form=form, title="Edit Grade")


@admin.route('/grades/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_grade(id):
    """
    Delete a grade from the database.
    """
    check_admin()
    grade = Grade.query.get_or_404(id)
    db.session.delete(grade)
    db.session.commit()
    flash('You have successfully deleted the grade.')
    return redirect(url_for('admin.list_grades'))
