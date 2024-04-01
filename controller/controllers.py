#controllers.py

from model.models import db, Employee
from flask import jsonify, render_template
from model.schemas import EmployeeSchema

# Initialize the EmployeeSchema marshmallow


def get_employees():
    employees = Employee.query.all()
    output = [{'id': employee.employee_id, 'name': employee.name, 'salary': employee.salary} for employee in employees]
    return jsonify({'employees': output})

from model.models import db, Employee, employee_schema
from flask import jsonify

def create_employee(data):
    errors = employee_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400

    new_employee = Employee(name=data['name'], salary=data['salary'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee created successfully'}), 201

def update_employee(id, data):
    errors = employee_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400

    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    
    employee.name = data['name']
    employee.salary = data['salary']
    db.session.commit()
    return jsonify({'message': 'Employee updated successfully'})



def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully'})
