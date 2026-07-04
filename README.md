# 🎓 EduTrack — Student Result & Marks Portal

> A full stack Student Result Management System built with Django and Bootstrap 5, developed as part of the **Codveda Technologies Frontend Development Internship (Level 3 · Task 1 · Custom Component Library)**.

---

## 🌐 Live Demo

> Run locally using Django development server at `http://127.0.0.1:8000`

---

## 📸 Project Screenshots

| Page | Description |
|---|---|
| Login | Secure student authentication |
| Register | New student account creation |
| Dashboard | CGPA overview + quick stats |
| Marks | Subject-wise marks table |
| CGPA Calculator | Anna University grade system |
| Components | Reusable UI component library |
| Admin Panel | Teacher marks management |

---

## 🎯 Project Description

**EduTrack** is a full stack Student Result Portal for B.E Computer Science Engineering students. Students can securely login, view their subject-wise marks for Python, Java, DBMS, Operating Systems and Computer Networks. The portal automatically calculates CGPA using Anna University grade system and displays visual performance charts.

Teachers (Admin) can login to the admin panel, add subjects, enter marks for each student, and manage the entire portal.

---

## ✅ Codveda Internship Objectives Achieved

- [x] **Django Web Application** — Full stack portal with backend logic
- [x] **User Authentication** — Login, Register, Logout, Password Reset
- [x] **Reusable Components** — base.html template used across all pages
- [x] **Component Documentation** — Dedicated components.html page
- [x] **ARIA Accessibility** — All forms follow ARIA standards
- [x] **Database** — SQLite with Student, Subject and Marks models
- [x] **Admin Panel** — Django admin for teacher data management
- [x] **Bootstrap 5 Frontend** — Responsive, professional UI

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.14** | Backend programming language |
| **Django 6.0.6** | Web framework |
| **SQLite** | Database |
| **Bootstrap 5** | Frontend UI framework |
| **HTML5** | Page structure |
| **CSS3** | Custom styling |
| **JavaScript** | Frontend interactivity |
| **Chart.js** | CGPA visualization |
| **Bootstrap Icons** | Icon library |
| **Django Auth** | Authentication system |

---

## 📋 Features

### 🔐 Authentication
- Student Register with Roll Number
- Secure Login / Logout
- Password Reset (Console Email)
- Session Management

### 📊 Student Dashboard
- Welcome message with student info
- Current CGPA display
- Total subjects count
- Passed / Failed subjects
- Quick action buttons

### 📚 Marks Management
- Subject-wise marks table
- Internal + External marks
- Auto-calculated total
- Grade display (O, A+, A, B+, B, C, U)
- Pass/Fail status per subject

### 🎓 CGPA Calculator
- Auto CGPA calculation
- Anna University grade system
- Credits × Grade Points formula
- Performance label (Outstanding, Excellent, Good)
- Grade scale reference chart

### 📄 Component Library
- 8 reusable UI components documented
- Button variants
- Card variants
- Badge system
- Alert messages
- Form inputs
- Tables
- Grade badges
- Stat cards

### 👨‍💼 Admin Panel
- Add/Edit/Delete subjects
- Enter student marks
- Manage student profiles
- View all results

---

## 🗂️ Project Structure

```
edutrack/
│
├── edutrack/                  ← Project settings
│   ├── settings.py            ← Configuration
│   ├── urls.py                ← URL routing
│   └── wsgi.py                ← Server connector
│
├── accounts/                  ← Authentication app
│   ├── views.py               ← Login/Register/Logout
│   └── migrations/
│
├── results/                   ← Marks & CGPA app
│   ├── models.py              ← Database models
│   ├── views.py               ← Page logic
│   ├── admin.py               ← Admin configuration
│   └── migrations/
│
├── templates/                 ← HTML pages
│   ├── base.html              ← Main layout
│   ├── dashboard.html         ← Student dashboard
│   ├── components.html        ← Component library
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── password_reset.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_confirm.html
│   │   └── password_reset_complete.html
│   └── results/
│       ├── list.html          ← Marks table
│       └── cgpa.html          ← CGPA calculator
│
├── db.sqlite3                 ← Database file
├── manage.py                  ← Django command tool
└── README.md                  ← Documentation
```

