# app.py 
from flask import Flask, request, jsonify, render_template, redirect
from model.models import db, Employee
from controller.controllers import create_employee, get_employees, update_employee, delete_employee, display_employees
import os


# Create the Flask application
app = Flask(__name__, template_folder=os.path.abspath('templates'))

# Set the database URI for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://databaseuser:password@localhost/company'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Routes
# Display the home page
@app.route('/')
def index():
    return jsonify({'message': 'Flask application is running'})

# Read employees
@app.route('/employee', methods=['GET'])
def get_employees_route():
    return get_employees()

#create employee
@app.route('/employee/create', methods=['POST'])
def create_employee_route():
    data = request.form.to_dict()  # Convert ImmutableMultiDict to dictionary / marshmallow
    return create_employee(data)

#update employee
@app.route('/employee/<int:id>/update', methods=['POST'])
def update_employee_route(id):
    data = request.form.to_dict()  # Convert ImmutableMultiDict to dictionary
    return update_employee(id, data)


# Delete an employee
@app.route('/employee/<int:id>/delete', methods=['POST'])
def delete_employee_route(id):
    return delete_employee(id)

# Display employees using template
@app.route('/employees')
def display_employees_route():
    return display_employees()


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
