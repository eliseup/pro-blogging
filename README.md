# 📝 Pro Blogging Platform

A simple, extensible blogging platform built with Django. This project supports Dockerized development and production environments, with features ready for scalable deployment.

---

## 🧰 Tech Stack

- **Backend**: Django (Python)  
- **Database**: PostgreSQL  
- **Containerization**: Docker & Docker Compose  
- **Environment Management**: Multiple Docker environments (dev & production)  

---

## 🚀 Getting Started

### 🔧 Setup
1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd pro-blogging
   ```

---

### 🔧 Development Environment

After cloning the repository, follow these steps:

1. **Navigate to the `pro-blogging` directory**  
   ```bash
   cd pro-blogging
   ```

2. **Initialize the containers**  
   ```bash
   docker compose -f docker/docker-compose-dev.yml up
   ```

In another terminal, access the containers:

3. **Access the application container**  
   ```bash
   docker exec -it pro-blogging-app-1 bash
   ```

4. **Run Django commands inside the container**  
   - Start the Django development server:  
     ```bash
     ./runserver.sh
     ```  
     or  
     ```bash
     python manage.py runserver 0.0.0.0:8000
     ```  
   - Run tests:  
     ```bash
     python manage.py test
     ```

**The Django development server will listen on port 8000**

---

### 🔧 Production Environment

After cloning the repository, follow these steps:

1. **Navigate to the `pro-blogging` directory**  
   ```bash
   cd pro-blogging
   ```

2. **Build the application Docker image**  
   ```bash
   docker build -f docker/prod/app/Dockerfile -t pro-blogging-app-prod .
   ```

3. **Apply migrations**  
   ```bash
   docker compose -f docker/docker-compose-prod.yml run --rm app python manage.py migrate
   ```

4. **Create a Django Admin user** (Optional)  
   ```bash
   docker compose -f docker/docker-compose-prod.yml run --rm app python manage.py createsuperuser
   ```

5. **Start the Application**  
   ```bash
   docker compose -f docker/docker-compose-prod.yml up
   ```

**After starting, the application will listen on port 8080**


# API Endpoints Documentation
*Production environment*

## Base URL
`http://localhost:8080/api`

---

## 1. **List or Create Blog Posts**
**Endpoint**: `POST /posts`  
**Method**: `GET` or `POST`  
**Description**:  
- **GET**: Retrieve a list of all blog posts.  
- **POST**: Create a new blog post.

**Request (POST)**:  
```json
{
    "title": "string",
    "content": "string"
}
```

---

## 2. **Retrieve a Blog Post**
**Endpoint**: `GET /posts/<int:pk>`  
**Method**: `GET`  
**Description**: Retrieve a specific blog post by its ID.

---

## 3. **Create a Comment**
**Endpoint**: `POST /posts/<int:pk>/comments`  
**Method**: `POST`  
**Description**: Create a new comment for a specific blog post by its ID.

**Request**:  
```json
{
    "content": "string"
}
```
