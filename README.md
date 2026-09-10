# VortexTech Cyber Security Internship – Week 2

## Hands-On with Basic Security Tools

This project was completed as part of the **VortexTech Cyber Security Internship – Week 2** task.

The task focused on practicing two basic cybersecurity activities:

* Building a **password strength evaluator** using Python
* Performing a **local port scan using Nmap**

## What I Built

### 1. Password Strength Evaluator

The Python script checks a password based on:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Common or easily guessed passwords

It then classifies the password as **Very Weak, Weak, Medium, or Strong** and provides feedback to improve it.

### 2. Local Port Scanning with Nmap

I used **Nmap** to scan my local machine (`localhost`) and identify open TCP ports and their associated services.

The scan was performed only on the local system for safe and authorized testing.

## Files

* `password_checker.py` — Python script for evaluating password strength
* `vortextech-cybersec-week2.pdf` — Complete report containing the implementation, test outputs, Nmap scan results, and reflection

## How to Run

### Password Strength Evaluator

Make sure Python is installed, then open a terminal in the project folder and run:

```bash
python password_checker.py
```

Enter a password when prompted, and the script will display its strength and feedback.

### Nmap Scan

If Nmap is installed, a local scan can be performed with:

```bash
nmap localhost
```

This scans the local machine and displays the open ports and detected services.

## Safety Note

Nmap was used only against `localhost` for this task. Port scanning should only be performed on systems or networks that you own or have explicit permission to test.

## Conclusion

This task provided practical experience with basic security checks. It helped me understand how password strength affects account security and how open ports can expose services running on a system.
