from flask import Flask, render_template

app = Flask("hello_world")

@app.route("/")
def hello_flask():
    return render_template('index.html')

@app.route("/username/<name>")
def learn(name):
    return f"{name} is learning Flask!"

if __name__ == '__main__':
    app.run(debug=True)