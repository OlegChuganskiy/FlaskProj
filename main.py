from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def randomizer():
    # Генеруємо випадкове число від 1 до 6
    random_number = random.randint(1, 6)
    return render_template("index.html", number=random_number)

if __name__ == '__main__':
    app.run(debug=True)
