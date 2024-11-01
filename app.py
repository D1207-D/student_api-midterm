from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
students = []

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# Get a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"message": "Student not found"}), 404

# Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.json
    students.append(new_student)
    return jsonify(new_student), 201

# Update a student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        updated_data = request.json
        student.update(updated_data)
        return jsonify(student), 200
    return jsonify({"message": "Student not found"}), 404

# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return jsonify({"message": "Student deleted"}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
