# 🦁 Masterblog - TheBlogSpot

Welcome to **Masterblog**, a fully functional CRUD (Create, Read, Update, Delete) web application built with **Flask**. This project allows users to manage a personal blog, with all data being stored persistently in a JSON-based database.

## ✨ Features
* **Read:** View all blog posts on a clean, modern homepage.
* **Create:** Add new posts with a title, author name, and content.
* **Update:** Edit existing posts using a pre-filled form to correct or update information.
* **Delete:** Remove posts securely with a confirmation prompt to prevent accidental loss of data.
* **Persistent Storage:** Uses `posts.json` to ensure your data is saved even if the server restarts.
* **Modern UI:** Styled with a custom "TheBlogSpot" CSS theme for a professional look.

## 🛠️ Tech Stack
* **Backend:** Python 3 with Flask
* **Frontend:** HTML5, CSS3, Jinja2 Templates
* **Database:** JSON (File-based storage)
* **Version Control:** Git & GitHub

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Masterblog.git](https://github.com/YOUR_USERNAME/Masterblog.git)
    cd Masterblog
    ```

2.  **Set up a Virtual Environment (Optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install Flask:**
    ```bash
    pip install flask
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **View the blog:**
    Open your browser and navigate to `http://127.0.0.1:5001` (or the port specified in your terminal).

## 📁 Project Structure
* `app.py`: The main Flask application logic and routing.
* `posts.json`: The data storage file.
* `templates/`: Contains `index.html`, `add.html`, and `update.html`.
* `static/`: Contains `style.css` for the blog's design.

---
Created by **TheBlogSpot** 🚀