---

## 🚀 How to Run Locally

### Step 1 — Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/edutrack-student-portal.git
cd edutrack-student-portal
```

### Step 2 — Install Django:
```bash
py -m pip install django
```

### Step 3 — Run migrations:
```bash
py manage.py migrate
```

### Step 4 — Create admin account:
```bash
py manage.py createsuperuser
```

### Step 5 — Start server:
```bash
py manage.py runserver
```

### Step 6 — Open browser:
```
http://127.0.0.1:8000
```

---

## 📱 Pages & URLs

| Page | URL |
|---|---|
| Login | `/login/` |
| Register | `/register/` |
| Dashboard | `/dashboard/` |
| Marks | `/marks/` |
| CGPA Calculator | `/cgpa/` |
| Component Library | `/components/` |
| Password Reset | `/password-reset/` |
| Admin Panel | `/admin/` |

---

## 🎓 Grade System (Anna University)

| Marks | Grade | Grade Point |
|---|---|---|
| 91 – 100 | O | 10 |
| 81 – 90 | A+ | 9 |
| 71 – 80 | A | 8 |
| 61 – 70 | B+ | 7 |
| 51 – 60 | B | 6 |
| 45 – 50 | C | 5 |
| Below 45 | U (Fail) | 0 |

---

## 🗄️ Database Models

### StudentProfile
```python
user        → OneToOne link to Django User
roll_no     → Student roll number
department  → Computer Science
year        → 1 to 4
semester    → 1 to 8
```

### Subject
```python
name        → Subject name
code        → Subject code (CS101)
credits     → Credit points (3 or 4)
semester    → Which semester
```

### Marks
```python
student         → Links to StudentProfile
subject         → Links to Subject
internal_marks  → Out of 25
external_marks  → Out of 75
total_marks     → Auto calculated (property)
grade           → Auto calculated (property)
grade_point     → Auto calculated (property)
```

---

## ♿ Accessibility (ARIA)

All components follow ARIA accessibility standards:
- `aria-label` on all inputs and buttons
- `aria-required="true"` on required fields
- `aria-live="assertive"` on error messages
- `aria-hidden="true"` on decorative icons
- `role="alert"` on alert messages
- `role="table"` on data tables
- `role="region"` on card sections

---

## 🎓 Presentation Points

> *"EduTrack is a full stack Student Result Portal built with Django backend and Bootstrap frontend. Students login securely with their credentials and view their marks for CS subjects including Python, Java, DBMS, OS and Networks. The system automatically calculates CGPA using Anna University grade system. Teachers use the Django Admin panel to enter and manage marks. The project follows ARIA accessibility standards and includes a complete component documentation page."*

---

## 📌 Internship Details

| Field | Info |
|---|---|
| **Intern Name** | A. Ancy |
| **Company** | Codveda Technologies |
| **Position** | Front-End Development Intern |
| **Intern ID** | CV/A1/78322 |
| **Level** | Level 3 — Advanced |
| **Task** | Task 1 — Custom Component Library |
| **Duration** | 21 June 2026 – 21 July 2026 |
| **Mode** | Remote / Virtual |

---

## 👩‍💻 Developer

**A. Ancy**
- 💼 Frontend Development Intern @ Codveda Technologies
- 🎓 B.E Computer Science Engineering
- 🌐 LinkedIn: [Your LinkedIn URL]
- 🐙 GitHub: [Your GitHub URL]

---

## 📄 License

This project was built for internship learning and academic purposes.

---

⭐ **If you found this project helpful, please give it a star on GitHub!**
