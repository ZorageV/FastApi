# Robust Social Media Application

This is a powerful social media application where users can create accounts, log in securely, and engage by posting and liking content. With **JWT authentication** powered by **PyJWT** and **SQLAlchemy** as the ORM, the app ensures seamless and secure user interaction. It also tracks likes in real-time, making it a dynamic platform.

---

## Features

- **Authentication**:  
  - Secure login and signup with **JWT tokens**.  
  - Passwords stored securely with hashing.

- **User Actions**:  
  - Create posts.  
  - Like posts from other users.

- **Real-time Tracking**:  
  - Keeps track of individual likes.  
  - Like counts are updated dynamically.

---

## Technologies

- **Python 3.9+**  
- **FastAPI** – Web framework  
- **SQLAlchemy** – ORM for database management  
- **PyJWT** – For JWT-based authentication  
- **SQLite / PostgreSQL** – Database  
- **Uvicorn** – ASGI server  

---

## Installation & Setup

### Step 1: Clone the repository  
```bash
git clone <repository-url>
cd <project-directory>
