
# Student API

## Overview

This is a simple RESTful API for managing students. It supports basic CRUD operations (Create, Read, Update, Delete) for a Student entity, which includes the following attributes:

- **ID**: Integer
- **Name**: String
- **Grade**: String
- **Email**: String

## API Endpoints

### 1. Retrieve all students
- **GET** `/students`
- **Response**: Returns a list of all students.

### 2. Retrieve a student by ID
- **GET** `/students/{id}`
- **Response**: Returns the details of a student by ID.

### 3. Add a new student
- **POST** `/students`
- **Request Body**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "grade": "A",
        "email": "john.doe@example.com"
    }
    ```
- **Response**: Returns the created student.

### 4. Update an existing student by ID
- **PUT** `/students/{id}`
- **Request Body**:
    ```json
    {
        "id": 1,
        "name": "John Doe Updated",
        "grade": "A+",
        "email": "john.doe.updated@example.com"
    }
    ```
- **Response**: Returns the updated student.

### 5. Delete a student by ID
- **DELETE** `/students/{id}`
- **Response**: Returns a message indicating the student has been deleted.

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd student_api
   ```

3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scriptsctivate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install Flask
   ```

## Running the Application

To run the application, execute:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:8000`.

## Testing the API

You can use tools like Postman or cURL to test the API endpoints. Here are some example requests:

- **Get all students**:
  ```bash
  curl http://127.0.0.1:8000/students
  ```

- **Get a student by ID**:
  ```bash
  curl http://127.0.0.1:8000/students/1
  ```

- **Add a new student**:
  ```bash
  curl -X POST http://127.0.0.1:8000/students -H "Content-Type: application/json" -d '{"id": 2, "name": "Jane Smith", "grade": "A", "email": "jane.smith@example.com"}'
  ```

## Deployment

You can deploy the API to a cloud service like Azure or Heroku. Follow their respective documentation for instructions.


