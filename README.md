# Primary School Management System

This is a Django-based web application for managing a primary school. It includes features for managing students, staff, guardians, student groups, and homework assignments.

## Features

- **User Management**: Manage staff and guardians.
- **Student Management**: Manage student information and their group assignments.
- **Homework Management**: Assign and manage homework for student groups.
- **API**: RESTful API for interacting with the system.
- **Celery Integration**: Asynchronous task processing for sending notifications.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ahmednoureldeen/primary-school-management.git
    cd primary-school-management
    ```

2. **Build and run the Docker containers**:
    ```sh
    docker-compose up --build
    ```

3. **Create a superuser**:
    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

4. **Access the application**:
    Open your browser and go to `http://localhost:8000`.

## Running Tests

To run the tests, use the following command:
```sh
docker-compose exec web pytest
```

Alternatively to run the tests locally install the project requirements in your environment(use virtualenv for example)":
```sh
pip install -r requirements.txt
```

And run the test as follows:
```sh
pytest
```


Note: For testing; sending a task using celery is mocked for simplicity.

## To check system functions API and django admin could be used to test the system functions.
## I Assumed that the main focus is on Homework API so I did not apply permission on the other APIs



