'''
Things to note:

Remember to create the SQLite database with the required tables (Movies, Genres, etc.) using the SQL queries provided earlier before running this code.
Replace the database and CSV file paths with your actual file locations.
This code assumes the first row of your CSV contains column headers. Modify the code to handle different CSV formats if needed.
Error handling is included for database connection and basic data type conversion. You may want to add more robust validation for data in the CSV file.
'''
import csv
import sqlite3

# Database path (replace with your actual database file path)
db_path = "movies.db"  # Assuming your database file is named movies.db

# CSV file path (replace with your actual file path)
csv_file = "movies.csv"


def connect_to_db():
    """Connects to the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def import_movies_from_csv():
    """Reads data from CSV and inserts into Movies and Movie_Genres tables."""
    conn = connect_to_db()
    if not conn:
        return

    cursor = conn.cursor()

    # Assuming the first row of CSV contains column headers (modify as needed)
    with open(csv_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            movie_data = [row[0], int(row[1]), row[2], int(row[3] if row[3] else None), float(row[4] if row[4] else None), row[5], row[6], row[7]]
            genres = row[8].split(",")  # Assuming genres are comma-separated

            # Insert movie data
            insert_movie_query = """
                INSERT INTO Movies (title, release_year, media_type, length, imdb_rating, mpaa_rating, description, location)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_movie_query, movie_data)

            # Get movie ID for genre association
            cursor.execute("SELECT last_insert_rowid()")
            movie_id = cursor.fetchone()[0]

            # Insert movie genres (one by one)
            for genre in genres:
                genre_name = genre.strip()  # Remove leading/trailing whitespaces
                insert_genre_query = """
                    INSERT INTO Genres (genre_name)
                    SELECT * FROM (VALUES (?)) AS tmp (genre_name)
                    WHERE NOT EXISTS (SELECT 1 FROM Genres WHERE genre_name = ?);
                """
                cursor.execute(insert_genre_query, (genre_name, genre_name))

                # Get genre ID (if genre already exists, it won't be inserted again)
                cursor.execute("SELECT genre_id FROM Genres WHERE genre_name = ?", (genre_name,))
                genre_id = cursor.fetchone()[0]

                # Link movie and genre
                insert_link_query = "INSERT INTO Movie_Genres (movie_id, genre_id) VALUES (?, ?);"
                cursor.execute(insert_link_query, (movie_id, genre_id))

    conn.commit()
    cursor.close()
    conn.close()
    print("Movies imported successfully!")


if __name__ == "__main__":
    import_movies_from_csv()
