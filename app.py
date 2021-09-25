from flask import Flask, render_template

from controllers.dogs_controller import dogs_blueprint
from controllers.appointments_controller import appointments_blueprint

app = Flask(__name__)

app.register_blueprint(dogs_blueprint)
app.register_blueprint(appointments_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()