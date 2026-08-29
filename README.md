# Django Blog

A full-featured blog web application built with **Django**. The project allows users to explore blog posts across different categories, while administrators can manage blogs, categories, users, and other website content through Django's admin panel.

## 🌐 Live Demo

**[Visit the Live Website](https://nishu07.pythonanywhere.com/)**

## 📂 GitHub Repository

**[View Source Code](https://github.com/Bhattnishu/Django_Blog)**

## ✨ Features

* User authentication and authorization
* Blog post creation and management
* Blog categories
* Featured blog posts
* Featured images for blog posts
* Draft and Published post status
* Blog comments
* About section
* Social media links
* Django Admin panel for content management
* Responsive user interface
* Static and media file handling
* Deployed on PythonAnywhere

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **Bootstrap**
* **Django Crispy Forms**
* **Git & GitHub**
* **PythonAnywhere**

## 📁 Project Structure

```text
Django_Blog/
│
├── assignments/
├── blog_main/
├── blogs/
├── dashboard/
│
├── media/
│   └── uploads/
│
├── static/
│   └── css/
│
├── templates/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

## 📝 Blog Categories

The application currently contains categories such as:

* Sports
* Music
* Education
* Technology
* Entertainment
* Travel
* Health & Fitness
* Lifestyle

## 🗃️ Blog Management

Each blog post can contain:

* Title
* Slug
* Category
* Author
* Featured Image
* Short Description
* Blog Body
* Publication Status
* Featured Status

The `is_featured` field allows selected posts to be highlighted on the website.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Bhattnishu/Django_Blog.git
cd Django_Blog
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🖼️ Static and Media Files

The project separates static files and user-uploaded media files.

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

For production, static files are collected using:

```bash
python manage.py collectstatic
```

## 🚀 Deployment

The application is deployed on **PythonAnywhere**.

The deployment includes:

* Python virtual environment
* WSGI configuration
* Static file configuration
* Media file configuration
* SQLite database
* Production web server

### Live Application

https://nishu07.pythonanywhere.com/

## 🔐 Admin Panel

Django's built-in admin panel is used to manage:

* Blog posts
* Categories
* Authors/users
* Website content
* Other application data

## 🎯 Purpose of the Project

This project was created to gain practical experience with Django and understand how a real-world web application is structured, developed, managed, and deployed.

It demonstrates concepts such as:

* Django models
* Views and templates
* URL routing
* Forms
* Authentication
* Database relationships
* CRUD operations
* Static and media files
* Django Admin
* Deployment

## 👨‍💻 Author

**Nishant Bhatt**

* GitHub: https://github.com/Bhattnishu
* Live Project: https://nishu07.pythonanywhere.com/

---

⭐ If you find this project useful, feel free to explore the repository.
