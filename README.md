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
   git clone https://github.com/eliseup/pro-blogging.git
   ```

---

### 🔧 Development Environment

After cloning the repository, follow these steps:

1. **Navigate to the `pro-blogging` directory**  
   ```bash
   cd pro-blogging
   ```

2. **Start Development Containers**
   - To start the development environment, use the following command:
   ```bash
   docker compose -f docker/docker-compose-dev.yml up
   ```
   - To run the containers in the background, add the -d flag:
   ```bash
   docker compose -f docker/docker-compose-dev.yml up -d
   ```

In another terminal, access the containers:

3. **Access the application container**  
   ```bash
   docker exec -it pro-blogging-app-1 bash
   ```   
   - **Apply migrations**  
     ```bash
     python manage.py migrate
     ```

   - **Start the Django development server:**  
     ```bash
     ./runserver.sh
     ```  
     or  
     ```bash
     python manage.py runserver 0.0.0.0:8000
     ```  
   - **Run tests:**
     ```bash
     python manage.py test
     ```

**Port Mapping for Django Development Server**  

- **Container Port**: `8000`  
- **Host Port**: `8008`  

The Django development server runs on port `8000` inside the Docker container. This port is exposed to the host machine on port `8008`  

- Access the server **on the host machine** at `http://localhost:8008`


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
   docker compose -f docker/docker-compose-prod.yml run --rm app bash -c "sleep 7 && python app/manage.py migrate"
   ```

4. **Create a Django Admin user** (Optional)  
   ```bash
   docker compose -f docker/docker-compose-prod.yml run --rm app python app/manage.py createsuperuser
   ```

5. **Start the Application**  
   ```bash
   docker compose -f docker/docker-compose-prod.yml up
   ```

**Port Mapping for Production Application**  

- **Container Port**: `8000`  
- **Host Port**: `8080`  

The production application runs on port `8000` inside the Docker container. This port is exposed to the host machine on port `8080`  

- Access the application **on the host machine** at `http://localhost:8080`

---

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

---

**Note on Environment Files:**  
For simplicity and ease of assessment, `.dev_env` and `.prod_env` files have been included in the repository. While
storing production environment variables in version control is generally not recommended for security reasons, this
approach was chosen to streamline the setup process for evaluation purposes. In a real-world scenario, sensitive
environment variables should be managed securely outside of version control.
