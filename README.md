# Marriage Matchmaking App

## Task Overview

The **Marriage Matchmaking App** is a backend application built using **FastAPI** and **SQLAlchemy** to help users find potential matches based on their profile information. Users can create, read, update, and delete profiles, with details such as name, age, gender, email, city, and interests.

### **Task Requirements**
1. **Add User Update Endpoint**: Implement an endpoint to update user details by ID.
2. **Add User Deletion Endpoint**: Implement an endpoint to delete a user profile by ID.
3. **Find Matches for a User**: Implement an endpoint to find potential matches for a user based on their profile information.
4. **Add Email Validation**: Add validation to ensure the email field in user profiles contains valid email addresses.

## Approach

1. **Database**:
   - The app uses **SQLite** as the database for storing user profiles.
   - The `User` model includes fields like `id`, `name`, `age`, `gender`, `email`, `city`, and `interests`. The `interests` field is stored as a **JSON** array for flexibility in storing multiple values.

2. **Schemas**:
   - Pydantic models were used to validate the input data.
   - The `UserCreate` schema was used to create new users, while `UserUpdate` was introduced to allow partial updates to existing users.
   - Email validation was implemented using **Pydantic's `EmailStr`** for correct email formats.

3. **Endpoints**:
   - **Create User**: Allows users to create new profiles.
   - **Read Users**: Allows retrieving a list of users.
   - **Read User by ID**: Retrieve a specific user profile by their ID.
   - **Update User**: Allows users to update their profile information.
   - **Delete User**: Allows deleting a user profile by their ID.
   - **Find Matches**: Retrieves potential matches for a user based on their profile, including city, gender, age, and shared interests.

## Technologies Used
- **Python 3.7+**
- **FastAPI**: For building the web API.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **Pydantic**: For data validation and serialization.
- **SQLite**: For database storage.

## Installation & Setup

### Step 1: Install Dependencies
Ensure you have **Python 3.7+** installed. Then, install the required dependencies:

```bash
pip install fastapi sqlalchemy pydantic uvicorn
pip install pydantic[email]  # For email validation


After installing the dependencies, navigate to the directory where your main.py file is located and start the FastAPI app using Uvicorn:

run in terminal: uvicorn main:app --reload


The app will run at http://127.0.0.1:8000 or copy and paste the below in the browser:

http://127.0.0.1:8000/docs

