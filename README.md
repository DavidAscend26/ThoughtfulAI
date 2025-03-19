# ThoughtfulAI
Technical Challenge

# Package Sorting System

## Description
This is a Flask-based web application that sorts packages into different stacks based on their dimensions and mass. The system categorizes packages as:
- **STANDARD**: Neither bulky nor heavy.
- **SPECIAL**: Either bulky or heavy.
- **REJECTED**: Both bulky and heavy.

## Features
- Web interface for user input.
- Automated package classification.
- Error handling for invalid inputs.
- Simple UI built with Bootstrap.

## Installation

### Prerequisites
Ensure you have Python installed (>= 3.7). You also need `Flask`.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/DavidAscend26/ThoughtfulAI.git
   cd ThoughtfulAI
   ```
2. Install dependencies:
   ```sh
   pip install flask
   ```
3. Run the Flask application:
   ```sh
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
```
package-sorting-system/
│── app.py              # Main Flask application
│── templates/
│   └── index.html      # HTML template for UI
│── README.md           # Documentation
```

## Usage
1. Enter the package dimensions and mass.
2. Click **Sort Package**.
3. View the result indicating whether the package is STANDARD, SPECIAL, or REJECTED.

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork the repository and submit pull requests!

---

**Author:** David Muñoz
