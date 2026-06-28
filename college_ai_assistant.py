import tkinter as tk
from tkinter import scrolledtext
import sqlite3

root = tk.Tk()
root.title("College AI Assistant")
root.geometry("1000x600")
root.configure(bg="white")

# ================== FUNCTIONS ==================

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# ---------- CHATBOT ----------
def open_chatbot():
    clear_content()

    tk.Label(
        content_frame,
        text="College AI Chatbot",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    chat_area = scrolledtext.ScrolledText(
        content_frame,
        width=70,
        height=20
    )
    chat_area.pack(pady=10)

    chat_area.insert(
        tk.END,
        """Welcome to College AI Assistant

Ask:
• library
• fees
• exam
• attendance
• placement

"""
    )

    def send_message():
        user = entry.get().lower()

        if "library" in user:
            response = "Library Timing: 9 AM - 5 PM"

        elif "fees" in user:
            response = "Contact Accounts Department"

        elif "exam" in user:
            response = "Exam starts from 10 July"

        elif "attendance" in user:
            response = "Minimum attendance required is 75%"

        elif "placement" in user:
            response = "Placement Cell is in Block B"

        else:
            response = "Information not available"

        chat_area.insert(tk.END, "You: " + entry.get() + "\n")
        chat_area.insert(tk.END, "Bot: " + response + "\n\n")

        entry.delete(0, tk.END)

    entry = tk.Entry(content_frame, width=50)
    entry.pack(side=tk.LEFT, padx=20)

    tk.Button(
        content_frame,
        text="Send",
        command=send_message
    ).pack(side=tk.LEFT)

# ---------- ATTENDANCE ----------
def open_attendance():
    clear_content()

    tk.Label(
        content_frame,
        text="Attendance Checker",
        font=("Arial",18,"bold")
    ).pack(pady=20)

    tk.Label(
        content_frame,
        text="Enter Roll Number"
    ).pack()

    roll_entry = tk.Entry(content_frame)
    roll_entry.pack()

    result_label = tk.Label(
        content_frame,
        text="",
        font=("Arial",12)
    )
    result_label.pack(pady=20)

    def check():

        roll = roll_entry.get()

        conn = sqlite3.connect("college.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name, attendance FROM students WHERE roll_no=?",
            (roll,)
        )

        data = cursor.fetchone()

        conn.close()

        if data:
            result_label.config(
                text=f"Name: {data[0]}\nAttendance: {data[1]}%"
            )
        else:
            result_label.config(
                text="Student Not Found"
            )

    tk.Button(
        content_frame,
        text="Check Attendance",
        command=check
    ).pack(pady=10)
# ---------- RESULTS ----------
def open_results():
    clear_content()

    tk.Label(
        content_frame,
        text="Result Checker",
        font=("Arial",18,"bold")
    ).pack(pady=20)

    tk.Label(
        content_frame,
        text="Enter Roll Number"
    ).pack()

    roll_entry = tk.Entry(content_frame)
    roll_entry.pack()

    result_label = tk.Label(
        content_frame,
        text="",
        justify="left",
        font=("Arial",12)
    )
    result_label.pack(pady=20)

    def show_result():
        roll = roll_entry.get()

        if roll == "1":
            result_label.config(
                text="""
Name: Aarya

Python: 90
DBMS: 85
Java: 88
Maths: 92

Percentage: 88.75%
"""
            )

        elif roll == "2":
            result_label.config(
                text="""
Name: Rahul

Python: 75
DBMS: 80
Java: 78
Maths: 82

Percentage: 78.75%
"""
            )

        else:
            result_label.config(
                text="Student Not Found"
            )

    tk.Button(
        content_frame,
        text="Show Result",
        command=show_result
    ).pack(pady=10)

# ---------- NOTICE BOARD ----------
def open_notice():
    clear_content()

    tk.Label(
        content_frame,
        text="Notice Board",
        font=("Arial",18,"bold")
    ).pack(pady=10)

    notice_area = scrolledtext.ScrolledText(
        content_frame,
        width=70,
        height=20
    )
    notice_area.pack(pady=10)

    notice_text = """
1. Semester Examination starts from 10 July.

2. Project Submission Last Date: 5 July.

3. Library Books Return Before 30 June.

4. Placement Drive on 15 July.

5. Sports Registration Last Date: 3 July.
"""

    notice_area.insert(tk.END, notice_text)
    notice_area.config(state="disabled")

# ---------- HOME ----------
def open_home():
    clear_content()

    tk.Label(
        content_frame,
        text="Welcome To College AI Assistant",
        font=("Arial",22,"bold")
    ).pack(pady=40)

    tk.Label(
        content_frame,
        text="BE Second Year Mini Project",
        font=("Arial",14)
    ).pack()

# ================== SIDEBAR ==================

sidebar = tk.Frame(root, bg="lightblue", width=220)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(
    sidebar,
    text="MENU",
    bg="lightblue",
    font=("Arial",18,"bold")
).pack(pady=20)

tk.Button(
    sidebar,
    text="Home",
    width=20,
    command=open_home
).pack(pady=5)

tk.Button(
    sidebar,
    text="AI Chatbot",
    width=20,
    command=open_chatbot
).pack(pady=5)

tk.Button(
    sidebar,
    text="Attendance",
    width=20,
    command=open_attendance
).pack(pady=5)

tk.Button(
    sidebar,
    text="Results",
    width=20,
    command=open_results
).pack(pady=5)

tk.Button(
    sidebar,
    text="Notice Board",
    width=20,
    command=open_notice
).pack(pady=5)

tk.Button(
    sidebar,
    text="Exit",
    width=20,
    command=root.destroy
).pack(pady=20)

# ================== CONTENT AREA ==================

content_frame = tk.Frame(root, bg="white")
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

open_home()

root.mainloop()