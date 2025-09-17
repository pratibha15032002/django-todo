![Uploading Screenshot 2025-09-17 213655.png…]()
# Django To-Do App (with Authentication)

Simple Django To-Do web app with user signup/login and user-specific tasks.

## Quick start

1. Create and activate virtualenv:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```
     python -m venv venv
     source venv/bin/activate
     ```

2. Install:
```
pip install -r requirements.txt
```

3. Run migrations:
```
python manage.py migrate
```

4. Run server:
```
python manage.py runserver
```

5. Open http://127.0.0.1:8000/

Admin: create superuser with `python manage.py createsuperuser`
