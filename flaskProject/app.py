from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from datetime import timedelta

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_PERMANENT_LIFETIME'] = timedelta(minutes=20)


@app.route('/home')
@app.route('/')
def home_route():
    username = ''
    return render_template("homepage.html", username=username)

@app.route('/home')
def home_func():
    return redirect('/')

@app.route('/homepage')
def homepage_func():
    return redirect(url_for('home_route'))

@app.route('/contact')
def contact_func():
    return render_template("contact.html")


curr_user= {'firstname': "Tal", 'Lastname': "Barokas"}
#curr_user = ''
@app.route('/assignment3_1' )
def assignment3_1():
    return render_template("assignment3_1.html",
                           hobbies=['Dance', 'Sing', 'Reading Books', 'Watch movies', 'Traveling'], curr_user=curr_user)


users = {'Yossi': {'email': "yossi@gmail.com"}, 'Namma': {'email': "Namma@gmail.com"},
                                                         'Arseni': {'email': "Arseni@gmail.com"}, 'Rotem': {'email': "Rotem@gmail.com"},
                                                         'Moshe': {'email': 'Moshe@gmail.com'}}
users_dict ={'arseni':'1234', 'Yossi':'5678'}
@app.route('/assignment3_2', methods= ['GET','POST'])
def assignment3_2():
    if request.method == 'POST':
        username = request.form['user_name']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
        if username in users_dict:
            pas_in_dict = users_dict[username]
            if pas_in_dict == password:
                session['username'] = username
                return render_template('assignment3_2.html', message='Wellcom', username=username)
            else:
                return render_template('assignment3_2.html', message='Wrong password')
        else:
            new_user={username: password}
            users_dict.update(new_user)
            return render_template('assignment3_2.html', message='registration Succeed')

    return render_template('assignment3_2.html')



@app.route('/friends')
def friends():
    return render_template("friends.html", hobbies=['Dance', 'Sing', 'Reading Books', 'Watch movies', 'Traveling'], curr_user=curr_user)


@app.route('/log_out')
def logout():
    session.clear()
    return redirect(url_for('assignment3_2'))

if __name__ == '__main__':
    app.run(debug=True)
