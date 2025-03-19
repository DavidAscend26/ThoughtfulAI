# ThoughtfulAI
Technical Challenge

Package Sorting System

Description

This is a Flask-based web application that sorts packages into different stacks based on their dimensions and mass. The system categorizes packages as:

STANDARD: Neither bulky nor heavy.

SPECIAL: Either bulky or heavy.

REJECTED: Both bulky and heavy.

Features

Web interface for user input.

Automated package classification.

Error handling for invalid inputs.

Simple UI built with Bootstrap.

Installation

Prerequisites

Ensure you have Python installed (>= 3.7). You also need Flask.

Steps

Clone the repository:

git clone https://github.com/yourusername/package-sorting-system.git
cd package-sorting-system

Install dependencies:

pip install flask

Run the Flask application:

python app.py

Open your browser and go to:

http://127.0.0.1:5000/

File Structure

package-sorting-system/
│── app.py              # Main Flask application
│── templates/
│   └── index.html      # HTML template for UI
│── README.md           # Documentation

Usage

Enter the package dimensions and mass.

Click Sort Package.

View the result indicating whether the package is STANDARD, SPECIAL, or REJECTED.

License

This project is licensed under the MIT License.

Contributions

Feel free to fork the repository and submit pull requests!

Author: Your Name
