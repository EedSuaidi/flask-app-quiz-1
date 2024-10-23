from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about', name="Moh. Su'aidi", npm="5230411271")

if __name__ == "__main__":
    app.run(debug=True)