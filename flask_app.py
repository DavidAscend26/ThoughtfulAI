from flask import Flask, render_template, request


def sort(width, height, length, mass):
    """
    Sorts packages into the correct stack based on their volume and mass.

    Parameters:
        width (int): Width of the package in cm.
        height (int): Height of the package in cm.
        length (int): Length of the package in cm.
        mass (int): Mass of the package in kg.

    Returns:
        str: The stack where the package should go ('STANDARD', 'SPECIAL', 'REJECTED').
    """
    if not all(isinstance(i, (int, float)) and i > 0 for i in [width, height, length, mass]):
        raise ValueError("All dimensions and mass must be positive numbers.")

    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in (width, height, length))
    is_heavy = mass >= 20

    return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"


# Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            width = float(request.form['width'])
            height = float(request.form['height'])
            length = float(request.form['length'])
            mass = float(request.form['mass'])
            result = sort(width, height, length, mass)
        except ValueError:
            result = "Invalid input! Please enter valid positive numbers."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)