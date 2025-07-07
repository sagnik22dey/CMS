import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def db_setup():
    """
    Connects to Supabase and creates the necessary tables if they don't exist.
    """
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    try:
        # Check if tables exist by trying to select from them.
        # A more direct way to check for table existence can be used if the library supports it.
        # For now, we assume if the first one fails, none exist.
        supabase.table('developers').select('id').limit(1).execute()
        print("Database tables already exist.")
        return
    except Exception as e:
        print("Tables not found, creating them...")

        try:
            # Drop tables if they exist
            supabase.rpc('exec_sql', {'sql': 'DROP TABLE IF EXISTS developers CASCADE;'}).execute()
            supabase.rpc('exec_sql', {'sql': 'DROP TABLE IF EXISTS clients CASCADE;'}).execute()
            supabase.rpc('exec_sql', {'sql': 'DROP TABLE IF EXISTS projects CASCADE;'}).execute()
            print("Dropped existing tables.")
        except Exception as e:
            # Fallback for older Supabase projects
            pass

        # SQL to create the developers table
        create_developers_table_sql = """
        CREATE TABLE developers (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            name TEXT NOT NULL,
            role TEXT,
            image TEXT,
            tech TEXT,
            join_date DATE,
            current_projects TEXT,
            completed_projects INTEGER,
            clients INTEGER,
            rating INTEGER,
            status TEXT DEFAULT 'Inactive'
        );
        """

        # SQL to create the clients table
        create_clients_table_sql = """
        CREATE TABLE clients (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            name TEXT NOT NULL,
            image TEXT,
            join_date DATE,
            projects INTEGER,
            rating INTEGER,
            status TEXT DEFAULT 'Inactive'
        );
        """
        # SQL to create the projects table
        create_projects_table_sql = """
        CREATE TABLE projects (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            name TEXT NOT NULL,
            description TEXT,
            owner TEXT,
            assigned_dev TEXT,
            est_completion_date DATE,
            actual_completion_date DATE
        );
        """
        try:
            supabase.rpc('exec_sql', {'sql': create_developers_table_sql}).execute()
            print("'developers' table created successfully.")
            supabase.rpc('exec_sql', {'sql': create_clients_table_sql}).execute()
            print("'clients' table created successfully.")
            supabase.rpc('exec_sql', {'sql': create_projects_table_sql}).execute()
            print("'projects' table created successfully.")
        except Exception as creation_error:
            print(f"Error creating tables: {creation_error}")

if __name__ == '__main__':
    db_setup()