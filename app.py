from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/expertise')
def expertise():
    return render_template('expertise.html')

@app.route('/industries')
def industries():
    return render_template('industries.html')

@app.route('/case-studies')
def case_studies():
    return render_template('case_studies.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)