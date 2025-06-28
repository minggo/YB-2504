from flask import Flask, render_template

app = Flask("flask learning")

@app.route("/")
def load_image():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)