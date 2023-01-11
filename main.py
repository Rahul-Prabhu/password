from flask import Flask, render_template
import random
import string


app = Flask(__name__)

@app.route("/")
def generate_password():
    length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(password)
    return render_template("password.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)