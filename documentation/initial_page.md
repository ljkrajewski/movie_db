Here's an initial framework for accessing the movie database using Python and Flask:

```python
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

```

**Explanation:**

1. **Flask Setup:** We import Flask and create a Flask application instance (`app`).
2. **Database Connection:** The `connect_to_db` function establishes a connection to the database using psycopg2.
3. **Get All Movies:** The `get_all_movies` function retrieves all movies from the `Movies` table and returns them as a list.
4. **Movies List Route:** The `@app.route("/")` decorator defines a route for the root URL (`/`). The `movies_list` function retrieves all movies using `get_all_movies` and renders the `movies.html` template, passing the list of movies as context.
5. **Template (movies.html - Not included):** This would be a separate HTML file that displays the list of movies. You can use Jinja templating syntax within the HTML to iterate through the list of movies and display their details.

**Running the Application:**

1. Replace the database connection details with your actual credentials.
2. Create a `movies.html` template file with your desired layout for displaying movies.
3. Save the code in a Python file (e.g., `movies.py`).
4. Run the application using `python movies.py`.
5. Access `http://localhost:5000/` in your web browser to see the list of all movies from the database.

**Next Steps:**

* This provides a basic framework for accessing the database.
* You can build upon this to implement functionalities like:
    * Adding a new movie form in the template and a route to handle form submission for adding movies to the database.
    * Implementing search functionality by adding a search bar to the template and modifying the route handler to retrieve movies based on search criteria.
    * Including functionalities for deleting and updating movies.
