# 🎉 RUThere - Event Management Platform

RUThere is a full-stack web application built with **HTML**, **CSS**, and **Django** to manage and streamline events for clubs and students. The platform includes separate interfaces for clubs and students, user authentication, and automated email confirmation on event registration.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Sign up / Log in
  - Role-based access (Clubs & Students)

- 🏛️ **Club Interface**
  - Create, update, and manage events
  - View participants and manage registrations

- 🧑‍🎓 **Student Interface**
  - Explore upcoming events
  - Register with one click
    
- 📧 **Email Confirmation**
  - Instantly sends an event registration confirmation to the user’s email

---

## 🛠️ Tech Stack

| Layer     | Tools/Technologies       |
|-----------|---------------------------|
| Frontend  | HTML5, CSS3               |
| Backend   | Django (Python)           |
| Database  | SQLite / PostgreSQL       |
| Email     | SMTP via Gmail (for notifications) |

---

## 📦 Installation & Setup

Follow these steps to get the project up and running locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/eventsphere.git
cd eventsphere
```
2. Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Required Packages
```bash
pip install -r requirements.txt
```
4. Environment Variables
Create a .env file and add the following:

```env
SECRET_KEY=your_django_secret_key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=yourpassword_or_app_password
```
5. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```
7. Run the Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to see the app live.

📬 Email Setup Tips
Make sure you allow Less Secure Apps or use an App Password for Gmail.

The platform sends confirmation emails instantly after each successful event registration.

👨‍💻 Author
Lalith Gunnu
Aspiring engineer & full-stack web developer

📄 License
This project is open source

🙌 Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to improve.

📌 To-Do / Roadmap
 Add event poster upload for clubs

 Add QR code for event entry validation

 Dashboard analytics for clubs

 Pagination and search for events
 
---

Let me know if you want:
- A `requirements.txt` file
- Hosting guide for Render/Railway
- `.env.example` file







