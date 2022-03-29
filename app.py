from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("z&d_homepage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("z&d_login.html")

@app.route("/register")
def register():
    return render_template("z&d_register.html")

if __name__ == "__main__":
    app.run(debug=True)
