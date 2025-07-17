📚 Teacher Portal — Django Project
A simple, user-friendly Teacher Portal built with Django, Bootstrap 5, and DataTables.
Teachers can manage student records:
✅ View, ✅ Add (via Modal), ✅ Edit (via Modal), ✅ Delete.

🚀 Features
Secure Login / Logout / Signup for Teachers.
Interactive DataTable with:
Search
Pagination
Column sorting
Bootstrap Icons for a modern look.
Pop-up Modal Forms for:
Adding students
Editing students
Backend logic:
If Name + Subject exists, adds to existing marks.
Otherwise, creates a new student.

🛠️ Tech Stack
Layer	Technology
Backend	Django (Python)
Frontend	Bootstrap 5, DataTables, Vanilla JS
DB	SQLite (Default for Django)
Auth	Django Auth

📂 Project Setup (Local)
1️⃣ Clone the Repo
git clone 
cd teacher-portal
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate
    
3️⃣ Install Dependencies
pip install django
🔧 Migrate Database

python manage.py makemigrations
python manage.py migrate
🔑 Create Superuser (Optional, Admin Panel)

python manage.py createsuperuser
🚦 Run the App

python manage.py runserver
Go to: http://127.0.0.1:8000/


🙌 Author
Omkar Kure
[Your GitHub Profile Link]