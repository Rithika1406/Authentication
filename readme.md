# Django Authentication Project

A simple Django project demonstrating **user registration, login, logout, and role-based access control** using custom groups (Admin, Editor, Viewer).

## 🚀 Features

- User registration
- User login/logout
- Dashboard view (for all logged-in users)
- Role-based views:
  - Admin-only
  - Editor-only
  - Viewer-only


## 📁 Project Structure

```

auth_project/
│
├── auth_project/         # Project-level settings
│   └── settings.py
│   └── urls.py
│   └── wsgi.py
│
├── accounts/             # Custom app for user management
│   └── views.py
│   └── forms.py
│   └── utils.py
│   └── urls.py
│
├── templates/
│   └── registration/
│       └── login.html
│       └── register.html
│   └── dashboard.html
│   └── roles/
│       └── admin.html
│       └── editor.html
│       └── viewer.html
│
└── db.sqlite3            # Default SQLite database

```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Rithika1406/Authentication

cd auth_project
````

### 2. Create and Activate Virtual Environment


```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
````



### 3. Install Dependencies


```bash
pip install -r requirements.txt
```

Or, if not using `requirements.txt`:

```bash
pip install django==5.2
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧠 How Role-Based Access Works

* Users are assigned to Django groups: **Admin**, **Editor**, or **Viewer**
* A utility function `is_in_group(user, group_name)` checks if a user belongs to a specific group
* Views are protected using:

  ```python
  @login_required
  @user_passes_test(lambda u: is_in_group(u, 'Admin'))
  ```

## ✅ Default URL Patterns

| URL             | Description            |
| --------------- | ---------------------- |
| `/register/`    | User registration page |
| `/login/`       | User login page        |
| `/dashboard/`   | Logged-in dashboard    |
| `/admin-view/`  | Admin-only page        |
| `/editor-view/` | Editor-only page       |
| `/viewer-view/` | Viewer-only page       |

> You can customize URLs in `accounts/urls.py` and link them from the `auth_project/urls.py`.

---

## 📦 Requirements

* Python 3.10+
* Django 5.2
* SQLite (default) or any other database

---

## 🙌 Credits

Developed by **Rithika Singh**.


