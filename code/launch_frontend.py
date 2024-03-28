from flask import Flask, render_template, request

app = Flask(__name__)

# Database path (replace with your actual database file path)
db_path = "movies.db"  # Assuming your database file is named movies.db

def connect_to_db():
  """Connects to the SQLite database."""
  try:
      conn = sqlite3.connect(db_path)
      return conn
  except Exception as e:
      print(f"Error connecting to database: {e}")
      return None

def get_all_movies():
  """Retrieves all movies from the database."""
  conn = connect_to_db()
  if not conn:
      return None

  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Movies")
  movies = cursor.fetchall()
  cursor.close()
  conn.close()
  return movies

@app.route("/")
def movies_list():
  """Renders the main page with a list of all movies."""
  movies = get_all_movies()
  if not movies:
      return "Error retrieving movies from database"
  return render_template("movies.html", movies=movies)

if __name__ == "__main__":
  app.run(debug=True)

