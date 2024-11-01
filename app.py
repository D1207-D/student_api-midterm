from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for students
students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({"students": students}), 200  # Return students in a structured format

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"message": "Student not found"}), 404

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    updated_student = request.get_json()
    for index, student in enumerate(students):
        if student['id'] == id:
            students[index] = updated_student
            return jsonify(updated_student), 200
    return jsonify({"message": "Student not found"}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [student for student in students if student['id'] != id]
    return jsonify({"message": "Student deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True, port=8000)
