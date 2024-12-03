from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Represents an Employee entity with login capabilities (via UserMixin).
    """

    __tablename__ = 'employees'  # Table name in the database

    # Attributes/Columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Employee table
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)  # Unique email of the employee
    username = db.Column(db.String(60), index=True, unique=True, nullable=False)  # Unique username for login
    first_name = db.Column(db.String(60), nullable=False)  # First name of the employee
    last_name = db.Column(db.String(60), nullable=False)  # Last name of the employee
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password (no plain text)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))  # Foreign key linking to the department
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # Foreign key linking to the role
    grade_id = db.Column(db.Integer, db.ForeignKey('grades.id'))  # Foreign key linking to the grade
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # Boolean flag to indicate admin status
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp when created
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp when updated

    @property
    def password(self):
        """
        Prevent password from being directly accessed.
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set the password after hashing it securely.
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Verify the entered password against the stored hashed password.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        String representation of the Employee instance for debugging purposes.
        """
        return f"<Employee: {self.username} (Email: {self.email})>"


# Flask-Login user loader function
@login_manager.user_loader
def load_user(user_id):
    """
    Load an employee instance based on their ID (used by Flask-Login).
    """
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Represents a Department entity in the system.
    """

    __tablename__ = 'departments'  # Table name in the database

    # Attributes/Columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Department table
    name = db.Column(db.String(60), unique=True, nullable=False)  # Unique name of the department
    description = db.Column(db.String(200), nullable=False)  # Description of the department's purpose
    employees = db.relationship('Employee', backref='department', lazy='dynamic')  # Relationship to employees in the department
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp when created
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp when updated

    def __repr__(self):
        """
        String representation of the Department instance for debugging purposes.
        """
        return f"<Department: {self.name}>"


class Role(db.Model):
    """
    Represents a Role entity (e.g., job titles) in the system.
    """

    __tablename__ = 'roles'  # Table name in the database

    # Attributes/Columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Role table
    name = db.Column(db.String(60), unique=True, nullable=False)  # Unique name of the role
    description = db.Column(db.String(200), nullable=False)  # Description of the role's responsibilities
    employees = db.relationship('Employee', backref='role', lazy='dynamic')  # Relationship to employees with this role
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp when created
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp when updated

    def __repr__(self):
        """
        String representation of the Role instance for debugging purposes.
        """
        return f"<Role: {self.name}>"


class Grade(db.Model):
    """
    Represents a Pay Grade entity in the system.
    """

    __tablename__ = 'grades'  # Table name in the database

    # Attributes/Columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Grade table
    paygrade = db.Column(db.String(60), unique=True, nullable=False)  # Unique identifier for the pay grade
    amount = db.Column(db.String(200), nullable=False)  # Pay amount for the grade
    employees = db.relationship('Employee', backref='grade', lazy='dynamic')  # Relationship to employees in this grade
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp when created
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp when updated

    def __repr__(self):
        """
        String representation of the Grade instance for debugging purposes.
        """
        return f"<Grade: {self.paygrade}>"
