from application import app, db
from flask import json, render_template, request, Response
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

courseData = [
{'courseID': '1111', 'title': 'PHP', 'description': 'Intro to PHP', 'credits': '3', 'term': 'Fall, Spring'},
{'courseID': '2222', 'title': 'Java 1', 'description': 'Intro to Java Programming', 'credits': '4', 'term': 'Spring'},
{'courseID': '3333', 'title': 'Adv PHP 201', 'description': 'Advanced PHP Programming', 'credits': '3', 'term': 'Fall'},
{'courseID': '4444', 'title': 'Angular 1', 'description': 'Intro to Angular', 'credits': '3', 'term': 'Fall, Spring'},
{'courseID': '5555', 'title': 'Java 2', 'description': 'Advanced Java Programming', 'credits': '4', 'term': 'Fall'}
]

# Creating some default routes
@app.route('/')
@app.route('/index')
@app.route('/barf')
def index():
    return render_template('index.html', index=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form, login=True, title='Login')

@app.route('/courses')
@app.route('/courses/<term>')
def courses(term='Spring 2019'):
    return render_template('courses.html', courseData = courseData, courses=True, term=term)

@app.route('/register')
def register():
    return render_template('register.html', register=True)

@app.route('/enrollment', methods=['GET', 'POST'])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template('enrollment.html', data={'courseID': id, 'title': title, 'term': term})

@app.route('/api/')
@app.route('/api/<index>')
def api(index=None):
    if (index==None):
        jsonData = courseData
    else:
        jsonData = courseData[int(index)]

    return Response(json.dumps(jsonData), mimetype='application/json')

@app.route('/users')
def user():
    # User(user_id=1, first_name='Alma', last_name='Alfalfa', email='alma.alfalfa@uta.com', password='abc123').save()
    # User(user_id=2, first_name='Bernie', last_name='Baptista', email='bernie.baptista@uta.com', password='abc123').save()
    users = User.objects.all()
    return render_template('users.html', users=users)
