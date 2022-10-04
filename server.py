from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=["POST", "GET"])
def main():
    return render_template('index.html')
@app.route('/results', methods=["POST", "GET"])
def results():
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/display')
@app.route('/display')
def display():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)