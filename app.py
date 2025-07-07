from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['userid'] == 'admin' and request.form['password'] == 'password':
        return redirect(url_for('admin'))
    return redirect(url_for('index'))

developers = [
    {
        "name": "John Doe",
        "role": "Senior Developer",
        "image": "",
        "tech": "Python, Flask, JavaScript",
        "join_date": "2022-01-15",
        "current_projects": "Project A, Project B",
        "completed_projects": 5,
        "rating": 4
    }
]

clients = [
    {
        "name": "Test Client",
        "image": "",
        "join_date": "2023-03-20",
        "projects": 2,
        "rating": 5
    }
]

@app.route('/admin')
def admin():
    return render_template('admin.html', developers=developers, clients=clients)

if __name__ == '__main__':
    app.run(debug=True)