from flask import abort, flash, redirect, render_template, url_for
from flask_login import login_required, current_user

from . import home
from .. import db
from ..models import Employee


@home.route('/')
def homepage():
    """
    Render the homepage.
    """
    return render_template('home/index.html', title='Welcome to Employee Management')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the user dashboard for logged-in employees.
    """
    return render_template('home/dashboard.html', title='Dashboard')


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """
    Render the admin dashboard. Only accessible by admin users.
    """
    if not current_user.is_admin:
        flash("You are not authorized to access this page.")
        abort(403)
    return render_template('home/admin_dashboard.html', title='Admin Dashboard')


@home.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """
    Render the employee profile page.
    """
    # Fetch the current user's profile from the database
    employee = Employee.query.get_or_404(current_user.id)
    return render_template(
        'home/profilepage.html',
        title='Employee Profile',
        employee=employee
    )
