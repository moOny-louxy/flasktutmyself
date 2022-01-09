from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'key_for_flask'


@app.route('/login', methods=['POST', 'GET'])
def login():  # put application's code here
    error_info = None
    if request.method == 'POST' and request.form['email'] == 'test@xxx.com' and request.form['password'] == 'test':
        return redirect(url_for('index'))
    elif request.method == 'POST' and request.form['email'] != 'test@xxx.com':
        error_info = 'Invalid User!'
    elif request.method == 'POST' and request.form['password'] != 'test':
        error_info = 'Wrong Password'

    return render_template('login.html', error=error_info)


@app.route('/index')
def index():
    flash('Logged in successfully!', 'login')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
