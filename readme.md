# ToDo List Project

## Overview
This project is a simple ToDo List application that helps users manage their tasks efficiently. It allows users to add, edit, delete, and mark tasks as completed.

- **Live Backend (REST APIs):** https://to-do-list-4np2.onrender.com
- **Postman Collection:** [To-Do List API](https://orange-comet-842903.postman.co/workspace/SocialApp~4793c6e6-ca9d-4829-b619-c437488e9a69/collection/27788962-4762db34-70b0-4dcf-8654-2d5d1430e621?action=share&creator=27788962)

## Features
- User Registration
- User Login
- Add new tasks
- Edit existing tasks
- Delete tasks

## Installation

### With Docker
1. Clone the repository:
    ```bash
    git clone https://github.com/yashd24/To-Do-List.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ToDo_List
    ```
3. Configure Environment Variables. 
Create an `.env` file in the root directory.


```bash
# Database Configuration

DB_USER=<your_db_user>
DB_HOST=<your_db_host_url>
DB_PASS=<your_db_password>
DB_NAME=<your_db_name>
DB_PORT=<yout_db_port>

# Django Configuration
DJANGO_SECRET_KEY=<your_secret_key>

# Django Superuser Credentials
DJANGO_SUPERUSER_USERNAME=<your_admin_username>
DJANGO_SUPERUSER_EMAIL=<your_admin_email>
DJANGO_SUPERUSER_PASSWORD=<your_admin_password>

```

4. Build Docker Image:
    ```bash
    docker-compose build
    ```
5. Start the Docker Container:
    ```bash
    docker-compose up
    ```

### Without Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/yashd24/To-Do-List.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ToDo_List
    ```

3. Configure Environment Variables. 
Create an `.env` file in the root directory.


```bash
# Database Configuration

DB_USER=<your_db_user>
DB_HOST=<your_db_host_url>
DB_PASS=<your_db_password>
DB_NAME=<your_db_name>
DB_PORT=<yout_db_port>

# Django Configuration
DJANGO_SECRET_KEY=<your_secret_key>

# Django Superuser Credentials
DJANGO_SUPERUSER_USERNAME=<your_admin_username>
DJANGO_SUPERUSER_EMAIL=<your_admin_email>
DJANGO_SUPERUSER_PASSWORD=<your_admin_password>

```

4. Install Requirements:
    ```bash
    pip install -r requirements.txt
    ```

5. Migrate the database:
    ```bash
    python manage.py migrate
    ```
6. Collect static files:
    ```bash
    python manage.py collectstatic --noinput
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```


## Usage
- Open your browser and navigate to `http://localhost:8000`.

## Coverage Reports

### Unit Test
[Unit Test Coverage Report](assets/Unit_Test_Report.png")

### Integration Test
[Integration Test Coverage Report](assets/Integration_Test_Report.png")

## Contact
For any questions or feedback, please contact [yashd2024@gmail.com](mailto:yashd2024@gmail.com).
