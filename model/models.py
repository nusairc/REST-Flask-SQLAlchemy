#models.py

from flask_sqlalchemy import SQLAlchemy
# from .schemas import EmployeeSchema
from model.schemas import EmployeeSchema

db = SQLAlchemy()
employee_schema = EmployeeSchema()

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Float)

    def __repr__(self):
        return f'<Employee {self.employee_id}>'