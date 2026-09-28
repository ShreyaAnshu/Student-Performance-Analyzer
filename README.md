# College Performance Analyzer

## Project Overview

College Performance Analyzer is a Python-based project developed to analyze the academic performance of college students.

The system collects student profile details, subject details, credits, and grade points. It calculates semester-wise SGPA and overall CGPA and analyzes the student's academic performance based on the calculated CGPA.

The project follows a modular structure in which different tasks are handled by separate Python modules.

## Features

- Collects student profile information.
- Accepts subject details for each semester.
- Stores subject name, credits, and grade points.
- Calculates SGPA for each semester.
- Calculates overall CGPA using semester-wise SGPA and credits.
- Analyzes performance based on CGPA.
- Provides performance grade and feedback.
- Supports multiple semesters.
- Displays the final academic performance clearly.

## Technologies / Tools Used

- Python
- Visual Studio Code (VS Code)
- GitHub
- Vityarthi

## Project Modules

```
College-Performance-Analyzer/
│
├── main.py
│
├── student_profile.py
│
├── subject_manager.py
│
├── sgpa.py
│
├── cgpa.py
│
├── performance.py
│
└── README.md
```

The project is divided into the following modules:

- `main.py` – Controls the complete flow of the project.
- `student_profile.py` – Collects student name, registration number, branch, and year.
- `subject_manager.py` – Collects subject name, credits, and grade points.
- `sgpa.py` – Calculates semester-wise SGPA.
- `cgpa.py` – Calculates the overall CGPA.
- `performance.py` – Analyzes CGPA and provides performance grade and feedback.

## How to Install and Run the Project

### Step 1: Install Python

Install Python on the system and ensure that Python is added to the system PATH.

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Check the Project Files

Make sure the following files are present:

- `main.py`
- `student_profile.py`
- `subject_manager.py`
- `sgpa.py`
- `cgpa.py`
- `performance.py`

### Step 4: Run the Project

Open the terminal in VS Code and run:

```bash
python main.py


