# ToDo List Project

## Overview
This project is a simple ToDo List application that helps users manage their tasks efficiently. It allows users to add, edit, delete, and mark tasks as completed.

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
    git clone https://github.com/yourusername/ToDo_List.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ToDo_List
    ```
3. Build Docker Image:
    ```bash
    docker-compose build
    ```
4. Start the Docker Container:
    ```bash
    docker-compose up
    ```

### Without Docker

1. Clone the repository:
    ```bash
    git clone
    ```
2. Navigate to the project directory:
    ```bash
    cd ToDo_List
    ```
3. Install Requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Migrate the database:
    ```bash
    python manage.py migrate
    ```
5. Collect static files:
    ```bash
    python manage.py collectstatic --noinput
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```


## Usage
- Open your browser and navigate to `http://localhost:8000`.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact [yourname@example.com](mailto:yourname@example.com).
