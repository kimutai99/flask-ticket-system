
# 🧾 Flask IT Support Ticket System

A lightweight, responsive IT support ticketing system built with **Flask**, **SQLite**, and **HTML/CSS**. Users can submit issues, track ticket status, and mark issues as resolved.

---

## 🚀 Features

- Submit support tickets with name, issue, and urgency
- View all tickets in a clean, mobile-friendly table
- Mark tickets as "Closed"
- Responsive design (desktop & mobile)
- SQLite for simple and fast data persistence

---

## 🛠️ Tech Stack

- Python 3
- Flask
- SQLite
- HTML5 / CSS3

---

## 📁 Folder Structure

```
project/
├── app.py                # Main Flask app
├── tickets.db            # SQLite database (auto-created)
├── static/
│   └── style.css         # Stylesheet
└── templates/
    └── index.html        # Main HTML template
```

---

## ⚙️ Setup Instructions

1. **Clone the repo or download ZIP**
   ```bash
   git clone https://github.com/your-username/it-support-ticket-system.git
   cd it-support-ticket-system
   ```

2. **Create virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Flask**
   ```bash
   pip install Flask
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser and visit [http://localhost:5000](http://localhost:5000)

---

## 💡 Future Improvements

- Admin login panel
- Email notifications for new tickets
- Ticket search/filter functionality
- Export tickets to CSV or PDF

---

## 🧑‍💻 Author

- **Brian Kimutai Siele**
- Email: korosbrian574@gmail.com


---

## 📝 License

This project is licensed under the MIT License.
