# ToDo List Application

A lightweight, robust task management application built with **Python** and **Flask**. This application allows users to create, track, edit, and delete daily tasks, leveraging a persistent **SQLite** database to ensure data safety.

## Key Features

  * **Task Management**:
      * **Create**: Add new tasks instantly via the dashboard.
      * **Read**: View all scheduled tasks in a clean list format, sorted chronologically by creation date.
      * **Update**: Edit the details of any existing task.
      * **Delete**: Remove completed or unwanted tasks with a single click.
  * **Persistent Storage**: Uses SQLAlchemy with SQLite to store tasks locally, so your list survives server restarts.
  * **Date Tracking**: Automatically records the exact date and time when a task is created.
  * **Responsive Design**: Built with a base HTML template ensuring a consistent layout across all pages.

## Tech Stack

  * **Backend Framework**: [Flask](https://flask.palletsprojects.com/)
  * **Database ORM**: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
  * **Database**: SQLite (Default)
  * **Frontend**: HTML5, CSS3, Jinja2 Templating engine

## Project Structure

Here is an overview of the key files in the repository:

```text
├── app.py                  # Main application entry point; defines routes and DB models
├── requirements.txt        # List of python dependencies (Flask, SQLAlchemy, etc.)
├── instance/
│   └── test.db             # SQLite database file storing all tasks
├── static/
│   └── main.css            # Custom styling for the application
└── templates/              # HTML templates rendered by Flask
    ├── base.html           # Base layout inherited by other templates
    ├── index.html          # Homepage with task list and 'Add Task' form
    └── update.html         # Form to update existing task content
```

## Database Schema

The application uses a single table named `todo` with the following columns:

| Column Name    | Type      | Description                               |
| :------------- | :-------- | :---------------------------------------- |
| `id`           | Integer   | Primary Key, Unique ID for each task      |
| `content`      | String    | The text description of the task (Max 200 chars) |
| `date_created` | DateTime  | Timestamp of when the task was added      |

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

  * Python 3.x installed
  * pip (Python package manager)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/greatwhite9/ToDo.git
    cd todo-app
    ```

2.  **Create a virtual environment (Optional but Recommended):**

    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # Mac/Linux
    source env/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the Database:**
    The application automatically creates the database structure inside an `app_context` block when run.

5.  **Run the Application:**

    ```bash
    python app.py
    ```

    *Debug mode is enabled by default for development.*

6.  **Access the App:**
    Open your browser and navigate to `http://localhost:5000/`.

## 🔮 Future Improvements

  * **User Authentication**: Add login/signup functionality so users can have private lists.
  * **Due Dates**: Add a column for task deadlines.
  * **Task Completion**: Add a checkbox to mark tasks as "Done" without deleting them.
  * **Categories**: Tag tasks (e.g., Work, Personal, Shopping).
