from flask import Flask, render_template, request, redirect, url_for
from dbsetup import db_setup
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Initialize Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Setup the database
db_setup()

@app.route('/')
def index():
    return render_template('signIn.html')

@app.route('/signin', methods=['POST'])
def signin():
    if request.form.get('user_id') == 'admin' and request.form.get('password') == 'password':
        return redirect(url_for('admin'))
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    try:
        developers_response = supabase.table('developers').select('*').execute()
        clients_response = supabase.table('clients').select('*').execute()
        projects_response = supabase.table('projects').select('*').execute()
        
        developers = developers_response.data if developers_response.data else []
        clients = clients_response.data if clients_response.data else []
        projects = projects_response.data if projects_response.data else []
    except Exception as e:
        print(f"Error fetching data: {e}")
        developers = []
        clients = []
        projects = []

    return render_template('admin.html', developers=developers, clients=clients, projects=projects)
@app.route('/add_developer', methods=['POST'])
def add_developer():
    developer_data = {
        "name": request.form.get('name'),
        "role": request.form.get('role'),
        "image": request.form.get('image'),
        "tech": request.form.get('tech'),
        "join_date": request.form.get('join_date'),
        "current_projects": request.form.get('current_projects'),
        "completed_projects": request.form.get('completed_projects'),
        "rating": request.form.get('rating')
    }
    try:
        supabase.table('developers').insert(developer_data).execute()
    except Exception as e:
        print(f"Error inserting new developer: {e}")
    return redirect(url_for('admin'))

@app.route('/edit_developer/<int:developer_id>', methods=['POST'])
def edit_developer(developer_id):
    developer_data = {
        "name": request.form.get('name'),
        "role": request.form.get('role'),
        "image": request.form.get('image'),
        "tech": request.form.get('tech'),
        "join_date": request.form.get('join_date'),
        "current_projects": request.form.get('current_projects'),
        "completed_projects": request.form.get('completed_projects'),
        "rating": request.form.get('rating')
    }
    try:
        supabase.table('developers').update(developer_data).eq('id', developer_id).execute()
    except Exception as e:
        print(f"Error updating developer: {e}")
    return redirect(url_for('admin'))

@app.route('/delete_developer/<int:developer_id>', methods=['POST'])
def delete_developer(developer_id):
    try:
        supabase.table('developers').delete().eq('id', developer_id).execute()
    except Exception as e:
        print(f"Error deleting developer: {e}")
    return redirect(url_for('admin'))

@app.route('/add_client', methods=['POST'])
def add_client():
    client_data = {
        "name": request.form.get('name'),
        "image": request.form.get('image'),
        "join_date": request.form.get('join_date'),
        "projects": request.form.get('projects'),
        "rating": request.form.get('rating')
    }
    try:
        supabase.table('clients').insert(client_data).execute()
    except Exception as e:
        print(f"Error inserting new client: {e}")
    return redirect(url_for('admin'))

@app.route('/edit_client/<int:client_id>', methods=['POST'])
def edit_client(client_id):
    client_data = {
        "name": request.form.get('name'),
        "image": request.form.get('image'),
        "join_date": request.form.get('join_date'),
        "projects": request.form.get('projects'),
        "rating": request.form.get('rating')
    }
    try:
        supabase.table('clients').update(client_data).eq('id', client_id).execute()
    except Exception as e:
        print(f"Error updating client: {e}")
    return redirect(url_for('admin'))

@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    try:
        supabase.table('clients').delete().eq('id', client_id).execute()
    except Exception as e:
        print(f"Error deleting client: {e}")
    return redirect(url_for('admin'))

@app.route('/add_project', methods=['POST'])
def add_project():
    project_data = {
        "name": request.form.get('name'),
        "description": request.form.get('description'),
        "owner": request.form.get('owner'),
        "assigned_dev": request.form.get('assigned_dev'),
        "est_completion_date": request.form.get('est_completion_date'),
        "actual_completion_date": request.form.get('actual_completion_date')
    }
    try:
        supabase.table('projects').insert(project_data).execute()
    except Exception as e:
        print(f"Error inserting new project: {e}")
    return redirect(url_for('admin'))

@app.route('/edit_project/<int:project_id>', methods=['POST'])
def edit_project(project_id):
    project_data = {
        "name": request.form.get('name'),
        "description": request.form.get('description'),
        "owner": request.form.get('owner'),
        "assigned_dev": request.form.get('assigned_dev'),
        "est_completion_date": request.form.get('est_completion_date'),
        "actual_completion_date": request.form.get('actual_completion_date')
    }
    try:
        supabase.table('projects').update(project_data).eq('id', project_id).execute()
    except Exception as e:
        print(f"Error updating project: {e}")
    return redirect(url_for('admin'))

@app.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    try:
        supabase.table('projects').delete().eq('id', project_id).execute()
    except Exception as e:
        print(f"Error deleting project: {e}")
    return redirect(url_for('admin'))
@app.route('/edit_developer_card/<int:developer_id>', methods=['POST'])
def edit_developer_card(developer_id):
    developer_data = {
        "name": request.form.get('name'),
        "role": request.form.get('role'),
        "tech": request.form.get('tech'),
        "completed_projects": request.form.get('completed_projects'),
        "rating": request.form.get('rating'),
        "clients": request.form.get('clients'),
        "current_projects": request.form.get('current_projects')
    }
    try:
        supabase.table('developers').update(developer_data).eq('id', developer_id).execute()
    except Exception as e:
        print(f"Error updating developer card: {e}")
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)