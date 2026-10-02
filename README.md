# 🏥 MediCare – Hospital Management & AI Help Line

MediCare is a Python-based hospital management application built with **Streamlit** that helps manage patients, doctors, appointments, and billing records. It also includes an **AI Help Line** that assists users with questions related to the hospital management system.

## 🚀 Features

- 👨‍⚕️ **Doctor Management** – View and manage doctor information.
- 🧑‍🤝‍🧑 **Patient Management** – Add, view, update, and manage patient records.
- 📅 **Appointment Management** – Manage and track patient appointments.
- 💳 **Billing Management** – Maintain and view billing information.
- 🤖 **AI Help Line** – Provides AI-powered assistance for common application-related questions.
- 📊 **Dashboard** – Displays important hospital management statistics.
- 📁 **CSV Data Management** – Stores and manages application data using CSV files.
- 🖥️ **Streamlit Interface** – Simple and user-friendly web interface.

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **CSV**
- **Generative AI**
- **Google Gemini** *(if used in your project)*
- **Git & GitHub**

## 📂 Project Structure

```text
MediCare-AI-Help-Line/
│
├── app.py
├── system_prompt.py
├── requirements.txt
│
├── data/
│   ├── appointments.csv
│   ├── bills.csv
│   ├── doctor.csv
│   ├── doctors.csv
│   └── patients.csv
│
├── pages/
│   ├── __init__.py
│   ├── AI_Help_Line.py
│   ├── Appointments.py
│   ├── Billing.py
│   ├── Doctors.py
│   └── Patients.py
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py
│   └── llm_helper.py
│
├── .env
├── .gitignore
└── README.md
