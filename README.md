# Wads-FastAPI
Here's the API endpoint table for the provided FastAPI code:


| Endpoint                | Method | Description                                  | Body Request          | Body Response       |
|-------------------------|--------|----------------------------------------------|-----------------------|---------------------|
| /tasks/                 | POST   | Create a new task                           | {
  "id": 0,
  "title": "string",
  "completed": true
}    | Task object (JSON)  |
| /tasks/                 | GET    | Get all tasks optionally filtered by completion | -                     | List of Task objects (JSON) |
| /tasks/                 | DELETE | Delete all tasks                            | -                     | Message (JSON)      |
| /tasks/{task_id}        | GET    | Get a task by ID                            | -                     | Task object (JSON)  |
| /tasks/title/{title}    | GET    | Get a task by title                         | -                     | Task object (JSON)  |
| /tasks/{task_id}        | PUT    | Update a task by ID                         | Task object (JSON)    | Task object (JSON)  |
| /tasks/{task_id}        | DELETE | Delete a task by ID                         | -                     | Message (JSON)      |
| /tasks/title/{title}    | DELETE | Delete a task by title                      | -                     | Message (JSON)      |

