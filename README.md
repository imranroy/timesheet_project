**Project Overview**
A Django-based Timesheet Management System where users can log project activities, locations, start and end times, and view project dashboards.

🚀 **Features**
Create new project entries with start and end times
Automatically calculate project durations
View recent projects on the dashboard
Simple and clean interface
Built with Django 5.2 and Python 3.13

🛠️ **Tech Stack**
Backend: Django
Frontend: HTML, Bootstrap (optional if you styled it)
Database: SQLite3 (default Django DB)

🏗️ **Setup Instructions**
Clone the repository:
git clone https://github.com/your-username/timesheet_project.git
cd timesheet_project
Create a virtual environment and activate it:
python -m venv my_env
my_env\Scripts\activate   # On Windows
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Start the server:
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.

✨ **Future Improvements**
User authentication (login/signup)
Better UI/UX design
Export timesheet data to Excel/PDF
Admin dashboard enhancements
